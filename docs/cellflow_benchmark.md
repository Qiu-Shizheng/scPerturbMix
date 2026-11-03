# CellFlow comparison in the interferon-response task

The [Kang study](https://doi.org/10.1038/nbt.4042) measures how immune cells from eight donors respond to interferon-beta. Models predict CD14-positive and FCGR3A-positive monocytes in a held-out donor from responses in other donors' B, T and natural killer cells. Untreated target monocytes provide the starting cell states. The common evaluation panel contains 2,000 genes per donor.

We fit the [official CellFlow implementation](https://github.com/theislab/CellFlow), described by [Klein and colleagues](https://doi.org/10.1101/2025.04.11.648220), with capacity selected on training-cell validation. CellFlow learns a flow from untreated to stimulated cells in a 100-dimensional principal-component representation. The conditional network and optimal-transport flow-matching objective follow the official implementation.

Two network widths and three initializations give 48 candidate fits across eight donors. Validation assesses mean-expression error every 2,000 updates, with a maximum of 50,000 updates and early stopping after ten checks without improvement. Each donor's capacity is selected from the mean validation error of its three initializations. The resulting 24 fitted models generate predictions for all eligible target-control cells.

Both outputs are included in the [joint comparison](benchmark_comparison.md#kang-interferon-responses-in-monocytes):

- **CellFlow:** expression decoded from the predicted principal components.
- **CellFlow (control residual restored):** decoded prediction plus the measured untreated expression minus its principal-component reconstruction.

Gene-response metrics score the average predicted condition profile across the three initializations. Cell-distribution metrics are computed for each initialization and then averaged. Each donor has equal weight. The accompanying data include MSE, MAE, response Pearson and Spearman correlations, Hallmark response error and correlation, squared maximum mean discrepancy and energy distance.

[Model metrics](benchmarks/cellflow_model_metrics.tsv) · [Donor metrics](benchmarks/cellflow_donor_metrics.tsv) · [Individual fits](benchmarks/cellflow_per_fit_metrics.tsv) · [Paired donor intervals](benchmarks/cellflow_paired_donor_intervals.tsv) · [Training selection](benchmarks/cellflow_training_selection.tsv)

Distribution sensitivity covers 20 or 50 principal components, three kernel widths and cell samples capped at 64, 128 or 256. The complete grid includes all eight model outputs. Five cell subsamples and three CellFlow initializations are averaged within each donor. Energy distance has six distinct settings because it does not use the kernel width.

[All setting means](benchmarks/distribution_sensitivity_setting_means.tsv) · [Donor results](benchmarks/distribution_sensitivity_donor_results.tsv) · [Cell subsamples](benchmarks/distribution_sensitivity_subsamples.tsv) · [CellFlow paired intervals](benchmarks/cellflow_distribution_sensitivity_intervals.tsv)
