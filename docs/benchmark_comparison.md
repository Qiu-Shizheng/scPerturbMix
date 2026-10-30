# Benchmark comparisons

This page brings classical methods, single-cell perturbation models and pretrained-model adaptations into the same table for each prediction task. Each group shares its stated data panel and evaluation setting. Scores from different tasks or normalization schemes are reported separately.

**MSE** measures prediction error, so lower is better. **Response Pearson** measures agreement in the pattern of treatment-induced changes, so higher is better. A dash indicates that correlation is undefined for a constant-response prediction.

[Download the model summary](benchmarks/matched_model_summary.tsv) · [Download all matched metrics](benchmarks/matched_model_metrics.tsv) · [Read the data and task guide](data_and_tasks.md)

## OP3 drug responses in immune cells

The OP3 drug screen profiles donor blood cells exposed to small molecules. Models learn from lymphoid cells and predict myeloid-cell responses across 5,317 genes. The table shows the pooled myeloid target. scGPT and Nicheformer are evaluated with a common response head, including frozen, fine-tuned and randomly initialized encoders.

| Target | Model | MSE ↓ | Response Pearson ↑ |
|---|---|---:|---:|
| Pooled myeloid cells | scPerturbMix | 0.073151 | 0.2517 |
| Pooled myeloid cells | Low-rank response | 0.077050 | 0.1889 |
| Pooled myeloid cells | Nicheformer (frozen encoder) | 0.077321 | 0.1956 |
| Pooled myeloid cells | Nicheformer (fine-tuned encoder) | 0.077371 | 0.1947 |
| Pooled myeloid cells | Nicheformer architecture (random initialization) | 0.077393 | 0.1942 |
| Pooled myeloid cells | Global response scaling | 0.077398 | 0.1932 |
| Pooled myeloid cells | scGPT architecture (random initialization) | 0.077438 | 0.1932 |
| Pooled myeloid cells | scGPT (fine-tuned encoder) | 0.077463 | 0.1927 |
| Pooled myeloid cells | scGPT (frozen encoder) | 0.078524 | 0.1751 |

## Cellarity drug responses in primary cells

The Cellarity DrugReflector screen measures drug responses in cultured and primary human cells. Cultured cell backgrounds provide training data, and four primary cell populations are held out for evaluation across 13,290 genes. These targets include blood progenitors, T cells, airway epithelial cells and preadipocytes.

| Target | Model | MSE ↓ | Response Pearson ↑ |
|---|---|---:|---:|
| CD34+ blood progenitors | scPerturbMix | 0.028721 | 0.2250 |
| CD34+ blood progenitors | Low-rank response | 0.029253 | 0.2055 |
| CD34+ blood progenitors | Global response scaling | 0.029509 | 0.2104 |
| CD8+ T cells | Global response scaling | 0.014803 | 0.2934 |
| CD8+ T cells | scPerturbMix | 0.014821 | 0.2824 |
| CD8+ T cells | Low-rank response | 0.014890 | 0.2555 |
| Bronchial epithelial cells | scPerturbMix | 0.046215 | 0.2198 |
| Bronchial epithelial cells | Low-rank response | 0.047414 | 0.2054 |
| Bronchial epithelial cells | Global response scaling | 0.047771 | 0.2112 |
| Preadipocytes | scPerturbMix | 0.033806 | 0.2219 |
| Preadipocytes | Global response scaling | 0.034585 | 0.2102 |
| Preadipocytes | Low-rank response | 0.034601 | 0.1986 |

## Parse cytokine responses in monocytes

This blood-cell cytokine screen tests how immune-signalling molecules alter gene expression. The matched comparison predicts CD14+ and CD16+ monocyte responses using 12 donors and 2,000 genes per fold. All rows use the capped cell panel. Native generative outputs and control-anchored outputs are listed separately. Control anchoring combines a predicted response with the measured untreated-cell mean.

