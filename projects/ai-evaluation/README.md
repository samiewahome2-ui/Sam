# AI response evaluation

A small, deterministic demonstration of rubric-based review. It summarizes human-assigned ratings rather than claiming to automatically verify factual accuracy.

## Rubric

| Criterion | Scale |
|---|---|
| Factual accuracy | 0 = incorrect, 1 = partial, 2 = supported |
| Instruction adherence | 0 = missed, 1 = partial, 2 = met |
| Clarity | 0 = unclear, 1 = adequate, 2 = clear |

Critical errors override numerical scores. A response passes when there is no critical error and the total is at least 5/6.

Run `python projects/ai-evaluation/evaluate.py` from the root. The fictional cases yield one pass and two review decisions.

**Next evidence to add:** authorized evaluation samples, reviewer agreement and measured error rates.
