#!/usr/bin/env bash
# One-shot environment setup for a 4xH100 box running Nicole's DeepSeek V4 Flash pipeline.
# Follows README.md "Reproduction". Stops before the gated download unless HF auth is present.
set -eo pipefail
export WORK=${WORK:-$HOME/jlens-filler}
export PATH="$HOME/.local/bin:$PATH"
cd "$WORK"
if [ ! -d "$WORK/.venv" ]; then
  python3 -m venv "$WORK/.venv"
fi
source "$WORK/.venv/bin/activate"
pip install -q --upgrade pip
pip install -q wheel setuptools ninja packaging
export CUDA_HOME=${CUDA_HOME:-/usr/local/cuda}
pip install -q 'torch==2.10.0' 'transformers==5.0.0' 'safetensors>=0.7' 'tilelang==0.1.8' 'apache-tvm-ffi==0.1.3' 'huggingface-hub>=1.2' numpy jinja2 plotly matplotlib pytest
if ! python -c "import fast_hadamard_transform" 2>/dev/null; then
  [ -d "$WORK/fast-hadamard-transform/.git" ] || git clone --recursive -q https://github.com/Dao-AILab/fast-hadamard-transform.git "$WORK/fast-hadamard-transform"
  pip install -q --no-build-isolation "$WORK/fast-hadamard-transform"
fi
python -c "import torch, transformers, tilelang; print('torch', torch.__version__, 'cuda', torch.cuda.is_available(), torch.cuda.device_count(), 'gpus | transformers', transformers.__version__, '| tilelang', tilelang.__version__)"
python -m pytest -q tests | tail -1
mkdir -p "$WORK/cache"
# ungated pieces first
hf download camilablank/workspace-lenses deepseek-v4-flash/j-lens/lens.pt --revision 781b233 --local-dir "$WORK/cache/lens_repo" 2>&1 | tail -1
if hf auth whoami >/dev/null 2>&1; then
  echo "HF auth present; downloading gated DeepSeek-V4-Flash (149 GiB) ..."
  hf download deepseek-ai/DeepSeek-V4-Flash --revision 60d8d70770c6776ff598c94bb586a859a38244f1 --local-dir "$WORK/cache/model_hf" 2>&1 | tail -1
  du -sh "$WORK/cache/model_hf"
  echo "converting to 4-way model parallel (about an hour, ~330 GB disk peak) ..."
  python "$WORK/cache/model_hf/inference/convert.py" --hf-ckpt-path "$WORK/cache/model_hf" --save-path "$WORK/cache/model_mp4" --n-experts 256 --model-parallel 4
  cp "$WORK/cache/model_hf"/tokenizer*.json "$WORK/cache/model_mp4/"
  du -sh "$WORK/cache/model_mp4"
  echo SETUP_DONE
else
  echo "NOT LOGGED IN: run 'hf auth login' on this box, then rerun this script."
  echo SETUP_NEEDS_AUTH
fi