| Target | Model | MSE ↓ | Response Pearson ↑ |
|---|---|---:|---:|
| CD14+ monocytes | Source-selected replicated reliability | 0.018915 | 0.2441 |
| CD14+ monocytes | Gaussian context kernel | 0.018999 | 0.2373 |
| CD14+ monocytes | scPerturbMix | 0.019294 | 0.2431 |
| CD14+ monocytes | Global response scaling | 0.019302 | 0.2418 |
| CD14+ monocytes | scGen (control-anchored) | 0.020190 | 0.1571 |
| CD14+ monocytes | scVIDR (stable solver, control-anchored) | 0.021742 | 0.1451 |
| CD14+ monocytes | scGen | 0.022112 | 0.3605 |
| CD14+ monocytes | scVIDR (stable solver) | 0.024118 | 0.3495 |
| CD16+ monocytes | Source-selected replicated reliability | 0.023843 | 0.2477 |
| CD16+ monocytes | Gaussian context kernel | 0.023911 | 0.2415 |
| CD16+ monocytes | Global response scaling | 0.024340 | 0.2417 |
| CD16+ monocytes | scPerturbMix | 0.024343 | 0.2428 |
| CD16+ monocytes | scGen (control-anchored) | 0.024836 | 0.1801 |
| CD16+ monocytes | scVIDR (stable solver, control-anchored) | 0.025390 | 0.1771 |
| CD16+ monocytes | scGen | 0.026689 | 0.3490 |
| CD16+ monocytes | scVIDR (stable solver) | 0.027611 | 0.3461 |

## Kang interferon responses in monocytes

This independent study profiles blood cells before and after interferon stimulation. The comparison uses eight donors and 2,000 genes per fold to predict responses in two monocyte populations. The scPerturbMix row uses parameters fixed from the OP3 drug-response analysis.

| Target | Model | MSE ↓ | Response Pearson ↑ |
|---|---|---:|---:|
| CD14+ monocytes | scPerturbMix fixed OP3 parameters | 0.051356 | 0.7888 |
| CD14+ monocytes | scVIDR (stable solver) | 0.053393 | 0.8040 |
| CD14+ monocytes | scVIDR (stable solver, control-anchored) | 0.054583 | 0.8044 |
| CD14+ monocytes | scGen | 0.055909 | 0.8083 |
| CD14+ monocytes | Global response scaling | 0.056342 | 0.7881 |
| CD14+ monocytes | CPA (post-warmup, control-anchored) | 0.079118 | 0.7571 |
| CD14+ monocytes | CPA | 0.082858 | 0.6187 |
| CD14+ monocytes | CPA (control-anchored) | 0.083636 | 0.7323 |
| CD14+ monocytes | CPA (post-warmup) | 0.093255 | 0.5054 |
| FCGR3A+ monocytes | scVIDR (stable solver) | 0.038559 | 0.8091 |
| FCGR3A+ monocytes | scGen | 0.040419 | 0.8088 |
| FCGR3A+ monocytes | scVIDR (stable solver, control-anchored) | 0.041771 | 0.7992 |
| FCGR3A+ monocytes | scPerturbMix fixed OP3 parameters | 0.042364 | 0.7765 |
| FCGR3A+ monocytes | Global response scaling | 0.044873 | 0.7773 |
| FCGR3A+ monocytes | CPA (post-warmup, control-anchored) | 0.063314 | 0.7644 |
| FCGR3A+ monocytes | CPA (control-anchored) | 0.064070 | 0.7395 |
| FCGR3A+ monocytes | CPA | 0.068149 | 0.5869 |
| FCGR3A+ monocytes | CPA (post-warmup) | 0.077975 | 0.5042 |

CPA uses its official model with source-cell validation. The post-warmup rows select checkpoints after the adversarial objective reaches its full weight. Each CPA setting uses eight donor folds and three initializations. Mean-response predictions are averaged over initializations before scoring. Models use their respective training schedules.

[Complete Kang metrics](benchmarks/kang_model_metrics.tsv), including Spearman correlation and cell-distribution distances, and [CPA training and evaluation details](cpa_benchmark.md) accompany this comparison.

## Wood blood-cell responses with pretrained Stack

The independent Wood blood-cell study provides two experimental batches for a pretrained Stack comparison. Models predict held-out responses without treated target cells. The benchmark uses a shared 14,748-gene vocabulary and count denominator. These rows form their own comparison group.

| Target | Model | MSE ↓ | Response Pearson ↑ |
|---|---|---:|---:|
| Batch A | Stack-Large-Aligned (control-anchored) | 0.089598 | 0.5128 |
| Batch A | Stack-Large-Aligned | 0.098221 | 0.5605 |
| Batch A | Calibrated mean response | 0.113308 | 0.2944 |
| Batch A | Gaussian context kernel | 0.113805 | 0.2946 |
| Batch A | Linear context kernel | 0.119680 | 0.2747 |
| Batch B | Linear context kernel | 0.051891 | 0.1867 |
| Batch B | Stack-Large-Aligned (control-anchored) | 0.052368 | 0.2510 |
| Batch B | Gaussian context kernel | 0.052708 | 0.1785 |
| Batch B | Calibrated mean response | 0.052771 | 0.1734 |
| Batch B | Stack-Large-Aligned | 0.101268 | 0.3743 |

