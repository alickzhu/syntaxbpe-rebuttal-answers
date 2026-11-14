"""Recompute pointwise 95% paired hierarchical-bootstrap intervals.

Run with Python 3: python recompute_intervals.py
Uses only the standard library. Binary pass/fail labels are read as supplied;
this script does not re-execute generated code or verify those labels.
"""
import collections
import json
import random
from pathlib import Path

REPLICATES = 5000
SEED = 42
ROOT = Path(__file__).resolve().parent


def percentile(values, probability):
    values = sorted(values)
    position = (len(values) - 1) * probability
    lower = int(position)
    upper = min(lower + 1, len(values) - 1)
    return values[lower] + (position - lower) * (values[upper] - values[lower])


def evaluate(path):
    cells = collections.defaultdict(lambda: collections.defaultdict(dict))
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        assert isinstance(row['passed'], bool)
        cell = cells[row['group']][row['task_id']]
        assert row['sample_idx'] not in cell, 'Duplicate sample index'
        cell[row['sample_idx']] = row['passed']
    assert set(cells) == {'GPT5-style', 'SyntaxBPE'}
    tasks = sorted(cells['SyntaxBPE'])
    assert set(tasks) == set(cells['GPT5-style'])
    expected_tasks = 164 if 'humaneval_plus' in path.name else 378
    assert len(tasks) == expected_tasks
    arrays = {}
    for group in cells:
        arrays[group] = []
        for task in tasks:
            assert set(cells[group][task]) == set(range(10))
            arrays[group].append([cells[group][task][i] for i in range(10)])
    ours, baseline = arrays['SyntaxBPE'], arrays['GPT5-style']
    denominator = len(tasks) * 10
    ours_score = sum(map(sum, ours)) / denominator * 100
    baseline_score = sum(map(sum, baseline)) / denominator * 100
    rng = random.Random(SEED)
    differences = []
    for _ in range(REPLICATES):
        # Pair only the task resample; independently resample completions.
        task_indices = rng.choices(range(len(tasks)), k=len(tasks))
        delta = 0
        for i in task_indices:
            delta += sum(rng.choices(ours[i], k=10))
            delta -= sum(rng.choices(baseline[i], k=10))
        differences.append(delta / denominator * 100)
    return {
        'file': path.name,
        'tasks': len(tasks),
        'syntaxbpe_pass_at_1': ours_score,
        'gpt5_style_pass_at_1': baseline_score,
        'difference_pp': ours_score - baseline_score,
        'ci_lower_pp': percentile(differences, 0.025),
        'ci_upper_pp': percentile(differences, 0.975),
        'replicates': REPLICATES,
        'seed': SEED,
    }


if __name__ == '__main__':
    for path in sorted((ROOT / 'answers').glob('*.jsonl')):
        print(json.dumps(evaluate(path)), flush=True)
