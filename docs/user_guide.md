# User guide

scPerturbMix predicts gene-expression responses to perturbations. Start with the real-data example, then use a released checkpoint or fit a model to your own response profiles.

## Install

```bash
git clone https://github.com/Qiu-Shizheng/scPerturbMix.git
cd scPerturbMix
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

Python 3.9 or newer and NumPy are sufficient for prediction. Programme-model fitting additionally uses SciPy: `python -m pip install -e '.[programs]'`.

## Reproduce results with real data

```bash
python examples/immune_dictionary/run.py
```

The included mouse immune-cell profiles cover 438 population–cytokine conditions. The command generates predictions, overall and population-specific scores, and a table for every condition in `runs/immune_dictionary/`. Expected MSE is 0.01790635 and mean response Pearson correlation is 0.19371331. The [complete tutorial](../examples/immune_dictionary/README.md) gives the data citation, preparation, comparison results and output formats.

## Predict your own experiment

Choose a checkpoint from the [model catalogue](../README.md#predict-with-a-fitted-model). Match its species, gene panel, expression transformation and treatment conditions.

Create a CSV with one untreated mean-expression value per model gene:

```csv
gene_id,expression
```

Create a condition CSV using the checkpoint's `example_conditions.csv`. Drug models use `condition_id,drug,dose_uM,time_hours`. The mouse cytokine model uses `condition_id`.

```bash
scperturbmix-predict \
  --model-dir models/response_transfer/immune_dictionary \
  --control my_control.csv \
  --conditions my_conditions.csv \
  --output my_predictions.npz
```

The output includes predicted expression, change relative to the control, gene identities and condition identities. For condition-specific controls, use the Python `predict_conditions` interface illustrated in the [model guide](response_transfer.md#named-cytokine-conditions).

## Fit a response model

Prepare a NumPy archive with `effects` shaped as training contexts × shared conditions × genes and the required condition metadata. A context can be a cell type, donor or experimental background. Each effect is the treated mean expression minus its matched untreated mean. At least three training contexts are needed.

```bash
scperturbmix-fit \
  --source-effects my_training_responses.npz \
  --input-scale "describe your expression transformation" \
  --search programs \
  --output models/my_model
```

See the [training format and API](response_transfer.md) for the complete array contract and selection procedure. Keep evaluation responses separate from the training archive.

## Further guides

- [Datasets and biological tasks](data_and_tasks.md)
- [Task support and available interfaces](task_support.md)
- [Complete matched benchmark comparisons](benchmark_comparison.md)
- [H5AD reference runner and optional neural modules](reference_implementation.md)

## Troubleshooting

**Gene mismatch:** use the checkpoint's complete gene set and compatible expression scale. The CSV rows may be reordered, but gene identifiers must be unique.

**Unknown condition:** choose a registered condition from `model.json`, or fit a model containing the required treatments.

**Different numerical results:** check normalisation, gene order and control matching. For the included tutorial, compare with `examples/immune_dictionary/expected_summary.tsv`.
