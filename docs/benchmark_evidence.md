# Matched benchmark evidence

The OP3 screen measures how drugs change gene expression in human blood immune cells. B cells, T cells and natural killer cells provide source responses. Models predict myeloid responses on the same 5,317-gene panel. Donor rows are strata of this cell-population benchmark. Joint donor and cell-population holdouts are described separately in the detailed evidence.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| scPerturbMix | 127 | 0.073151 | 0.174055 | 0.2517 | 0.1791 |
| Gene reliability | 127 | 0.074393 | 0.175274 | 0.2251 | 0.1566 |
| Shared-response gene shrinkage | 127 | 0.074744 | 0.175725 | 0.2378 | 0.1676 |
| Gene-specific variance shrinkage | 127 | 0.074778 | 0.175337 | 0.2308 | 0.1609 |
| Shared-response positive-part shrinkage | 127 | 0.074928 | 0.175923 | 0.2332 | 0.1665 |
| Positive-part gene shrinkage | 127 | 0.075124 | 0.176030 | 0.2236 | 0.1619 |
| Pooled Stein-form shrinkage | 127 | 0.075726 | 0.176881 | 0.1971 | 0.1522 |
| Perturbation reliability | 127 | 0.075823 | 0.177192 | 0.1932 | 0.1497 |
| Unit-penalty pooled Stein-form shrinkage | 127 | 0.075908 | 0.177189 | 0.1971 | 0.1522 |
| Shared-response pooled Stein-form shrinkage | 127 | 0.076011 | 0.178552 | 0.2038 | 0.1482 |
| Shared-response compound shrinkage | 127 | 0.076148 | 0.178156 | 0.2062 | 0.1526 |
| Separate shared-response and intervention amplitudes | 127 | 0.076990 | 0.178443 | 0.2028 | 0.1517 |
| Low-rank response | 127 | 0.077050 | 0.177662 | 0.1889 | 0.1347 |
| Nicheformer (frozen encoder) | 127 | 0.077321 | 0.177933 | 0.1956 | 0.1515 |
| Geneformer V2 (frozen encoder) | 127 | 0.077334 | 0.178066 | 0.1946 | 0.1512 |
| Nicheformer (fine-tuned encoder) | 127 | 0.077371 | 0.177978 | 0.1947 | 0.1506 |
| Nicheformer architecture (random initialization) | 127 | 0.077393 | 0.178036 | 0.1942 | 0.1503 |
| Global response scaling | 127 | 0.077398 | 0.178215 | 0.1932 | 0.1497 |
| scGPT architecture (random initialization) | 127 | 0.077438 | 0.178107 | 0.1932 | 0.1493 |
| Geneformer V1 architecture (random initialization) | 127 | 0.077444 | 0.178130 | 0.1931 | 0.1496 |
| Geneformer V2 architecture (frozen random encoder) | 127 | 0.077453 | 0.178144 | 0.1929 | 0.1495 |
| scGPT (fine-tuned encoder) | 127 | 0.077463 | 0.178197 | 0.1927 | 0.1503 |
| scGPT (frozen encoder) | 127 | 0.078524 | 0.180188 | 0.1751 | 0.1382 |
| Geneformer V1 (fine-tuned encoder) | 127 | 0.082551 | 0.186883 | 0.1346 | 0.1112 |
| Geneformer V1 (frozen encoder) | 127 | 0.082615 | 0.187306 | 0.1376 | 0.1116 |
| Shared source response | 127 | 0.083638 | 0.186032 | 0.1307 | 0.0989 |
| Unit-penalty positive-part gene shrinkage | 127 | 0.083852 | 0.191677 | 0.2236 | 0.1619 |
| Mean source response | 127 | 0.112929 | 0.232823 | 0.1932 | 0.1497 |

## Encoder comparison

Complete pretrained encoders process untreated control pseudobulk profiles. A common response head combines the context representation, compound identity and a shared-source-response term. These experiments evaluate encoder adaptations for response prediction.

| Encoder | Transformer layers | Evaluated settings | Representation |
| --- | --- | --- | --- |
| scGPT | 12 | Frozen, fine-tuned and random initialization | Model-specific contextual encoding |
| Nicheformer | 12 | Frozen, fine-tuned and random initialization | Model-specific contextual encoding |
| Geneformer V1-10M | 6 | Frozen, fine-tuned and random initialization | Masked mean of final-layer gene-token embeddings |
| Geneformer V2-104M | 12 | Frozen pretrained and frozen random encoders | Source-selected pooling, with the official default identified separately |

Frozen encoders preserve all encoder parameters while training the response head. Geneformer V1 fine-tuning and its random-initialization control update all six encoder layers and the head. scGPT and Nicheformer fine-tuning update their twelve layers. Both Geneformer V2 encoder settings remain frozen, including the random architecture control.

Geneformer V2 accepts sequences of up to 4,096 tokens, including classification and end tokens, using its official vocabulary. The official default representation is the classification token from the penultimate layer. The source-selection candidates also include the mean of final-layer gene-token embeddings, excluding special and padding tokens. Pooling, positive training duration and response amplitude are selected using source-cell-population holdouts. Both reported V2 outputs use source-selected pooling. The V2 pooling search adds a tuning dimension.

Each neural response prediction averages three initializations. Source validation selects trained checkpoints from 25, 75 and 150 updates. A zero-update source-mean fallback is a separate diagnostic. OP3 is a development study, and overlap between model pretraining data and these studies has not been independently excluded.

