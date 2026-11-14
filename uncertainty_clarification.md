# Corrected confidence intervals and per-task outcomes

We corrected an error in the confidence-interval computation. The pass@1 point estimates are unchanged. The corrected intervals below supersede the previously reported HE+ and MBPP+ intervals; all eight remain above zero.

Each cell reports the SyntaxBPE-minus-GPT-5-style pass@1 difference in percentage points, followed by its pointwise 95% paired hierarchical-bootstrap confidence interval.

| Stage | Size | HE+ | MBPP+ |
|---|---|---|---|
| Base | 1B | +3.5 [+0.8, +6.3] | +1.7 [+0.2, +3.3] |
| Base | 3B | +1.5 [+0.2, +2.7] | +1.6 [+0.2, +3.0] |
| SFT | 1B | +2.3 [+0.2, +4.3] | +3.0 [+0.3, +5.9] |
| SFT | 3B | +1.6 [+0.2, +3.2] | +2.2 [+0.1, +4.3] |

## Per-task outcomes

The files contain both models' generated completions and pass/fail outcomes. HE+ contains 164 tasks and MBPP+ contains 378 tasks, with 10 completions per model per task. The `group`, `task_id`, and `sample_idx` fields identify each record.

| Stage | Size | HE+ outcomes | MBPP+ outcomes |
|---|---|---|---|
| Base | 1B | [JSONL](answers/base_1b_humaneval_plus.answers.jsonl) | [JSONL](answers/base_1b_mbpp_plus.answers.jsonl) |
| Base | 3B | [JSONL](answers/base_3b_humaneval_plus.answers.jsonl) | [JSONL](answers/base_3b_mbpp_plus.answers.jsonl) |
| SFT | 1B | [JSONL](answers/sft_1b_humaneval_plus.answers.jsonl) | [JSONL](answers/sft_1b_mbpp_plus.answers.jsonl) |
| SFT | 3B | [JSONL](answers/sft_3b_humaneval_plus.answers.jsonl) | [JSONL](answers/sft_3b_mbpp_plus.answers.jsonl) |

The root-level `answers.jsonl` is a copy of `answers/base_1b_humaneval_plus.answers.jsonl`, retained for compatibility with the earlier link.
