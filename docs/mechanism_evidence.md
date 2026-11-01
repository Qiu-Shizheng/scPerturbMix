# Mechanism and component comparisons

scPerturbMix combines gene-level reliability with response programmes learned from source data. A programme describes a coordinated direction of gene-expression change. Component comparisons examine which parts contribute to prediction.

## Removing individual components

Each structural ablation repeats source-context selection for its remaining parameters. In the immune-cell drug screen, the full model reduces MSE by 1.52% relative to removing gene weighting, 1.67% relative to removing the programme branch, and 0.85% relative to removing programme weighting. Effects vary across populations.

The percentage reduction uses the ablated model's MSE as its denominator. The interval concerns the absolute paired MSE difference, ablated minus full model. Positive differences favour the full model. Resampling keeps concentrations of each compound together.

| Target | Removed component | Full MSE | Ablated MSE | MSE reduction (%) | 95% interval for MSE difference |
| --- | --- | --- | --- | --- | --- |
| Immune drug screen | Gene weighting | 0.073151 | 0.074277 | 1.52 | 0.000743 to 0.001559 |
| Immune drug screen | Programme branch | 0.073151 | 0.074393 | 1.67 | 0.000332 to 0.002199 |
| Immune drug screen | Programme weighting | 0.073151 | 0.073781 | 0.85 | 0.000063 to 0.001175 |
| Immune drug screen | Mixture selection | 0.073151 | 0.073151 | 0.00 | 0.000000 to 0.000000 |
| Immune drug screen | Amplitude scaling | 0.073151 | 0.072963 | -0.26 | -0.000452 to 0.000062 |
| Blood progenitors | Gene weighting | 0.028721 | 0.028813 | 0.32 | 0.000011 to 0.000168 |
| Blood progenitors | Programme branch | 0.028721 | 0.029001 | 0.97 | 0.000026 to 0.000550 |
| Blood progenitors | Programme weighting | 0.028721 | 0.028846 | 0.43 | -0.000081 to 0.000352 |
| Blood progenitors | Mixture selection | 0.028721 | 0.028721 | 0.00 | 0.000000 to 0.000000 |
| Blood progenitors | Amplitude scaling | 0.028721 | 0.028740 | 0.06 | -0.000072 to 0.000098 |
| CD8 T cells | Gene weighting | 0.014821 | 0.014663 | -1.08 | -0.000260 to -0.000057 |
| CD8 T cells | Programme branch | 0.014821 | 0.015056 | 1.56 | -0.000100 to 0.000737 |
| CD8 T cells | Programme weighting | 0.014821 | 0.014853 | 0.21 | -0.000150 to 0.000270 |
| CD8 T cells | Mixture selection | 0.014821 | 0.014821 | 0.00 | 0.000000 to 0.000000 |
| CD8 T cells | Amplitude scaling | 0.014821 | 0.014716 | -0.72 | -0.000273 to 0.000075 |
| Airway epithelial cells | Gene weighting | 0.046215 | 0.046344 | 0.28 | -0.000074 to 0.000310 |
| Airway epithelial cells | Programme branch | 0.046215 | 0.046391 | 0.38 | -0.000268 to 0.000669 |
| Airway epithelial cells | Programme weighting | 0.046215 | 0.046687 | 1.01 | 0.000106 to 0.000917 |
| Airway epithelial cells | Mixture selection | 0.046215 | 0.046215 | 0.00 | 0.000000 to 0.000000 |
| Airway epithelial cells | Amplitude scaling | 0.046215 | 0.046198 | -0.04 | -0.000116 to 0.000084 |
| Adipocyte precursors | Gene weighting | 0.033806 | 0.033829 | 0.07 | -0.000048 to 0.000097 |
| Adipocyte precursors | Programme branch | 0.033806 | 0.034104 | 0.87 | -0.000087 to 0.000688 |
| Adipocyte precursors | Programme weighting | 0.033806 | 0.034020 | 0.63 | 0.000020 to 0.000427 |
| Adipocyte precursors | Mixture selection | 0.033806 | 0.033806 | 0.00 | 0.000000 to 0.000000 |
| Adipocyte precursors | Amplitude scaling | 0.033806 | 0.033772 | -0.10 | -0.000121 to 0.000061 |

Five binary component choices give 32 logical settings and 20 distinct estimator structures after structural equivalences. Fixed-parameter removals provide a second diagnostic. Random subspaces and rotations within the learned subspace test the learned representation and its coordinate-specific weights. These comparisons use previously evaluated OP3 and Cellarity cohorts.

## Programme directions reproducible across sources

A prespecified alternative learns directions from cross-source response agreement. It retains positive eigenvectors of a symmetric cross-source second-moment matrix and selects the rank using source validation. This is related to cross-validated principal component analysis. The other fitting grids remain the same.

| Target | Original basis MSE | Cross-context basis MSE |
| --- | --- | --- |
| Immune drug screen | 0.073151 | 0.072930 |
| Blood progenitors | 0.028721 | 0.028661 |
| CD8 T cells | 0.014821 | 0.015003 |
| Airway epithelial cells | 0.046215 | 0.046114 |
| Adipocyte precursors | 0.033806 | 0.034038 |

The alternative improves some target populations and worsens others. It is reported as an experimental basis variant. The released core checkpoints retain their original programme basis.

[Component data](benchmarks/component_contributions.tsv), [classical estimators](benchmarks/classical_comparators.tsv), and [cross-context basis data](benchmarks/cross_context_basis.tsv) provide complete tabular results. [Unified comparisons](benchmark_comparison.md) place the classical estimators and pretrained adaptations together within their matched tasks.
