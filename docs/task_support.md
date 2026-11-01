# Tasks and prediction interfaces

scPerturbMix models molecular responses to chemical, immune and genetic interventions. Its research framework uses components suited to each type of experiment.

| Task | Biological question | Model component |
|---|---|---|
| Drug response | How does a drug change expression in a cell population? | Gene and programme response weighting |
| Immune stimulation | How do immune cells respond to a cytokine or other stimulus? | Response weighting and untreated-state regression |
| Dose response | How does expression change at an unmeasured concentration? | Dose interpolation and shared/context-dependent response components |
| Conditional genetic response | How does a genetic intervention act under drug exposure? | A fitted map from measured vehicle responses to drug-context responses |
| Pilot-assisted prediction | What can a few measured stimuli reveal about additional responses? | Residual calibration using response covariance |

Each task has its own training data, model fit and evaluation conditions. A fitted model can predict multiple supported conditions in one call. The current framework uses separate fits across tasks; it does not share one jointly trained parameter set across all five tasks.

## Released interfaces

`scperturbmix-fit` trains gene-level or gene-and-programme response models from matched response arrays. `scperturbmix-predict` uses a fitted checkpoint, untreated expression and a batch of supported conditions. The checkpoint fixes the gene panel, expression scale and available perturbation conditions.

The repository includes six fitted drug-response, cytokine-response or expression checkpoints. The [model guide](response_transfer.md) describes fitting and prediction, and the [dataset guide](data_and_tasks.md) describes the broader research experiments. Dose, conditional genetic-response and pilot-calibration results are documented in the [benchmark guide](benchmark_evidence.md).

## Named cytokine conditions

The mouse Immune Dictionary checkpoint accepts registered cytokine identifiers through `predict_conditions`. Its catalogue records a fixed dose of 5 micrograms per mouse and a four-hour exposure. The [named-condition guide](response_transfer.md#named-cytokine-conditions) describes input normalisation and matched untreated target controls. Drug checkpoints continue to use `predict_response` with doses in micromolar.

## Python

```python
from scperturbmix import predict_response, predict_conditions, fit_from_arrays
```

The `prado_dt` implementation package and `contextdose-fit` / `contextdose-predict` commands remain available for existing integrations. New applications can use the `scperturbmix` import and command names above.