[Official Geneformer model and tokenizer](https://huggingface.co/ctheodoris/Geneformer), [scGPT](https://github.com/bowang-lab/scGPT) and [Nicheformer](https://github.com/theislab/nicheformer) document the pretrained models. [All matched results](benchmark_comparison.md#op3-drug-responses-in-immune-cells) retain every encoder setting and classical comparator.

| Geneformer V2 setting | Source-selected representation |
| --- | --- |
| Pretrained frozen encoder | Penultimate-layer classification token |
| Random frozen encoder | Penultimate-layer classification token |

## Donor transfer

A separate evaluation withholds one donor and the myeloid cell type jointly. Source responses use only the other two donors. Source validation also withholds one donor and one source cell type, giving six validation folds. Conditions require complete support in the source donor–cell-type groups.

| Held-out donor | Conditions | Gene and programme MSE | Compound-only MSE |
|---|---:|---:|---:|
| First | 107 | 0.130812 | 0.131768 |
| Second | 115 | 0.123658 | 0.124374 |
| Third | 116 | 0.155570 | 0.155762 |

Only the first paired 95% interval excludes zero. Cell-type-only source validation gives mixed programme-model results. The two validation designs have different source-complete condition sets, so their absolute scores cannot isolate the effect of validation alone. These folds share training donors and are not independent studies.

## Gene-set responses

Forty-seven Hallmark gene sets contain at least ten genes on the measured panel. Their mean response error is 0.010078 for the programme model, 0.012649 for the extended compound-only gate and 0.011931 for the gene-only gate. This is a 20.3% reduction relative to compound-only weighting. The paired difference is −0.002571, with a 95% compound-bootstrap interval from −0.003886 to −0.001406. Mean per-compound correlation across these sets increases from 0.512 to 0.544. Gene sets are retained according to annotation coverage, independently of performance. These scores describe coordinated expression responses, not causal pathway activity.

## Independent interferon-response study

The [Kang study](https://doi.org/10.1038/nbt.4042) measures matched untreated and interferon-beta-stimulated immune cells from eight donors. Published singlet labels and fixed quality criteria retain 23,981 cells. Each fold excludes the evaluation donor's stimulated cells and all stimulated monocytes. B, CD4 T, CD8 T and natural killer cells from the other seven donors provide source responses. Untreated target monocytes remain available. The 2,000-gene panel is selected from source controls separately in each fold.

scPerturbMix uses the gene-gate parameters fixed in the OP3 extended search, with source effects estimated within the new study. This tests transfer of weighting parameters for a known stimulus. The programme search selects the gene-only option in this single-stimulus setting. Both fixed OP3 recipes and all source-selected variants are retained in the accompanying result table.

| Target | Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- | --- |
| CD14+ monocytes | scPerturbMix fixed OP3 parameters | — | 0.051356 | 0.139769 | 0.7888 | 0.4359 |
| CD14+ monocytes | Perturbation reliability | — | 0.052678 | 0.140905 | 0.7881 | 0.4370 |
| CD14+ monocytes | Gene reliability | — | 0.052871 | 0.140584 | 0.7882 | 0.4365 |
| CD14+ monocytes | scPerturbMix | — | 0.052871 | 0.140584 | 0.7882 | 0.4365 |
| CD14+ monocytes | scVIDR (original numerical solver) | — | 0.053375 | 0.137688 | 0.8039 | 0.5795 |
| CD14+ monocytes | scVIDR (stable solver) | — | 0.053393 | 0.137635 | 0.8040 | 0.5794 |
| CD14+ monocytes | Mean source response | — | 0.054077 | 0.141531 | 0.7881 | 0.4370 |
| CD14+ monocytes | scVIDR (stable solver, control-anchored) | — | 0.054583 | 0.138366 | 0.8044 | 0.5634 |
| CD14+ monocytes | scGen | — | 0.055909 | 0.138687 | 0.8083 | 0.5787 |
| CD14+ monocytes | Global response scaling | — | 0.056342 | 0.142728 | 0.7881 | 0.4370 |
| CD14+ monocytes | Low-rank response | — | 0.056373 | 0.142764 | 0.7880 | 0.4368 |
| CD14+ monocytes | scPerturbMix (fixed-parameter sensitivity) | — | 0.067911 | 0.149879 | 0.7893 | 0.4345 |
| CD14+ monocytes | CPA (post-warmup, control-anchored) | 8 | 0.079118 | 0.157746 | 0.7571 | 0.4369 |
| CD14+ monocytes | CPA | 8 | 0.082858 | 0.155302 | 0.6187 | 0.5166 |
| CD14+ monocytes | CPA (control-anchored) | 8 | 0.083636 | 0.160522 | 0.7323 | 0.4140 |
| CD14+ monocytes | CPA (post-warmup) | 8 | 0.093255 | 0.160871 | 0.5054 | 0.3835 |
| CD14+ monocytes | biolord (control-anchored) | 8 | 0.093568 | 0.169550 | 0.5562 | 0.4693 |
| CD14+ monocytes | biolord | 8 | 0.093962 | 0.172178 | 0.5619 | 0.4776 |
| CD14+ monocytes | No-change control | — | 0.124769 | 0.182156 | — | — |
| FCGR3A+ monocytes | scVIDR (stable solver) | — | 0.038559 | 0.125226 | 0.8091 | 0.6323 |
| FCGR3A+ monocytes | scVIDR (original numerical solver) | — | 0.038652 | 0.125421 | 0.8090 | 0.6318 |
| FCGR3A+ monocytes | scGen | — | 0.040419 | 0.125964 | 0.8088 | 0.6340 |
| FCGR3A+ monocytes | scVIDR (stable solver, control-anchored) | — | 0.041771 | 0.133465 | 0.7992 | 0.5295 |
| FCGR3A+ monocytes | scPerturbMix fixed OP3 parameters | — | 0.042364 | 0.137598 | 0.7765 | 0.4393 |
| FCGR3A+ monocytes | Perturbation reliability | — | 0.042690 | 0.138029 | 0.7773 | 0.4399 |
| FCGR3A+ monocytes | Gene reliability | — | 0.042946 | 0.137986 | 0.7764 | 0.4397 |
| FCGR3A+ monocytes | scPerturbMix | — | 0.042946 | 0.137986 | 0.7764 | 0.4397 |
| FCGR3A+ monocytes | Mean source response | — | 0.043450 | 0.138544 | 0.7773 | 0.4399 |
| FCGR3A+ monocytes | Global response scaling | — | 0.044873 | 0.139648 | 0.7773 | 0.4399 |
| FCGR3A+ monocytes | Low-rank response | — | 0.044897 | 0.139677 | 0.7772 | 0.4398 |
| FCGR3A+ monocytes | scPerturbMix (fixed-parameter sensitivity) | — | 0.053673 | 0.146808 | 0.7765 | 0.4383 |
| FCGR3A+ monocytes | CPA (post-warmup, control-anchored) | 8 | 0.063314 | 0.154657 | 0.7644 | 0.4342 |
| FCGR3A+ monocytes | CPA (control-anchored) | 8 | 0.064070 | 0.156058 | 0.7395 | 0.3910 |
| FCGR3A+ monocytes | CPA | 8 | 0.068149 | 0.152016 | 0.5869 | 0.4939 |
| FCGR3A+ monocytes | CPA (post-warmup) | 8 | 0.077975 | 0.154930 | 0.5042 | 0.4624 |
| FCGR3A+ monocytes | biolord (control-anchored) | 8 | 0.079414 | 0.169951 | 0.5715 | 0.4162 |
| FCGR3A+ monocytes | biolord | 8 | 0.096413 | 0.177241 | 0.5408 | 0.4783 |
| FCGR3A+ monocytes | No-change control | — | 0.102908 | 0.177429 | — | — |

[scGen](https://github.com/theislab/scgen) and [scVIDR](https://github.com/BhattacharyaLab/scVIDR) use their native variational architectures and objectives: two 800-unit hidden layers, 100 latent coordinates, at most 100 epochs, and source-only validation. Each family has eight donor folds and three initialisations, giving 48 fitted models. All checkpoint reloads reproduce predictions exactly. Mean-response scores use the three-fit ensemble. Distribution scores average individual fits.

scPerturbMix has lower CD14 MSE than scGen, with a paired donor-bootstrap difference of −0.004553 (95% interval −0.006480 to −0.002210). The difference against scVIDR includes zero. scVIDR is more accurate for CD16 MSE and both native models have higher response correlations. scPerturbMix has lower squared MMD than both native models in both populations under the declared source-PCA distribution metric. All 42 Hallmark sets meeting coverage requirements in every fold are included.

The eight donor folds share source training donors. Treatment and control were sequenced in separate lanes in the original study. [Complete mean scores](benchmarks/ifnb_summary.tsv), [donor scores](benchmarks/ifnb_donor_results.tsv), [initialisation results](benchmarks/ifnb_native_seed_results.tsv) and [paired intervals](benchmarks/ifnb_paired_intervals.json) accompany this comparison.

The official CPA model is evaluated on the same eight-donor interferon task in native and control-anchored form. Source-cell validation selects its regularization setting and checkpoint. A separate post-warmup evaluation selects checkpoints after the adversarial objective reaches full strength. scPerturbMix has 33.9–38.6% lower MSE than source-selected CPA and 33.1–45.7% lower MSE than post-warmup CPA across the two monocyte populations and two output conventions. Correlation and distribution scores are included alongside MSE. Native CPA has higher response Spearman correlation in some comparisons.

The [unified comparison](benchmark_comparison.md#kang-interferon-responses-in-monocytes) lists CPA with the other matched methods. [Training settings and complete downloadable results](cpa_benchmark.md) provide model-level, donor-level and initialization-level scores.

CPA and biolord use their official training objectives with source-only checkpoint selection. The CPA post-warmup sensitivity selects checkpoints after the adversarial objective reaches full weight. Each new native-model setting uses eight donor folds and three initializations. Mean-response predictions are averaged across initializations before scoring. Native and control-anchored outputs remain separate. Stimulated cells from the evaluation donor and all stimulated target monocytes are excluded from fitting. Untreated target cells remain available.

[All matched metrics](benchmarks/matched_model_metrics.tsv), [comparison settings](data/baseline_comparison_scope.tsv), and [CPA training details](cpa_benchmark.md) accompany these results.

## Independent multi-cytokine study

The [Parse PBMC cytokine dataset](https://www.parsebiosciences.com/datasets/10-million-human-pbmcs-in-a-single-experiment/) contains 9,697,974 blood immune cells from twelve healthy donors exposed to 90 cytokines and PBS controls. The evaluation predicts CD14 and CD16 monocyte responses from seven B-cell, T-cell and natural-killer-cell populations. Every outer fold excludes stimulated cells from the held-out donor and all stimulated target monocytes. Source controls determine the 2,000-gene panel. Inner validation jointly holds out a donor and source population.

Fixed minimum support of twenty cells in treatment and matched control yields 1,046 CD14 and 957 CD16 donor–cytokine pairs. Scores first average eligible conditions within each donor, then weight the twelve donors equally. All eligible conditions are retained. One donor has only one eligible CD16 condition. The experiment uses one plate per donor, so donor and plate effects are not separately identifiable.

| Predictor | CD14 MSE | CD16 MSE | CD14 response Pearson | CD16 response Pearson |
|---|---:|---:|---:|---:|
| scPerturbMix, frozen source-selection procedure | 0.011929 | 0.018094 | 0.3963 | 0.3381 |
| Global response scaling | 0.011929 | 0.018094 | 0.3963 | 0.3381 |
| Source mean | 0.012313 | 0.018521 | 0.3963 | 0.3381 |
| Untreated | 0.013759 | 0.020295 | Undefined | Undefined |

The selected model reduces MSE by 3.12% and 2.30% relative to the source mean. All twelve folds select zero programme contribution, and predictions match global scaling to displayed precision. Thus this cohort supports response calibration without establishing an additional programme-model benefit. [All nine base comparators and four cell-state variants](benchmarks/parse_model_metrics.tsv) are included, alongside [donor scores](benchmarks/parse_donor_metrics.tsv), [paired intervals](benchmarks/parse_paired_intervals.tsv), [coverage](benchmarks/parse_condition_coverage.tsv) and [all-pair weighting sensitivity](benchmarks/parse_profile_weighted_sensitivity.tsv).

### Cell-state conditioning

A cell-state-conditioned model uses untreated source states to predict response differences between populations. This is a development analysis within the Parse cohort. Hyperparameters remain selected using source-only donor and cell-type holdouts. The selected module has MSE 0.011450 and 0.017577 in CD14 and CD16 monocytes, respectively. These are reductions of 4.01% and 2.86% relative to the frozen selected model. Its predictions are exactly identical to the Gaussian kernel ridge comparator in every fold. This supports the usefulness of cell-state information within this cohort. It does not establish an advantage beyond that classical comparator or constitute a second untouched validation.

Across the same 32 eligible Hallmark sets, mean-response MSE is 0.003694 and 0.003181, compared with 0.004056 and 0.003462 for the frozen model. Mean response Pearson correlation is 0.3959 and 0.3390. [Complete condition scores](benchmarks/parse_per_condition_metrics.tsv) and [analysis scope](benchmarks/parse_summary.json) accompany the results. Outer folds share source training donors.

### Cytokine specificity and donor consistency

An exact decomposition of fixed predictions separates error in the shared cytokine response from error in differences between cytokines. The cytokine-varying component accounts for 67.0% of the kernel model's MSE gain in CD14 monocytes and 56.7% in CD16 monocytes. MSE improves in eight and seven of twelve donors, respectively. Removing any single donor leaves the overall mean improvement positive in both populations. The paired interval for cytokine-centred MSE excludes zero in CD14 but includes zero in CD16. The donor with one eligible CD16 condition remains in the primary analysis. Its centred error is zero by definition, and its centred correlation is undefined.

[Decomposition by model](benchmarks/parse_specificity_model_decomposition.tsv), [donor results](benchmarks/parse_specificity_donor_decomposition.tsv), [condition-level changes](benchmarks/parse_specificity_condition_improvements.tsv) and [paired uncertainty and sensitivity](benchmarks/parse_specificity_summary.json) accompany this diagnostic. No prediction is refitted for the decomposition.

### Donor-reliability extension

A donor-reliability model estimates which source cell-type differences recur across donors. It downweights response components with high donor variability and separately calibrates the shared response and the cell-state correction. Every inner donor and cell-type holdout re-estimates these quantities using only its training sources. A two-amplitude kernel without reliability weighting controls for the additional calibration. Cytokine-level and gene-level weighting are both evaluated, and all twelve source selections choose cytokine-level weighting.

| Predictor | CD14 MSE | CD16 MSE | CD14 response Pearson | CD16 response Pearson |
|---|---:|---:|---:|---:|
| Gaussian kernel ridge | 0.011450 | 0.017577 | 0.3959 | 0.3390 |
| Kernel with two amplitudes | 0.011469 | 0.017601 | 0.3938 | 0.3373 |
| Source-selected donor reliability | 0.011411 | 0.017533 | 0.4039 | 0.3467 |

The source-selected extension reduces MSE by 0.34% and 0.25% relative to Gaussian kernel ridge. The paired differences are −0.0000385 (95% interval −0.0001842 to 0.0001390) and −0.0000441 (−0.0002089 to 0.0001540). Both intervals include zero, as do those for response Pearson gains. The comparison retains the same 2,003 target pairs, source-control gene panels and donor weighting. These models are development analyses within the same Parse cohort.

[All compared variants](benchmarks/parse_replicated_model_metrics.tsv), [donor scores](benchmarks/parse_replicated_donor_metrics.tsv), [condition scores](benchmarks/parse_replicated_per_condition_metrics.tsv), [paired intervals](benchmarks/parse_replicated_paired_intervals.tsv) and [source selections](benchmarks/parse_replicated_source_selections.tsv) provide the full comparison. Source-selected and cytokine-weighted predictions coincide and are not independent replications. This extension is an experimental analysis, not a replacement for the packaged trained transfer model.

The provider distributes the original Parse data under CC BY-NC 4.0. This repository includes analytical summaries, not raw cells. The code licence does not replace third-party data licences.

### Control-state coverage and donor directions

Untreated monocyte states lie farther from their nearest source state than the queries used in source validation. Across twelve outer folds, the median target-to-validation distance ratios are 2.33 for CD14 and 2.25 for CD16 monocytes. Every target exceeds the largest nearest-source distance observed in its source donor–cell-type validation folds. These distances use the same measured gene panels and no treated target values. [Donor-level geometry](benchmarks/parse_geometry_donor_geometry.tsv) and [summary](benchmarks/parse_geometry_summary.json) provide the measurements.

A representation-ablation experiment attenuates donor-associated directions in untreated expression before computing kernel similarities. Each inner validation fold re-estimates these directions using its training donors and cell types. The original representation, three projection ranks and two attenuation strengths share the source-selected Gaussian kernel parameters. Shared-response and residual amplitudes use the same source calibration in all variants.

| Predictor | CD14 MSE | CD16 MSE |
|---|---:|---:|
| Gaussian kernel ridge | 0.011450 | 0.017577 |
| Unmodified representation, two amplitudes | 0.011469 | 0.017601 |
| All donor directions removed | 0.011824 | 0.017914 |

All twelve source selections retain the unmodified representation. This ablation does not support adding donor-direction removal to the model. Donor-associated variation includes both biology and plate effects in this experiment. [All model scores](benchmarks/parse_projection_model_metrics.tsv), [paired intervals](benchmarks/parse_projection_paired_intervals.tsv), [source selections](benchmarks/parse_projection_source_selections.tsv) and [donor results](benchmarks/parse_projection_donor_metrics.tsv) retain the full comparison. The unmodified comparator reproduces the two-amplitude expression-kernel model, and the 2,003 evaluation pairs remain unchanged.

### Receptor context with matched information

A source-selected development experiment tests whether receptor context improves transfer beyond expression similarity. The [CellPhoneDB v5 resource](https://doi.org/10.1038/s41596-024-01137-1) provides curated ligand–receptor directions and complete subunit annotations. Conservative, unique name matching covers 34 of the 90 stimuli, with 36 receptor entities and 43 receptor genes. Their features are measured in untreated control populations. Four receptor genes occur in each original 2,000-gene panel.

The comparison includes an expression kernel, a kernel using all 36 receptor features, a stimulus-specific receptor kernel and an assignment-shuffled control. Pooled and stimulus-specific models receive the same additional control information. Unmapped conditions remain in the evaluation and use expression-based weights. Hyperparameters and amplitudes are selected only in joint source donor–cell-type holdouts. Transcript abundance is a proxy for receptor context, not a direct measurement of receptor activity.

Source validation selects receptor information in 2/12 folds. The complete evaluation retains all 2,003 eligible response pairs. Scores weight donors equally.

| Predictor | CD14 MSE | CD16 MSE | CD14 response Pearson | CD16 response Pearson |
|---|---:|---:|---:|---:|
| Gaussian kernel ridge | 0.011450 | 0.017577 | 0.3959 | 0.3390 |
| Expression kernel, two amplitudes | 0.011469 | 0.017601 | 0.3938 | 0.3373 |
| Pooled receptor features | 0.011469 | 0.017601 | 0.3938 | 0.3373 |
| Stimulus-specific receptors | 0.011488 | 0.017623 | 0.3932 | 0.3368 |
| Shuffled receptor assignments | 0.011478 | 0.017616 | 0.3935 | 0.3370 |
| Source-selected receptor model | 0.011488 | 0.017623 | 0.3932 | 0.3368 |

For the source-selected model compared with Gaussian kernel ridge, the paired MSE differences are 0.0000379 (95% donor interval 0.0000125 to 0.0000703) and 0.0000464 (95% donor interval 0.0000161 to 0.0000838) in CD14 and CD16 monocytes, respectively. The folds share source donors. This is model development within the Parse study, not an additional independent cohort. Coincident source-selected variants are not independent model replications.

[Complete scores](benchmarks/parse_receptor_model_metrics.tsv), [donor results](benchmarks/parse_receptor_donor_metrics.tsv), [condition results](benchmarks/parse_receptor_per_condition_metrics.tsv), [paired intervals](benchmarks/parse_receptor_paired_intervals.tsv), [source selections](benchmarks/parse_receptor_source_selections.tsv), [mapping coverage](benchmarks/parse_receptor_stimulus_coverage.tsv) and [analysis scope](benchmarks/parse_receptor_summary.json) accompany the comparison. The receptor variant remains an experimental analysis and does not replace the packaged trained model.

### Native perturbation models on a matched cell panel

The Parse comparison contains 72 fitted native models: scGen and scVIDR, twelve donor folds and three initialisations per family. Training inputs and target controls use the same frozen samples of at most 64 cells per donor–population–condition group for every method. The source-selected 2,000-gene axes and all 2,003 eligible target pairs remain fixed. Mean-response truth uses all eligible treated cells. Distribution truth uses the sampled cell panel. These scores are a separate matched-input comparison and must not be compared directly with the full-source Parse scores above.

| Predictor | CD14 MSE | CD16 MSE | CD14 response Pearson | CD16 response Pearson |
|---|---:|---:|---:|---:|
| scPerturbMix, gene and programme procedure | 0.019294 | 0.024343 | 0.2431 | 0.2428 |
| Global response scaling | 0.019302 | 0.024340 | 0.2418 | 0.2417 |
| Fixed OP3 gene gate | 0.019174 | 0.024235 | 0.2435 | 0.2431 |
| scGen, native output | 0.022112 | 0.026689 | 0.3605 | 0.3490 |
| scGen, control-anchored output | 0.020190 | 0.024836 | 0.1571 | 0.1801 |
| scVIDR, native output | 0.024065 | 0.027593 | 0.3501 | 0.3462 |
| scVIDR, control-anchored output | 0.021693 | 0.025401 | 0.1461 | 0.1766 |

Native outputs are decoded perturbed profiles. Control-anchored outputs add the decoded perturbed-minus-control change to the observed target control, using the same fitted models. Anchoring lowers mean expression error but also lowers response correlation. The fixed OP3 gate outperforms the gene-and-programme procedure on MSE in both populations. Native scGen and scVIDR retain higher overall response correlations. Mean-response scores use the three-fit prediction ensemble; distribution scores average the three individual-fit metrics.

All 72 fits passed training-boundary and checkpoint-replay checks. Mean metrics were independently recomputed for every model and eligible condition. The single-condition CD16 donor remains included. [All 13 variants](benchmarks/parse_native_panel_model_metrics.tsv), [donor scores](benchmarks/parse_native_panel_donor_metrics.tsv), [paired intervals](benchmarks/parse_native_panel_paired_intervals.tsv) and [fit coverage and boundary checks](benchmarks/parse_native_panel_fit_audit.tsv) are available.

### Training-budget sensitivity

A six-fit training-budget sensitivity evaluates the two native families with a maximum of 300 epochs for three prespecified donors, with one initialisation per family. The checkpoint weights selected within the first 100 epochs are identical in the two training-budget evaluations. Checkpoint selection uses source reconstruction validation throughout. Five fits reach the 300-epoch limit and one stops early, so the experiment does not establish full convergence.

Source reconstruction loss improves, while mean target-response MSE increases for both families, both populations and both output conventions. For example, native scGen CD14 MSE changes from 0.022143 to 0.023310, and native scVIDR from 0.023405 to 0.024441. This three-donor sensitivity analysis is separate from the twelve-donor, three-initialisation comparison. [Model scores](benchmarks/parse_native_budget_model_metrics.tsv), [donor scores](benchmarks/parse_native_budget_donor_metrics.tsv), [paired budget effects](benchmarks/parse_native_budget_paired_effects.tsv) and [training convergence](benchmarks/parse_native_budget_convergence.tsv) retain every fitted model.

### Distribution representation sensitivity

Fixed predictions from all 13 panel variants are evaluated in three 50-dimensional representations: source-control principal components, source-response principal components and a fixed random orthogonal projection. The same twelve donors and 2,003 target pairs are retained in each view. Both learned transforms use source information only.

The gene-and-programme procedure has lower squared MMD and energy distance than the native outputs of scGen and scVIDR in both populations across all three views. Comparisons with control-anchored outputs have narrower differences and some intervals include zero. The procedure does not consistently outperform global scaling or the fixed OP3 gate. Absolute distances should be compared within a representation because the three views use different scales. [View-level scores](benchmarks/parse_native_distribution_view_metrics.tsv), [donor scores](benchmarks/parse_native_distribution_view_donor_metrics.tsv) and [paired intervals](benchmarks/parse_native_distribution_view_paired_intervals.tsv) accompany this check.

### Matched cell-state and donor-reliability comparison

The matched-input analysis includes 21 variants, comparing cell-state kernels and donor-reliability weighting to the same source cells, genes, target controls and evaluation pairs. Every new variant selects its parameters in source-only validation. Coincident selected variants are retained in the tables and are not independent replications.

| Predictor | CD14 MSE | CD16 MSE | CD14 response Pearson | CD16 response Pearson |
|---|---:|---:|---:|---:|
| Gaussian kernel ridge | 0.018999 | 0.023911 | 0.2373 | 0.2415 |
| Source-selected donor reliability | 0.018915 | 0.023843 | 0.2441 | 0.2477 |
| Fixed OP3 gene gate | 0.019174 | 0.024235 | 0.2435 | 0.2431 |

Relative to Gaussian kernel ridge, donor reliability changes MSE by −0.44% in CD14 and −0.28% in CD16 monocytes. The paired mean differences are −0.00008371 and −0.00006716. With 100,000 donor resamples, the respective 95% intervals are [−0.000166993, +0.00000008244] and [−0.000158197, +0.000024467]. Both MSE intervals include zero. Response Pearson correlation increases by 0.0068 and 0.0062, with paired 95% intervals of [0.0029, 0.0109] and [0.0020, 0.0104]. These are small incremental changes, and native scGen and scVIDR still have higher overall response correlations.

The paired tables also include pathway error and cytokine-centred response accuracy. Centred correlation is defined for twelve CD14 donors and eleven CD16 donors; the one-condition CD16 donor remains in all uncentred metrics. Other paired intervals use 5,000 donor resamples. All intervals describe donor variability conditional on fitted predictors with overlapping source folds. This remains model development within the existing Parse study, not a new independent cohort. The independent mouse cytokine study is described in the [external evaluation guide](external_validation.md).

[All 21 variants](benchmarks/parse_matched_context_model_metrics.tsv), [donor scores](benchmarks/parse_matched_context_donor_metrics.tsv), [publication paired intervals, including the high-precision MSE check](benchmarks/parse_matched_context_paired_intervals.tsv) and [source selections](benchmarks/parse_matched_context_source_selections.tsv) provide the evaluation results. `NA` denotes undefined or inapplicable values in the result tables. These experimental variants do not change the packaged model or software API.

### Source-context selection of training duration

A source-context experiment tests training-budget selection on three prespecified source donor–population pairs. It contains six fits and 48 checkpoint snapshots. Each fit excludes treated cells from either held-out source axis. All original monocytes and the outer evaluation donor are absent. Each source pair contains 87 cytokines. The criterion averages response MSE relative to the unchanged-control predictor equally across the three pairs.

| Model | Output | Selected snapshot epoch | Source MSE | Source MSE under the 100-epoch reconstruction rule | Reduction |
|---|---|---:|---:|---:|---:|
| scGen | anchored | 25 | 0.017677 | 0.018054 | 2.08% |
| scGen | native | 50 | 0.011399 | 0.011563 | 1.42% |
| scVIDR | anchored | 25 | 0.017548 | 0.017846 | 1.67% |
| scVIDR | native | 150 | 0.011467 | 0.011632 | 1.42% |

Reconstruction favours checkpoints at epochs 289–300, whereas response-transfer validation selects 50 epochs for native scGen, 150 for native scVIDR and 25 for both anchored outputs. The anchored choice is the earliest tested budget, rather than an unconstrained optimum. These are source-selection scores from the same environments used for tuning. They do not revise the twelve-donor monocyte benchmark or establish an unbiased gain in target performance.

The Donor 1 training-duration comparison uses six 100-epoch checkpoints whose weights match the reference benchmark exactly. Source-selected durations increase native-output MSE in all four model/population settings. The 25-epoch anchored outputs reduce MSE by 1.85–2.11%, while response Pearson decreases. This is one biological donor with three training repetitions per model. [Frozen-budget scores](benchmarks/parse_frozen_budget_model_metrics.tsv) and [paired duration comparisons](benchmarks/parse_frozen_budget_paired_budget_comparisons.tsv) retain all outcomes. Extending the selection procedure to other donor holdouts requires new nested source validation.

[All source curves](benchmarks/parse_source_validation_curves.tsv), [selected budgets](benchmarks/parse_source_budget_selections.tsv), [source score comparisons](benchmarks/parse_source_selection_comparisons.tsv) and [selection sensitivity to leaving out one source pair](benchmarks/parse_source_selection_stability.tsv) provide the diagnostic results.

### Pilot-stimulation calibration

A separate task measures responses to 4, 8 or 16 pilot stimuli in a new donor and monocyte population, then predicts a fixed set of remaining stimuli. Stimulus identities and their responses in source contexts are known. This supervised calibration task uses additional target observations and is separate from the zero-shot comparisons above. All model settings are selected within nine source donor–population holdouts. The primary analysis averages three fixed random panels within each donor, then weights donors equally. It contains twelve CD14 and eleven CD16 donor groups. The one-condition CD16 donor remains in the original zero-shot evaluation.

| Predictor, 16 pilot stimuli unless indicated | CD14 MSE | CD16 MSE | CD14 response Pearson | CD16 response Pearson |
|---|---:|---:|---:|---:|
| Shared-response prior, no pilot observations | 0.018727 | 0.019278 | 0.238 | 0.226 |
| Shared residual calibration | 0.011317 | 0.011845 | 0.736 | 0.705 |
| Gaussian kernel ridge | 0.009863 | 0.010726 | 0.772 | 0.733 |
| Source-covariance kernel ridge | 0.009210 | 0.010268 | 0.775 | 0.734 |
| Independent-noise Gaussian process | 0.009218 | 0.010271 | 0.776 | 0.734 |
| Shared-control-noise Gaussian process | 0.009275 | 0.010292 | 0.776 | 0.735 |

At sixteen observations, source-covariance kernel ridge reduces MSE by 50.82% and 46.74% relative to the same prior on identical query sets. Its additional reduction over shared-residual calibration is 18.62% and 13.31%. Centred and Hallmark response errors also improve, identifying stimulus-specific information beyond a common response offset. A Gaussian process and kernel ridge using identical covariance and regularisation produce the same predictions and count as one method.

Shared-control modelling includes control sampling variance in both the support–support and query–support covariance. This model does not improve mean MSE over source-covariance kernel ridge or independent-noise conditioning in any of the six nonzero-budget/population settings. At sixteen observations it raises centred response correlation slightly, while Hallmark error is higher. The results support the value of pilot observations and source covariance without establishing a performance advantage for the added noise structure. The independent Wood study below tests the same calibration task with source-only refitting. Native pretrained perturbation comparisons are still being prepared. Independent-control sensitivity below shows why the shared-reference improvements cannot be interpreted as reference-independent response recovery.

[All model and budget scores](benchmarks/parse_fewshot_model_metrics.tsv), [donor scores](benchmarks/parse_fewshot_donor_metrics.tsv), [paired donor intervals](benchmarks/parse_fewshot_paired_intervals.tsv), and [independently recomputed noise-model comparisons](benchmarks/parse_fewshot_noise_comparisons.tsv) include the primary random-panel analysis and secondary source-coverage design. Independent verification recomputed all seven metrics for every saved condition-level prediction and checked source, support and query boundaries. This experimental analysis is not a replacement for the stable packaged model.

### Independent blood-cell stimulation cohort

The [Wood study](https://doi.org/10.1186/s13073-026-01721-y) contains 153,443 cells from twelve donors. Five donors qualify for a four-stimulus calibration panel and six for a separate seven-stimulus panel. The batches have different donors and stimuli and are reported separately. A fixed twenty-cell threshold excludes one donor from the complete four-stimulus task, while retaining its three supported responses in a zero-support diagnostic. Raw count identities, library sizes, detected-gene counts and independently recalculated metrics passed verification.

| Maximum-support comparison | Batch A: one support | Batch B: two supports |
|---|---:|---:|
| Shared-response prior MSE | 0.085538 | 0.044565 |
| Shared residual MSE | 0.052706 | 0.037449 |
| Gaussian KRR MSE | 0.052891 | 0.037653 |
| Source-covariance KRR MSE | 0.053467 | 0.037354 |
| Shared-control-noise GP MSE | 0.053504 | 0.037496 |

Source-covariance KRR reduces MSE relative to the prior by 37.49% and 16.18%. Simple calibration is competitive, and explicit shared-control noise has no consistent advantage. These are independently collected experimental data with within-cohort source refitting, not predictions from unchanged Parse-trained weights. Repeated support designs are averaged within donor. [All scores](benchmarks/wood_calibration_model_metrics.tsv), [donor scores](benchmarks/wood_calibration_donor_metrics.tsv) and [exact empirical donor-bootstrap intervals](benchmarks/wood_calibration_paired_donor_intervals_exact_bootstrap.tsv) retain every eligible comparison. GP and KRR with identical covariance coincide numerically. The low-rank covariance also coincides with full covariance on these short panels.

### Shared and independent control references

A separate Parse technical sensitivity splits the fixed target cell panels into disjoint halves. Predictions use only control half A. After all predictions are fixed, evaluation responses subtract either half A or half B. Two support-cell halves and three stimulus designs are averaged within donor. Source-only validation selects predictors separately for the two reference conditions.

| Sixteen pilot stimuli | CD14 MSE | CD16 MSE |
|---|---:|---:|
| Shared reference, covariance KRR | 0.009895 | 0.010981 |
| Independent reference, prior | 0.025845 | 0.026440 |
| Independent reference, covariance KRR | 0.027007 | 0.027625 |
| Independent reference, control-noise model | 0.025041 | 0.025803 |

The control-noise model improves independent-reference MSE over the prior by 3.11% and 2.41%. Its Hallmark advantage over KRR is uncertain. Source validation selects zero shared-residual correction in every independent-reference selection. Holding shared-regime KRR predictions and cell inputs fixed, changing only the evaluation reference increases MSE by 0.026647 and 0.025782. Stimulus-centred metrics remain unchanged under this reference change. This isolates sensitivity to the measured control. The split-cell scores use smaller target panels than the original benchmark and are not pooled with those scores.

The noise search includes zero noise and the full KRR penalty grid, preserving KRR as an exact special case. Source selection chooses positive noise while retaining the zero-noise KRR solution as an eligible candidate. [All model scores](benchmarks/parse_control_split_model_metrics.tsv), [donor values](benchmarks/parse_control_split_donor_metrics.tsv), [paired intervals](benchmarks/parse_control_split_paired_model_intervals.tsv) and [fixed-prediction reference comparisons](benchmarks/parse_control_split_identical_prediction_control_reuse.tsv) provide the complete sensitivity results.

The independent Wood study uses the same fixed technical-sensitivity design. With independent query controls, covariance KRR gives MSE 0.072615 in batch A and 0.050590 in batch B, against priors of 0.092876 and 0.051450. The control-noise model gives 0.073580 in batch A. In batch B, source validation selects zero noise contribution, making its predictions identical to KRR. Thus, the additional noise-model gain in Parse does not replicate here. With shared-regime KRR predictions fixed, changing only the query control increases MSE by 0.010916 and 0.016605. This confirms control-reference sensitivity across studies. [Wood split-control scores](benchmarks/wood_control_split_model_metrics.tsv), [donor scores](benchmarks/wood_control_split_donor_metrics.tsv), [paired intervals](benchmarks/wood_control_split_paired_model_intervals.tsv) and [fixed-prediction reference comparisons](benchmarks/wood_control_split_identical_prediction_control_reuse.tsv) retain all outcomes. This technical split is separate from the original full-panel Wood validation above.

### Numerically stable native-model comparisons

The centred scVIDR regression has at most six source directions in Parse and three in Kang. A fixed double-precision minimum-norm solver removes amplification of rounding errors in nearly zero singular directions. Both regression implementations use the same 36 Parse and 24 Kang fitted checkpoints. Their outputs are reported separately.

Stable scVIDR native MSE is 0.024118/0.027611 in Parse CD14/CD16 monocytes and 0.053393/0.038559 in Kang CD14/FCGR3A monocytes. In Kang FCGR3A cells, scVIDR retains lower mean-response MSE than the fixed refined reliability model. The regression comparison isolates numerical-solver sensitivity while keeping the learned neural representations fixed.

[Parse stable scores](benchmarks/parse_stable_scvidr_model_metrics.tsv), [Parse paired comparisons](benchmarks/parse_stable_scvidr_paired_comparisons.tsv), [Kang stable scores](benchmarks/kang_stable_scvidr_model_metrics.tsv) and [Kang paired comparisons](benchmarks/kang_stable_scvidr_paired_comparisons.tsv) report the double-precision solver variants. Package-default and minimum-norm regression results remain separately identified. Experimental benchmark extensions do not change the stable packaged prediction API.

## Data verification

### Perturbation-specific information

Removing each gene's average response across drugs gives a correlation of 0.273 for the programme model, compared with 0.203 for the compound-only gate, 0.236 for the gene-only gate, 0.189 for fine-tuned scGPT and 0.190 for frozen Nicheformer. This diagnostic evaluates differences between drugs after removing a shared expression pattern. All predictions remain fixed.

The programme model lowers MSE for 110 of 127 drugs relative to compound-only weighting. Its paired mean difference is −0.002672, with a 95% compound-bootstrap interval of −0.003722 to −0.001700. The drug-varying component accounts for 84.0% of this improvement. Removing any single drug leaves the average difference negative. Randomly permuting complete predicted vectors across drug labels increases programme-model MSE from 0.073151 to 0.091463 on average. All drug-aware comparator families also outperform their shuffled predictions.

[Model diagnostics](benchmarks/specificity_model_metrics.tsv), [per-drug values](benchmarks/specificity_per_drug_metrics.tsv) and [paired comparisons](benchmarks/specificity_summary.json) include every compared model and all drugs. The three donor-stratified analyses retain shared source training donors and are distinct from the joint donor holdouts above.

### Technical repeatability

Ten disjoint-half partitions within each eligible treatment and control profile use 36,722 original myeloid cells across 421 profiles. Summing the two count halves exactly reconstructs every original profile. All 127 drugs are retained, with at least ten cells per half. Mean response correlation between halves is 0.354, or 0.360 after removing the shared response. These partitions measure cell-sampling repeatability within the same experiments. They are not independent biological replicates or a strict model-performance ceiling. [Partition scores](benchmarks/split_half_partition_metrics.tsv) and [drug-level repeatability](benchmarks/split_half_per_drug_repeatability.tsv) are provided.

### Distribution-metric sensitivity

The interferon comparison retains fixed predictions and source-only PCA transforms. Eighteen MMD settings combine 20 or 50 principal components, bandwidth multipliers of 0.5, 1 or 2, and requested sample sizes of 64, 128 or 256 cells per arm. Available cells cap each sample size equally across models. Five subsamples are averaged within each donor. Native-model distribution scores also average their three fits.

scPerturbMix has lower biased and unbiased squared MMD than scGen and scVIDR in both monocyte populations under all 18 settings, with every paired donor interval below zero. Energy distance gives the same direction across its six unique settings. This evidence concerns cell distributions. scVIDR retains lower CD16 mean-response MSE. Sensitivity settings are not independent replications.

[Setting means](benchmarks/distribution_sensitivity_setting_means.tsv), [donor scores](benchmarks/distribution_sensitivity_donor_results.tsv), [paired intervals](benchmarks/distribution_sensitivity_paired_intervals.tsv) and [summary](benchmarks/distribution_sensitivity_summary.json) accompany the analysis. Energy values repeat across bandwidths in the detailed tables, but the summary counts each of the six unique energy settings once.

### Original count reconstruction

Reaggregation of the released 298,087 single cells exactly reproduces all 1,813 published pseudobulk count profiles and their cell counts on the evaluation panel. The 21,265-gene original release stores raw counts in `AnnData.raw.X`; `AnnData.X` contains processed expression.

The task is a development evaluation on a public study. It does not establish clinical or unseen-compound performance. Primary data: [OP3 benchmark](https://doi.org/10.52202/079017-0650). Model sources: [scGPT](https://github.com/bowang-lab/scGPT) and [Nicheformer](https://github.com/theislab/nicheformer). Gene sets: [MSigDB Hallmarks](https://doi.org/10.1016/j.cels.2015.12.004).

## Native pretrained generation in the Wood study

The independent Wood study evaluates the pretrained Stack-Large-Aligned model. This comparison supplied no treated target cells. It included 65 eligible stimulus responses across twelve held-out donors, with six donors in each of two stimulation batches. Stack and the classical models used a common 14,748-gene count denominator and the same source-selected evaluation genes. These results form a separate comparison from the full-library pilot experiment.

In batch A, native Stack gave MSE 0.098221, compared with 0.113308 for a source-calibrated mean response. Subtracting Stack's generated control and adding the observed target control reduced MSE to 0.089598. In batch B, native MSE was 0.101268 and control anchoring reduced it to 0.052368, close to the classical linear model's 0.051891. Native Stack had higher response correlations than the classical models in both batches, reaching 0.560 and 0.374. Its stimulus-centred correlations were also higher, indicating improved agreement with differences between stimuli. Complete errors, correlations, pathway metrics and paired donor intervals are reported in Supplementary Information. These results distinguish useful pretrained response information from errors in reconstructing the target's untreated background.

### Stimulation batch A

Six biological donors contribute equally.

| Predictor | MSE | MAE | Pearson | Spearman | Centred MSE | Centred Pearson | Pathway MSE |
|---|---|---|---|---|---|---|---|
| Calibrated source mean | 0.113308 | 0.236042 | 0.294372 | 0.164723 | 0.032851 | 0.270401 | 0.026297 |
| Gaussian kernel ridge | 0.113805 | 0.236920 | 0.294630 | 0.164615 | 0.033039 | 0.269485 | 0.026411 |
| Linear ridge | 0.119680 | 0.245135 | 0.274705 | 0.148169 | 0.034538 | 0.238161 | 0.029006 |
| Source mean | 0.118037 | 0.242331 | 0.294372 | 0.164723 | 0.036387 | 0.270401 | 0.026436 |
| Stack, control-anchored | 0.089598 | 0.209672 | 0.512831 | 0.395303 | 0.027847 | 0.417341 | 0.018578 |
| Stack, native | 0.098221 | 0.218160 | 0.560453 | 0.550383 | 0.027847 | 0.417341 | 0.012687 |
| Unchanged control | 0.124607 | 0.245642 | — | — | 0.035594 | — | 0.035986 |

### Stimulation batch B

Six biological donors contribute equally.

| Predictor | MSE | MAE | Pearson | Spearman | Centred MSE | Centred Pearson | Pathway MSE |
|---|---|---|---|---|---|---|---|
| Calibrated source mean | 0.052771 | 0.159654 | 0.173433 | 0.143411 | 0.030302 | 0.241802 | 0.014323 |
| Gaussian kernel ridge | 0.052708 | 0.159758 | 0.178502 | 0.147337 | 0.030282 | 0.244715 | 0.014024 |
| Linear ridge | 0.051891 | 0.158203 | 0.186704 | 0.147898 | 0.029922 | 0.252438 | 0.013538 |
| Source mean | 0.058438 | 0.171724 | 0.173433 | 0.143411 | 0.033663 | 0.241802 | 0.014710 |
| Stack, control-anchored | 0.052368 | 0.160703 | 0.251050 | 0.178092 | 0.029291 | 0.344642 | 0.011997 |
| Stack, native | 0.101268 | 0.229656 | 0.374318 | 0.366247 | 0.029291 | 0.344642 | 0.023449 |
| Unchanged control | 0.053644 | 0.158862 | — | — | 0.031719 | — | 0.015943 |

The [official Stack model](https://huggingface.co/arcinstitute/Stack-Large-Aligned) uses pretrained weights and its native masked-denoising generator. Each held-out donor receives source lymphoid context from five other donors in the same batch. Stimulated target monocytes and stimulated cells from the target donor are excluded. The permitted panel and output gene axis are shared with classical models. Native attention samples a subset of the available context, while classical methods use panel means. Thirty-six generations comprise three technical draws for each of twelve biological donors. Draw-level metrics are averaged within donors. They are not scored as an ensemble mean.

The common-vocabulary denominator contains 14,748 genes, and 2,000 genes are selected from source controls within each fold. These scores must be compared within this table. The Wood pilot analysis uses a different expression denominator and target-information budget. Parse was part of Stack's alignment data. Wood overlap with pretraining is unknown. The comparison assesses the released pretrained model under this explicit input design.

[Complete scores](benchmarks/wood_stack_model_metrics.tsv), [donor scores](benchmarks/wood_stack_donor_metrics.tsv), [condition scores](benchmarks/wood_stack_condition_metrics.tsv) and [exact paired-donor intervals](benchmarks/wood_stack_paired_donor_intervals.tsv) provide all seven evaluation metrics. Independent recomputation from raw counts reproduces reported metrics to numerical precision.

## Scope of baseline comparisons

The [comparison-scope table](data/baseline_comparison_scope.tsv) records 28 model/task comparisons. It distinguishes common input and scoring conditions from model-specific optimisation and adaptation. Source-selected classical models, pretrained representation adapters, native cell-level models and task-adapted neural models answer different questions. The State dose comparison trains its architecture from scratch. It is not a pretrained-State result. Reconstruction-selected and source-response-selected native checkpoints are reported separately. Folds share source training donors, and technical repeats do not increase the biological sample size.

## Relative error with a shared untreated reference

In the matched Parse cytokine benchmark, scPerturbMix has 2.0–11.3% lower mean squared prediction error than control-anchored scGen and numerically stable control-anchored scVIDR across CD14 and CD16 monocytes. The range covers four aggregate comparisons, with twelve donors in each population. Both CD14 paired intervals exclude zero; both CD16 intervals include zero. [Relative errors and paired donor intervals](benchmarks/matched_immune_relative_errors.tsv) report the four comparisons. Response-correlation rankings are reported separately above.

## Mechanism and classical-estimator comparisons

The [mechanism guide](mechanism_evidence.md) explains source-reselected component ablations, learned-basis controls and the cross-context basis variant. Complete classical estimators appear alongside pretrained models in the [unified task tables](benchmark_comparison.md).

## Independent mouse cytokine study

The [Immune Dictionary evaluation](external_validation.md) adds 438 eligible population–cytokine pairs from an independent in vivo study. The fitting rule is refitted to mouse source populations. Eight models, all six eligible target populations, published-signature endpoints and paired intervals are provided together.
