"""Reproduce the historical handoff and figures; no model inference required."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parent
SOURCE = Path('/Users/nicolema/Documents/Codex/2026-09-04/can-y/outputs/jlens-chat-history/main-project-conversation.md')
BLUE, TEAL, ORANGE, GRAY = '#2858a5', '#158477', '#c86b29', '#657184'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11, 'axes.spines.top': False,
 'axes.spines.right': False, 'axes.titleweight': 'bold', 'axes.labelcolor': '#253247',
 'text.color': '#253247', 'axes.edgecolor': '#ccd3dd', 'savefig.facecolor': 'white'})
DATA = {
 'source_message_utc': '2026-09-04T20:36:48.591Z',
 'provenance': 'Values transcribed from the historical conversation summary; not a fresh raw-data audit.',
 'independent_100': {'dots': [0,5,25,50,100], 'accuracy_percent': [59,74,79,94,96]},
 'initial_50': {'dots': [0,5,50,100], 'accuracy_percent': [70,90,98,98]},
 'window_35_selected_rescued': {'predecessors': ['0','1','2','4','8','16','32','Full'], 'correct': [7,14,28,29,30,31,33,35]},
 'path_10_selected_rescued': {'condition': ['Full setup','Block local dot communication','Block compressed dot communication','Block local answer access','Only local answer access'], 'correct': [10,2,9,4,10]},
 'patch_single_example': {'condition': ['Before patch','Full donor state','J-Lens-orthogonal remainder'], 'donor_answer_rank': [73,3,8]},
 'layer_schematic': {'base': 24, 'bound_value': 31, 'later_product': 31, 'answer': 36},
}
(ROOT/'figure-data.json').write_text(json.dumps(DATA, indent=2)+'\n')

def save(fig, name):
    fig.savefig(ROOT/'figures'/f'{name}.png', dpi=180, bbox_inches='tight')
    fig.savefig(ROOT/'figures'/f'{name}.svg', bbox_inches='tight')
    plt.close(fig)

fig, ax = plt.subplots(figsize=(9,4.6), layout='constrained')
for key, label, color in [('initial_50','Initial 50 examples',GRAY),('independent_100','Independent 100 examples',BLUE)]:
    d=DATA[key]; ax.plot(d['dots'],d['accuracy_percent'],'o-',label=label,color=color,lw=2.3)
for x,y in zip(DATA['independent_100']['dots'],DATA['independent_100']['accuracy_percent']):
    ax.annotate(f'{y}%',(x,y),xytext=(0,-19),textcoords='offset points',ha='center',color=BLUE)
ax.set(xlabel='Number of filler dots',ylabel='Exact-match accuracy (%)',ylim=(45,105),xticks=[0,5,25,50,100],
 title='Variable binding: accuracy improves with filler length')
ax.grid(axis='y',alpha=.18); ax.legend(loc='lower right',frameon=False)
save(fig,'01-accuracy')

fig, ax = plt.subplots(figsize=(10,4.5),layout='constrained')
ax.set(xlim=(-1,50),ylim=(41,19),xlabel='Filler position (schematic)',ylabel='Layer depth',
 title='J-Lens readouts: stages emerge across layers',yticks=[24,31,36],xticks=[1,10,20,30,40,50])
for y,label,color in [(24,'Base value  ·  around layer 24',BLUE),(31,'Bound value / later product  ·  around layer 31',TEAL),(36,'Final answer  ·  around layer 36',ORANGE)]:
    ax.axhspan(y-.7,y+.7,color=color,alpha=.12)
    ax.text(25,y,label,ha='center',va='center',weight='bold',color=color)
ax.text(25,39.5,'Illustration of reported ordering, not measured cell locations.\nAcross 14 rescued examples; no consistent one-step-per-dot ordering.',ha='center',va='center',fontsize=10,color=GRAY)
save(fig,'02-layer-progression')

fig,(ax,bx)=plt.subplots(1,2,figsize=(11,4.8),gridspec_kw={'width_ratios':[1.35,1]},layout='constrained')
d=DATA['window_35_selected_rescued']; vals=[n/35*100 for n in d['correct']]
ax.plot(range(8),vals,'o-',lw=2.4,color=BLUE)
for i,(n,y) in enumerate(zip(d['correct'],vals)):
    ax.annotate(f'{y:.0f}%\n{n}/35',(i,y),xytext=(0,9),textcoords='offset points',ha='center',fontsize=9)
ax.set(xticks=range(8),xticklabels=d['predecessors'],ylim=(0,119),yticks=[0,20,40,60,80,100],
 xlabel='Recent predecessor dots allowed',ylabel='Accuracy (%)',title='Most of the benefit survives a short window')
ax.grid(axis='y',alpha=.18)
bx.set(xlim=(0,10),ylim=(0,6)); bx.axis('off')
for x,label in [(1,'Dot 8'),(4,'Dot 9'),(7,'Dot 10')]:
    bx.add_patch(FancyBboxPatch((x,3),2,1,boxstyle='round,pad=.12',facecolor='#e8eff9',edgecolor=BLUE))
    bx.text(x+1,3.5,label,ha='center',va='center',weight='bold')
bx.annotate('',xy=(7,3.5),xytext=(6.1,3.5),arrowprops={'arrowstyle':'->','color':BLUE,'lw':2})
bx.annotate('',xy=(8,4.12),xytext=(2,4.12),arrowprops={'arrowstyle':'->','color':TEAL,'lw':2,'connectionstyle':'arc3,rad=-.3'})
bx.text(5,1.6,'Two-dot window:\nDot 10 can read dots 8 and 9.\nAll 50 dots remain in the prompt.',ha='center',va='center')
bx.text(5,.35,'Exact local-attention restriction;\nother routes remain available.',ha='center',fontsize=9,color=GRAY)
save(fig,'03-rolling-window')

fig,ax=plt.subplots(figsize=(10,4.8),layout='constrained')
d=DATA['path_10_selected_rescued']; colors=[BLUE,ORANGE,TEAL,ORANGE,TEAL]
ax.barh(d['condition'],d['correct'],color=colors,height=.6)
for i,n in enumerate(d['correct']): ax.text(n+.12,i,f'{n}/10',va='center',weight='bold')
ax.invert_yaxis(); ax.set(xlim=(0,11.3),xticks=[0,2,4,6,8,10],xlabel='Correct answers out of 10 selected rescued examples',
 title='Attention interventions: the local route matters most')
save(fig,'04-attention-paths')

fig,(ax,bx)=plt.subplots(1,2,figsize=(11,4.8),layout='constrained',gridspec_kw={'width_ratios':[1,1.15]})
d=DATA['patch_single_example']; labels=['Before\npatch','Full donor\nstate','J-orthogonal\nremainder']
ax.bar(labels,d['donor_answer_rank'],color=[GRAY,BLUE,TEAL],width=.58)
for i,n in enumerate(d['donor_answer_rank']):ax.text(i,n+2,str(n),ha='center',weight='bold')
ax.set(ylim=(0,85),ylabel='Donor-answer rank (lower is better)',title='One strong causal-patching example')
bx.axis('off')
bx.text(.02,.93,'Readout change ≠ answer change',fontsize=15,weight='bold',va='top')
bx.text(.02,.77,'Expected-token J-Lens component\n• About 2% of the state-change norm\n• Roughly two-thirds of readout change\n• About 8% of intermediate causal effect\n• Essentially no final-answer causal effect',va='top',linespacing=1.7,fontsize=11)
bx.text(.02,.30,'Orthogonal remainder\nRetained roughly 80% of causal transfer.',va='top',linespacing=1.7,color=TEAL,weight='bold')
bx.text(.02,.06,'Pilot summary; percentages are approximate.\nNorm, readout, and causal effect are different measures.',va='top',fontsize=9,color=GRAY)
save(fig,'05-state-dissection')

source=SOURCE.read_text()
start=source.index('## Assistant — 2026-09-04T20:36:48.591Z')
body=source[start:].split('\n',1)[1]
body=body[:body.index('\n## User —')].strip()
(ROOT/'original-summary.md').write_text(body+'\n')
insertions={
 '# 6. What J-Lens': ('01-accuracy','Figure 1. Exact-match accuracy on two reported variable-binding cohorts. Lines connect tested dot counts; they do not represent measurements between them. Some historical sweeps changed demonstration filler as well as target filler.'),
 '# 7. More dots': ('02-layer-progression','Figure 2. Schematic of the approximate first-decodable layer ordering reported across 14 rescued examples. Bands are illustrative, not measured layer × position heatmaps.'),
 '# 10. Local attention': ('03-rolling-window','Figure 3. All 50 dots remain present. The intervention restricts recent predecessor access through exact local attention. These 35 examples were selected because 50 dots rescued them; full-history accuracy is therefore 100% by selection. Other communication routes remain available. This figure does not use J-Lens.'),
 '# 11. Candidate competition': ('04-attention-paths','Figure 4. Reported attention-path interventions on ten selected rescued examples. These are causal masking results, not J-Lens readouts, and are not overall task accuracies.'),
 '# 17. DeepSeek': ('05-state-dissection','Figure 5. Left: one reported donor-state patch, showing donor-answer rank before and after intervention. Right: approximate state-dissection pilot summaries. The J-Lens component uses the tested expected-token directions, not every possible J-Lens direction. Norm share, readout change, and causal transfer are different quantities.'),
}
for prefix,(name,caption) in insertions.items():
    pos=body.index(prefix)
    block=f'![{caption}](figures/{name}.png)\n\n*{caption}*\n\n---\n\n'
    body=body[:pos]+block+body[pos:]
header='''# JLENS project — illustrated results handoff

**Historical snapshot:** September 4, 2026, 20:36 UTC.  
**Scope:** The original detailed 18-part conversation summary, preserved verbatim with figures inserted. The text reports prior experiments; this handoff does not rerun them or independently audit raw outputs. Later work in the repository is outside this snapshot.

## Reading and reuse

- The main summary below retains the original wording, including its interpretations. Figure captions and the handoff notes distinguish selected cohorts, schematics, and limitations.
- Open this file in a Markdown viewer. Keep the adjacent `figures/` folder when sharing it. Each figure is supplied as PNG and SVG.
- `original-summary.md` contains the exact source summary without figures. `figure-data.json` records the plotted values. `build_handoff.py` regenerates this package with Python and Matplotlib; its source path may need updating on another computer.
- Source: `main-project-conversation.md`, assistant message `2026-09-04T20:36:48.591Z`. No credentials or connection details are included.

---

'''
footer='''

---

## Handoff notes — interpretation and next work

These notes are additions to the historical response above.

- **Calibration wording:** Section 2's weak `80` result refers to the numeric token. Earlier records also report the lexical token ` eighty` as J-Lens top-1 at layer 40, filler 4.
- **Layer and stream compatibility:** Exact final-head closure and the layer-41 identity check do not independently confirm the projection used when the pretrained lens was fitted. Publisher confirmation remains relevant.
- **Scope of causal claims:** Attention-mask results are separate from J-Lens-guided evidence. Masking can introduce distribution shifts. The short-window experiment does not establish a literal two-register circuit.
- **Direction interventions:** Successful local score edits with little answer change show robustness to the tested edits. They do not prove universal non-necessity or non-sufficiency of every J-Lens direction.
- **State dissection:** The approximately 2% figure concerns donor–target state-change norm, not total activation norm or explained variance. The orthogonal remainder is defined relative to the tested token span.
- **Generalization:** Strong behavioral cohorts and small selected mechanistic cohorts answer different questions. Stream roles, candidate competition, and sparse decomposition need broader replication.

### Outstanding baselines at the end of the supplied conversation

1. Alternative filler identities, with tokenization and length controlled.
2. Target-dot sweeps with demonstration geometry held fixed.
3. Full 50–100-example J-Lens/logit-lens Recall@k and MRR, stratified by answer correctness.
4. Cross-example mean-subtracted scores, alongside raw scores.
5. Shuffled J-Lens layer assignments.
6. Larger held-out causal and mHC-stream cohorts.
7. Cross-model comparisons calibrated away from floor and ceiling.
8. Matched attention-mask controls for intervention distribution shift.
9. Additional dataset seeds and checkpoint/revision replication where feasible.

This is the historical gap list, not a claim that the current repository still lacks every item.
'''
(ROOT/'jlens-results-handoff.md').write_text(header+body+footer)
print(ROOT/'jlens-results-handoff.md')
