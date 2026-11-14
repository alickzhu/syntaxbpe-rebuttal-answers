# Corrected confidence intervals and per-task outcomes

We have corrected an implementation issue in the confidence-interval calculation. The pass@1 point estimates are unchanged. The intervals below supersede the previously reported HE+ and MBPP+ intervals. The Base 1B HE+ interval excludes zero; the other seven intervals include zero.

Each cell reports the SyntaxBPE-minus-GPT-5-style pass@1 difference in percentage points, followed by its pointwise 95% paired hierarchical-bootstrap confidence interval.

| Stage | Size | HE+ | MBPP+ |
|---|---|---|---|
| Base | 1B | +3.5 [+1.3, +5.8] | +1.7 [-0.5, +3.9] |
| Base | 3B | +1.5 [-0.8, +4.0] | +1.6 [-0.4, +3.7] |
| SFT | 1B | +2.3 [-1.6, +6.3] | +3.0 [-0.5, +6.6] |
| SFT | 3B | +1.6 [-2.1, +5.4] | +2.2 [-0.1, +4.5] |

## Reproducing the intervals

Run `python recompute_intervals.py` from this repository. The [script](recompute_intervals.py) uses 5,000 bootstrap replicates and random seed 42 independently for each dataset. Each replicate resamples tasks with replacement, sharing the task resample between models, and independently resamples the 10 binary completion outcomes within each sampled model–task cell. The bounds are the 2.5th and 97.5th percentiles, using linear interpolation; the table rounds to one decimal place. The script reads the supplied pass/fail labels and does not re-execute generated code.

## Per-task outcomes

The files contain both models' generated completions and pass/fail outcomes. HE+ contains 164 tasks and MBPP+ contains 378 tasks, with 10 completions per model per task. The `group`, `task_id`, and `sample_idx` fields identify each record.

| Stage | Size | HE+ outcomes | MBPP+ outcomes |
|---|---|---|---|
| Base | 1B | [JSONL](answers/base_1b_humaneval_plus.answers.jsonl) | [JSONL](answers/base_1b_mbpp_plus.answers.jsonl) |
| Base | 3B | [JSONL](answers/base_3b_humaneval_plus.answers.jsonl) | [JSONL](answers/base_3b_mbpp_plus.answers.jsonl) |
| SFT | 1B | [JSONL](answers/sft_1b_humaneval_plus.answers.jsonl) | [JSONL](answers/sft_1b_mbpp_plus.answers.jsonl) |
| SFT | 3B | [JSONL](answers/sft_3b_humaneval_plus.answers.jsonl) | [JSONL](answers/sft_3b_mbpp_plus.answers.jsonl) |

The root-level `answers.jsonl` is a copy of `answers/base_1b_humaneval_plus.answers.jsonl`, retained for compatibility with the earlier link.
