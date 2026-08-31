#!/usr/bin/env python3
"""Minimal NCCL smoke test for manually assigned distributed ranks."""

from __future__ import annotations

import json
import os
import socket
import time
from datetime import timedelta

import torch
import torch.distributed as dist


def main() -> None:
    rank = int(os.environ["RANK"])
    local_rank = int(os.environ["LOCAL_RANK"])
    world_size = int(os.environ["WORLD_SIZE"])
    torch.cuda.set_device(local_rank)
    dist.init_process_group(
        "nccl",
        timeout=timedelta(minutes=3),
        device_id=torch.device("cuda", local_rank),
    )

    scalar = torch.tensor(float(rank + 1), device="cuda")
    dist.all_reduce(scalar)
    expected = world_size * (world_size + 1) / 2
    if scalar.item() != expected:
        raise AssertionError(f"all-reduce returned {scalar.item()}, expected {expected}")

    payload = torch.full((16 * 1024 * 1024,), rank + 1, dtype=torch.float32, device="cuda")
    torch.cuda.synchronize()
    started = time.monotonic()
    dist.all_reduce(payload)
    torch.cuda.synchronize()
    elapsed = time.monotonic() - started
    if not torch.all(payload == expected):
        raise AssertionError("large all-reduce produced incorrect values")

    print(
        json.dumps(
            {
                "rank": rank,
                "local_rank": local_rank,
                "world_size": world_size,
                "hostname": socket.gethostname(),
                "gpu": torch.cuda.get_device_name(local_rank),
                "sum": scalar.item(),
                "large_all_reduce_seconds": elapsed,
                "status": "passed",
            },
            sort_keys=True,
        ),
        flush=True,
    )
    dist.destroy_process_group()


if __name__ == "__main__":
    main()
