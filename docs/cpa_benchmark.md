# CPA on the Kang interferon-response task

[CPA](https://github.com/theislab/cpa) is a single-cell perturbation model that separates cell state from treatment and other experimental factors. This benchmark evaluates its official architecture on the [Kang interferon-beta study](https://doi.org/10.1038/nbt.4042), which profiles blood immune cells from eight donors before and after immune stimulation. CD14-positive and FCGR3A-positive monocytes are the two evaluated immune-cell populations.

CPA appears with scGen, scVIDR and classical methods in the [unified task comparison](benchmark_comparison.md#kang-interferon-responses-in-monocytes). These are results for the interferon task. The fitted drug-response checkpoints distributed with scPerturbMix are listed in the [model guide](response_transfer.md).

## Software and result files

This release provides runnable scPerturbMix prediction and fitting tools, five fitted drug-response or expression checkpoints, and the CPA benchmark tables described below. The CPA component is a result-table release with a task specification. Reproducing those tables requires separate study-specific training and scoring scripts around the official CPA package and the original Kang data.

For CPA installation, follow the [official repository instructions](https://github.com/theislab/cpa). This evaluation uses CPA-tools 0.8.8. Its training runtime adapts the older Lightning epoch-end interface while retaining CPA's model, losses and optimization updates. The source-cell split, gene panels, preprocessing, checkpoint-selection rules and scoring aggregation must follow the specification below to reproduce the comparison.

## Data and prediction task

Each fold predicts interferon responses in the two monocyte populations from one held-out donor. B cells, CD4 T cells, CD8 T cells and natural killer cells from the other seven donors provide training data. Untreated monocytes from the held-out donor provide the query cells. Treated target monocytes are used for evaluation.

The comparison uses the fixed 2,000-gene panel selected from source controls in each fold. Expression is log1p counts per 10,000, with library sizes calculated before gene selection. All compared methods receive the permitted untreated controls and are scored on the same gene panel. Each CPA setting is fitted with three random initializations across all eight donors.

## Model and training selection

CPA uses its official encoder, decoder, perturbation embeddings and adversarial objectives with a Gaussian expression likelihood. The model has 64 latent coordinates, two 128-unit encoder layers and two 512-unit decoder layers. Training uses batches of 512 cells and the Adam optimizer with an initial learning rate of 0.0003. Ten per cent of source cells form the validation set. Target treated cells do not enter model fitting or selection.

The **CPA** rows select the checkpoint and adversarial regularization setting using the official source-validation CPA metric. The candidate adversarial-loss and gradient-penalty coefficients are 20 and 5, or 1 and 1. Training lasts 80–400 epochs, with validation every five epochs and early stopping after five non-improving validation checks. The source-validation metric combines mean-expression R-squared, one-half of variance R-squared and an exponential contrast between treatment and covariate separability in perturbed and basal representations. The regularization coefficients do not directly enter this selection metric.

The **CPA (post-warmup)** rows use coefficients of 1 and 1 and select checkpoints only after the adversarial objective reaches its full weight. Training lasts at least 105 epochs and at most 400 epochs. Early-stopping checks begin after the warmup phase. Checkpoint selection uses the same source-validation metric. Both selection rules were specified before target scoring.

The source-selected checkpoints occur at epochs 15–30, before adversarial training begins. The post-warmup checkpoints occur at epochs 85–125. The [selection table](benchmarks/kang_cpa_source_selection.tsv) gives the selected epoch and training duration for every donor and initialization. The two regularization candidates and the post-warmup schedule comprise 72 training fits of one model family. Other model families use their respective training schedules.

## Outputs and metrics

**Native predictions** are the expression profiles decoded by CPA after switching untreated query cells to the interferon condition. **Control-anchored predictions** add the model's predicted treated-minus-untreated change to the measured untreated cell. Both outputs use the same fitted model.

Mean-response metrics average the three initialization-specific predicted profiles before scoring each donor. Model-level scores then weight the eight donors equally. Cell-distribution metrics are calculated for each fit and then averaged across initializations, using the same source-derived projection, kernel bandwidth and cell samples as the other native models.

| Metric | Meaning | Preferred direction |
|---|---|---|
| MSE | Mean squared expression error | Lower |
| MAE | Mean absolute expression error | Lower |
| Response Pearson | Agreement in the magnitude and pattern of treatment-induced changes | Higher |
| Response Spearman | Agreement in gene rankings of treatment-induced changes | Higher |
| Hallmark MSE and Pearson | Error and agreement for coordinated responses in curated gene sets | Lower MSE, higher Pearson |
| Squared MMD and energy distance | Differences between predicted and observed cell distributions | Lower |

Paired uncertainty intervals resample the eight donors 5,000 times. Each comparison preserves the matched donor pairs. Donor folds share source training donors.

## Downloadable results

- [Complete Kang model comparison](benchmarks/kang_model_metrics.tsv): 34 population–model rows, including classical methods, component analyses and native perturbation models.
- [CPA model summary](benchmarks/kang_cpa_model_metrics.tsv): all eight population–output rows for the two checkpoint-selection rules.
- [CPA donor scores](benchmarks/kang_cpa_donor_metrics.tsv): 64 matched donor-level rows.
- [CPA initialization scores](benchmarks/kang_cpa_fit_metrics.tsv): scores from all selected individual fits, in both output conventions.
- [Paired donor intervals](benchmarks/kang_cpa_paired_intervals.tsv): differences between scPerturbMix and each CPA output, across eight metrics.
- [Source-validation selections](benchmarks/kang_cpa_source_selection.tsv): 48 selected donor–initialization checkpoints across the two reported selection rules.

The [CPA paper](https://doi.org/10.15252/msb.202211517) describes the original method. The evaluation uses CPA-tools 0.8.8. The public benchmark tables contain aggregate results and no raw donor expression matrices.
