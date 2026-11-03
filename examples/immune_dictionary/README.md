# Real-data example: cytokine responses in mouse immune cells

This example predicts how cytokines change gene expression in six macrophage and dendritic-cell populations. It uses **438 measured population–cytokine conditions**, covering **82 cytokines and 2,000 genes**, from the [Immune Dictionary](https://doi.org/10.1038/s41586-023-06816-9).

The package includes the observed treated profiles and their matched PBS controls as compact, population-level averages. Prediction uses the released model and the PBS profiles. The observed treated profiles are opened for scoring. No additional download or GPU is needed.

## Run

From the repository root:

```bash
python -m pip install -e .
python examples/immune_dictionary/run.py
```

Choose another output directory with `--output`:

```bash
python examples/immune_dictionary/run.py --output runs/my_cytokine_example
```

## Results

The command recomputes the following scores:

| Predictor | Mean squared error ↓ | Mean absolute error ↓ | Response Pearson correlation ↑ |
|---|---:|---:|---:|
| scPerturbMix | 0.01790635 | 0.09629542 | 0.19371331 |
| Training mean | 0.02028949 | 0.10433058 | 0.16987986 |
| Untreated reference | 0.01865026 | 0.09600342 | — |

scPerturbMix lowers mean squared error by **11.7%** relative to the training mean. The untreated reference has the lowest mean absolute error in this comparison. Its predicted effect is zero for every gene, so its response correlation is undefined.

Each score is calculated across genes within a population–cytokine pair and then averaged across all 438 pairs. Correlation compares predicted and observed changes relative to the matched control. These are condition-weighted results. The full research comparison, including the low-rank model and all eight evaluated methods, is available in the [external evaluation guide](../../docs/external_validation.md).

The command writes:

| Output | Contents |
|---|---|
| `predictions.npz` | Newly computed expression predictions, treatment effects, genes and condition labels |
| `summary.json` | Overall scores for the three predictors |
| `summary.tsv` | Overall scores and separate scores for all six populations |
| `condition_metrics.tsv` | Scores for each predictor and all 438 conditions |

The [expected summary](expected_summary.tsv) records the verified output. Small floating-point differences in the final digits are normal across numerical libraries.

## Data and model

The model was fitted to six lymphoid populations: B cells, CD4 and CD8 T cells, gamma-delta T cells, regulatory T cells and natural killer cells. The six evaluated populations are Langerhans cells, macrophages, migratory dendritic cells, CD103-positive and CD209-positive dendritic cells, and plasmacytoid dendritic cells. Their stimulated profiles were held out from fitting. Training and evaluation populations can include cells from the same mice.

Mice received 5 micrograms of cytokine and were profiled four hours later. Expression was normalised across the complete 31,053-gene count matrix, transformed as cell-level log1p counts per 10,000, averaged within each mouse, and then averaged equally across mice. The tutorial retains the 2,000 genes selected using training controls. Each target condition has its own matched PBS profile.

The [provenance record](provenance.json) describes the study, preprocessing, eligibility criteria and population sizes. Original single-cell count matrices are available from the [authors' portal](https://www.immune-dictionary.org/download/) and [GEO GSE202186](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE202186). The example contains derived numerical profiles. Credit: Cui et al., *Nature* **625**, 377–384 (2024), published online in 2023, [CC BY 4.0 article](https://creativecommons.org/licenses/by/4.0/). Original data terms apply.
