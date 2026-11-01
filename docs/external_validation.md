# External cytokine-response evaluation

The [Immune Dictionary study](https://doi.org/10.1038/s41586-023-06816-9) measures how cytokines change gene activity in mouse lymph nodes. Cytokines are proteins that coordinate immune-cell behaviour. Mice received individual cytokines, and lymph-node cells were profiled four hours later.

## Data and prediction task

The author-provided population analysis objects contain 117,282 cells. Six lymphoid populations contribute 70,991 source cells. The fixed model-fitting rule is refitted to these mouse source responses. Target stimulated profiles are withheld during feature selection, fitting and model selection. Untreated target cells provide the prediction reference. Source and target populations can come from the same mouse.

The six source populations share 83 eligible cytokines. The test set contains 438 population–cytokine pairs covering 82 cytokines in six macrophage or dendritic-cell populations. Monocytes and neutrophils did not meet the fixed cell and matched-control support criteria.

| Population | Role | Input cells | Eligible cytokines |
| --- | --- | --- | --- |
| B cells | Source | 16892 | 83 |
| CD4 T cells | Source | 10000 | 83 |
| CD8 T cells | Source | 10000 | 83 |
| γδ T cells | Source | 10320 | 83 |
| Regulatory T cells | Source | 10000 | 83 |
| Natural killer cells | Source | 13779 | 83 |
| Monocytes | Target | 2591 | 0 |
| Macrophages | Target | 3261 | 31 |
| CD103-positive dendritic cells | Target | 7416 | 82 |
| cDC2/CD209-positive dendritic cells | Target | 7244 | 82 |
| Migratory dendritic cells | Target | 8852 | 81 |
| Langerhans cells | Target | 7648 | 82 |
| Plasmacytoid dendritic cells | Target | 8112 | 80 |
| Neutrophils | Target | 1167 | 0 |

The released objects are population analysis subsets, including refined dendritic-cell annotations. They are distinct from the original atlas total. Each eligible condition requires at least two treated mice, two matched PBS control mice and 20 cells in each condition. Individual mouse–population profiles require at least five cells. Controls are matched using shared experimental channels, and technical channels from the same mouse are combined. Expression is normalised across the full gene axis before selecting 2,000 variable genes from source control cells.

## Results

Condition-weighted metrics give each of the 438 test pairs equal weight. Equal-target MSE first averages within each target population and then gives the six populations equal weight.

| Model | Condition-weighted MSE | Condition-weighted MAE | Response Pearson | Response Spearman | Equal-target MSE |
| --- | --- | --- | --- | --- | --- |
| Untreated reference | 0.018650 | 0.096003 | — | — | 0.022109 |
| Source mean | 0.020289 | 0.104331 | 0.1699 | 0.1005 | 0.023643 |
| Global scaling | 0.017931 | 0.096809 | 0.1699 | 0.1005 | 0.021284 |
| Condition gate | 0.018042 | 0.096668 | 0.1699 | 0.1005 | 0.021381 |
| Gene gate | 0.017987 | 0.096431 | 0.1766 | 0.1001 | 0.021327 |
| Low rank | 0.017855 | 0.096395 | 0.1810 | 0.1009 | 0.021195 |
| scPerturbMix | 0.017906 | 0.096295 | 0.1937 | 0.1086 | 0.021249 |
| Cross-source basis | 0.017916 | 0.096284 | 0.1902 | 0.1071 | 0.021264 |

scPerturbMix reduces condition-weighted MSE by 11.7% relative to the source-mean predictor and 4.0% relative to the untreated reference. The corresponding 95% cytokine-block intervals are 10.4–13.1% and 2.5–5.7%. The low-rank predictor has a similar MSE, while scPerturbMix has the highest mean response Pearson correlation among these eight models. All target populations and models are retained in the [unified comparison](benchmark_comparison.md#immune-dictionary-in-vivo-cytokine-responses).

The published immune-response signatures provide an additional biological endpoint. Across 27 conditions with directly matching population labels and at least ten signature genes, scPerturbMix recovers 77.9% of published response directions on average. These signatures come from the same original study. A separate set of 87 conditions with parent-population or refined-subset correspondence is recorded as exploratory. Each condition is evaluated by all eight models.

Paired intervals resample cytokines while retaining all target populations within each sampled cytokine. The condition-weighted interval divides total paired differences by the number of sampled condition pairs. It describes variation across cytokines conditional on the measured mouse profiles and reused control animals.

[Population coverage](benchmarks/immune_dictionary_population_coverage.tsv), [overall scores](benchmarks/immune_dictionary_overall_metrics.tsv), [target scores](benchmarks/immune_dictionary_target_metrics.tsv), [all condition scores](benchmarks/immune_dictionary_condition_metrics.tsv), [published-signature scores](benchmarks/immune_dictionary_signature_metrics.tsv) and [condition-weighted intervals](benchmarks/immune_dictionary_condition_equal_intervals.tsv) accompany the evaluation.

Obtain the experimental data from the [authors' download portal](https://www.immune-dictionary.org/download/) or [GEO GSE202186](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE202186). The repository distributes evaluation summaries, not the original expression matrices.
