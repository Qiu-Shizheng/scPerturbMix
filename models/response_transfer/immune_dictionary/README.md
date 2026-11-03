# Mouse cytokine-response checkpoint

This scPerturbMix checkpoint predicts average gene-expression responses to cytokines in mouse immune-cell populations. Cytokines are proteins that coordinate immune activity. The model is fitted to six lymphoid source populations from the [Immune Dictionary study](https://doi.org/10.1038/s41586-023-06816-9). It uses mouse gene identities and 2,000 response genes.

The catalogue contains **83 cytokine conditions**, each measured **four hours after 5 micrograms per mouse**. This dose is a mass per animal. The checkpoint uses named conditions, without converting the dose to a concentration. Its external evaluation includes **438 population–cytokine pairs covering 82 cytokines** in six held-out macrophage or dendritic-cell populations. One registered cytokine has no eligible target condition under the evaluation's cell and control support criteria. Source and target populations can share mice. Model fitting and selection use the source populations, while untreated target cells provide the prediction reference.

## Files

Keep `model.json` and `model.npz` together in this directory. The JSON file lists the gene identities, registered conditions, physical units and fitted settings. The NumPy archive contains the fitted response arrays. The example CSV files demonstrate prediction inputs, and `verification.json` records checkpoint replay against the evaluated predictions.

## Prepare an untreated control

Use the expression scale recorded in `model.json`:

1. For each cell, sum counts across the full **31,053-gene** author count axis.
2. Divide each gene count by that cell's full-library total, multiply by **10,000**, then apply **log1p**.
3. Extract the **2,000 model genes** after normalisation. Preserve the exact mouse gene identities.
4. Average cells within each mouse, then average the mouse profiles with equal weight. Use the PBS control mice matched to the condition being predicted.

The control CSV contains `gene_id,expression`, with every model gene exactly once in any order. The packaged example contains a PBS reference from the evaluated plasmacytoid dendritic-cell population. For an experiment, supply its matched untreated target profile. The Python interface also accepts a separate control vector for each requested condition.

## Run from the repository root

Install the package using the [repository instructions](../../../README.md), then run:

```bash
scperturbmix-predict \
  --model-dir models/response_transfer/immune_dictionary \
  --control models/response_transfer/immune_dictionary/example_control.csv \
  --conditions models/response_transfer/immune_dictionary/example_conditions.csv \
  --output mouse_cytokine_predictions.npz
```

The condition file needs one column:

```csv
condition_id
41BBL
APRIL
```

Identifiers must match the catalogue exactly, including case. The output archive contains `prediction`, `effect`, `gene_ids` and `condition_id`. Prediction and effect arrays have one row per requested condition and 2,000 columns in model gene order. Predictions are on the supplied expression scale, and effects are changes relative to the supplied untreated reference.

See the [named-condition Python guide](../../../docs/response_transfer.md#named-cytokine-conditions) for matched-control matrices and a complete Python example. The [external evaluation guide](../../../docs/external_validation.md) describes the data, eligible populations, comparison models and results.