## sci-Plex3 drug-dose interpolation

sci-Plex3 measures how cancer cell lines respond to drugs at different concentrations. The task predicts 54 held-out interior-dose conditions across 512 genes. GPerturb and State use their official architectures with dose-task adaptations. State is trained from scratch. Each neural dose model uses one initialization and the documented finite training budget.

| Target | Model | MSE ↓ | Response Pearson ↑ |
|---|---|---:|---:|
| All held-out dose conditions | scPerturbMix dose model | 0.007270 | 0.5525 |
| All held-out dose conditions | Low-rank dose interpolation | 0.007375 | 0.5532 |
| All held-out dose conditions | Scaled log-dose interpolation | 0.007451 | 0.5577 |
| All held-out dose conditions | Shrunken dose interpolation | 0.007637 | 0.5558 |
| All held-out dose conditions | Log-dose interpolation | 0.008428 | 0.5577 |
| All held-out dose conditions | GPerturb (dose adaptation) | 0.010380 | 0.3624 |
| All held-out dose conditions | State (dose adaptation, from scratch) | 0.011691 | 0.5398 |

## sci-Plex2 dense drug-dose interpolation

sci-Plex2 samples drug responses over a dense concentration series. The task predicts expression changes at held-out interior doses across 32,418 genes, comparing log-dose interpolation with structured dose-response models.

| Target | Model | MSE ↓ | Response Pearson ↑ |
|---|---|---:|---:|
| All held-out conditions | Selected hybrid dose response | 0.091080 | 0.7533 |
| All held-out conditions | Scaled log-dose response | 0.091180 | 0.7421 |
| All held-out conditions | Variance-weighted low-rank dose response | 0.091180 | 0.7421 |
| All held-out conditions | Log-dose response | 0.093655 | 0.7411 |

## PerturbFate genetic responses across drug environments

PerturbFate combines genetic interventions with different drug environments. The task predicts genetic responses after a change in drug exposure, using measured genetic responses under the vehicle condition as inputs. Evaluation covers 26,357 genes.

| Target | Model | MSE ↓ | Response Pearson ↑ |
|---|---|---:|---:|
| All held-out conditions | Reduced-rank response | 0.280323 | 0.2900 |
| All held-out conditions | scPerturbMix conditional genetic model | 0.280323 | 0.2900 |
| All held-out conditions | Matched PCA-ridge | 0.280388 | 0.2895 |
| All held-out conditions | Drug-environment control | 0.304503 | — |
| All held-out conditions | Additive response | 0.530139 | 0.0073 |

## Glioblastoma expression prediction

This development analysis predicts expression in drug-treated glioblastoma cells, a brain tumour system, across 512 genes. Pretrained gene embeddings are combined with ridge-response heads and compared with a random-embedding control.

| Target | Model | MSE ↓ | Response Pearson ↑ |
|---|---|---:|---:|
| All held-out conditions | scPerturbMix expression model | 0.056403 | 0.3854 |
| All held-out conditions | Nicheformer gene embeddings with ridge | 0.057326 | 0.3744 |
| All held-out conditions | scGPT gene embeddings with ridge | 0.057399 | 0.3722 |
| All held-out conditions | Random gene embeddings with ridge | 0.057481 | 0.3710 |
| All held-out conditions | Ridge response model | 0.060537 | 0.0853 |

## Glioblastoma paired drug-response prediction

Using the same brain-tumour system, this task evaluates paired drug-induced changes rather than full expression profiles. The 512-gene comparison focuses on the response to treatment.

| Target | Model | MSE ↓ | Response Pearson ↑ |
|---|---|---:|---:|
| All held-out conditions | Nicheformer gene embeddings with ridge | 0.105065 | 0.0511 |
| All held-out conditions | Random gene embeddings with ridge | 0.105082 | 0.0504 |
| All held-out conditions | scGPT gene embeddings with ridge | 0.105082 | 0.0503 |
| All held-out conditions | Ridge expression model | 0.105091 | 0.0440 |
| All held-out conditions | scPerturbMix expression model | 0.105335 | 0.0406 |

## Metrics and model settings

The full metrics table includes additional measures where available: mean absolute error, Spearman correlation, pathway-response error, top-response-gene overlap, direction agreement and cell-distribution distances. Missing entries indicate that a metric was not included in that evaluation.

Control-anchored and native predictions are distinct model outputs. Pretrained encoder and embedding adaptations evaluate the stated representation and response head. Dose, cell-context and conditional genetic tasks use task-specific fits. The benchmark tables retain the aggregation defined by each task protocol.
