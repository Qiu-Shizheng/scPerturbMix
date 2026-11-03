#!/usr/bin/env python3
"""Predict real cytokine responses and score them against observed profiles."""
import argparse
import csv
import json
from pathlib import Path

import numpy as np
from scperturbmix import predict_conditions

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
POPULATIONS = {
    'Langerhans': 'Langerhans cells', 'Macrophage': 'Macrophages',
    'MigDC': 'Migratory dendritic cells', 'cDC1': 'CD103-positive dendritic cells',
    'cDC2': 'CD209-positive dendritic cells', 'pDC': 'Plasmacytoid dendritic cells'}


def score(observed_effect, predicted_effect):
    difference = predicted_effect - observed_effect
    x = predicted_effect - predicted_effect.mean(axis=1, keepdims=True)
    y = observed_effect - observed_effect.mean(axis=1, keepdims=True)
    denominator = np.sqrt((x * x).sum(axis=1) * (y * y).sum(axis=1))
    correlation = np.full(len(x), np.nan)
    np.divide((x * y).sum(axis=1), denominator, out=correlation, where=denominator > 0)
    return (np.mean(difference ** 2, axis=1), np.mean(abs(difference), axis=1), correlation)


def evaluate(data_path, model_dir, output):
    with np.load(data_path, allow_pickle=False) as data:
        control = data['control']
        observed = data['observed']
        gene_ids = data['gene_ids']
        conditions = data['condition_id']
        populations = data['population']
    if control.shape != observed.shape or control.shape != (len(conditions), len(gene_ids)):
        raise ValueError('Observed and control profiles must share the declared condition and gene axes.')
    if len(populations) != len(conditions) or not np.isfinite(control).all() or not np.isfinite(observed).all():
        raise ValueError('Population labels and finite profiles are required for every condition.')
    prediction, effect, output_genes = predict_conditions(control, gene_ids, conditions, model_dir)
    if not np.array_equal(gene_ids, output_genes):
        raise ValueError('The tutorial gene order must match the released checkpoint.')
    metadata = json.loads((model_dir / 'model.json').read_text())
    index = {row['condition_id']: i for i, row in enumerate(metadata['conditions'])}
    with np.load(model_dir / 'model.npz', allow_pickle=False) as checkpoint:
        training_mean = checkpoint['mean_effect'][[index[str(k)] for k in conditions]]
    effects = {'scPerturbMix': effect, 'Training mean': training_mean,
               'Untreated reference': np.zeros_like(effect)}
    truth = observed - control
    records, summaries = [], []
    for name, estimate in effects.items():
        mse, mae, pearson = score(truth, estimate)
        for i in range(len(conditions)):
            records.append({'model': name, 'population': POPULATIONS.get(str(populations[i]), str(populations[i])),
                            'condition_id': str(conditions[i]), 'mse': float(mse[i]),
                            'mae': float(mae[i]), 'response_pearson': float(pearson[i]) if np.isfinite(pearson[i]) else ''})
        for population in ['All'] + sorted(set(populations.tolist())):
            mask = np.ones(len(conditions), dtype=bool) if population == 'All' else populations == population
            corr = pearson[mask]
            summaries.append({'model': name, 'population': POPULATIONS.get(population, population),
                              'conditions': int(mask.sum()), 'mse': float(mse[mask].mean()),
                              'mae': float(mae[mask].mean()),
                              'response_pearson': float(corr[np.isfinite(corr)].mean()) if np.isfinite(corr).any() else None})
    output.mkdir(parents=True, exist_ok=True)
    for filename, rows in [('condition_metrics.tsv', records), ('summary.tsv', summaries)]:
        with (output / filename).open('w', newline='') as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]), delimiter='\t')
            writer.writeheader()
            writer.writerows(rows)
    np.savez_compressed(output / 'predictions.npz', prediction=prediction, effect=effect,
                        gene_ids=gene_ids, condition_id=conditions, population=populations)
    overall = [row for row in summaries if row['population'] == 'All']
    (output / 'summary.json').write_text(json.dumps(overall, indent=2, allow_nan=False) + '\n')
    return overall


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=HERE / 'observed_profiles.npz')
    parser.add_argument('--model-dir', type=Path, default=REPO / 'models/response_transfer/immune_dictionary')
    parser.add_argument('--output', type=Path, default=REPO / 'runs/immune_dictionary')
    args = parser.parse_args()
    print(json.dumps(evaluate(args.data, args.model_dir, args.output), indent=2, allow_nan=False))


if __name__ == '__main__':
    main()
