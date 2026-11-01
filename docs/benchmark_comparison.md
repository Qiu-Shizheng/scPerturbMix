# Benchmark comparisons

Classical response estimators, single-cell perturbation models and pretrained-model adaptations are grouped together for each of eleven matched tasks. Every evaluated row in the complete metrics table is included below. Compare methods within a target group, because expression scales and prediction settings differ across studies.

**MSE** and **MAE** measure prediction error, so lower is better. **Response Pearson** and **Response Spearman** measure agreement in gene-response patterns, so higher is better. A dash marks an undefined or unavailable metric. Constant zero responses have undefined response correlations.

[Summary table](benchmarks/matched_model_summary.tsv) · [Complete metrics](benchmarks/matched_model_metrics.tsv) · [Comparison settings](data/baseline_comparison_scope.tsv) · [Dataset guide](data_and_tasks.md)

## OP3 drug responses in immune cells

The OP3 screen measures how drugs change gene expression in human blood immune cells. B cells, T cells and natural killer cells provide source responses. Models predict myeloid responses on the same 5,317-gene panel. Donor rows are strata of this cell-population benchmark. Joint donor and cell-population holdouts are described separately in the detailed evidence.

### Donor 1

Evaluation gene panel: 5,317 genes.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| scPerturbMix | 120 | 0.134354 | 0.247807 | 0.1627 | 0.1157 |
| Gene reliability | 120 | 0.135798 | 0.248345 | 0.1498 | 0.1054 |
| Gene-specific variance shrinkage | 120 | 0.136372 | 0.248515 | 0.1535 | 0.1081 |
| Pooled Stein-form shrinkage | 120 | 0.136464 | 0.249173 | 0.1330 | 0.1032 |
| Shared-response gene shrinkage | 120 | 0.136541 | 0.248988 | 0.1538 | 0.1093 |
| Unit-penalty pooled Stein-form shrinkage | 120 | 0.136575 | 0.249385 | 0.1330 | 0.1032 |
| Shared-response positive-part shrinkage | 120 | 0.136705 | 0.249106 | 0.1518 | 0.1085 |
| Positive-part gene shrinkage | 120 | 0.136769 | 0.249012 | 0.1491 | 0.1088 |
| Perturbation reliability | 120 | 0.137151 | 0.249586 | 0.1299 | 0.1011 |
| Shared-response pooled Stein-form shrinkage | 120 | 0.137677 | 0.250871 | 0.1281 | 0.0949 |
| Shared-response compound shrinkage | 120 | 0.137961 | 0.250595 | 0.1317 | 0.0989 |
| Low-rank response | 120 | 0.138072 | 0.250088 | 0.1190 | 0.0819 |
| Geneformer V2 (frozen encoder) | 120 | 0.138861 | 0.250166 | 0.1334 | 0.1042 |
| Separate shared-response and intervention amplitudes | 120 | 0.138893 | 0.250872 | 0.1312 | 0.0991 |
| Nicheformer (frozen encoder) | 120 | 0.139012 | 0.250310 | 0.1314 | 0.1022 |
| Nicheformer (fine-tuned encoder) | 120 | 0.139056 | 0.250333 | 0.1309 | 0.1017 |
| Global response scaling | 120 | 0.139107 | 0.250519 | 0.1299 | 0.1011 |
| Nicheformer architecture (random initialization) | 120 | 0.139113 | 0.250413 | 0.1304 | 0.1014 |
| scGPT architecture (random initialization) | 120 | 0.139144 | 0.250448 | 0.1300 | 0.1008 |
| Geneformer V1 architecture (random initialization) | 120 | 0.139149 | 0.250461 | 0.1299 | 0.1010 |
| scGPT (fine-tuned encoder) | 120 | 0.139152 | 0.250473 | 0.1299 | 0.1018 |
| Geneformer V2 architecture (frozen random encoder) | 120 | 0.139161 | 0.250472 | 0.1298 | 0.1010 |
| scGPT (frozen encoder) | 120 | 0.139849 | 0.251449 | 0.1213 | 0.0953 |
| Geneformer V1 (frozen encoder) | 120 | 0.143600 | 0.256214 | 0.0961 | 0.0779 |
| Geneformer V1 (fine-tuned encoder) | 120 | 0.143635 | 0.256076 | 0.0944 | 0.0779 |
| Unit-penalty positive-part gene shrinkage | 120 | 0.144552 | 0.260838 | 0.1491 | 0.1088 |
| Shared source response | 120 | 0.145985 | 0.256850 | 0.0799 | 0.0581 |
| Mean source response | 120 | 0.173341 | 0.292624 | 0.1299 | 0.1011 |

### Donor 2

Evaluation gene panel: 5,317 genes.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| scPerturbMix | 120 | 0.118685 | 0.234285 | 0.1713 | 0.1187 |
| Shared-response gene shrinkage | 120 | 0.119228 | 0.234561 | 0.1755 | 0.1233 |
| Gene reliability | 120 | 0.119471 | 0.234704 | 0.1564 | 0.1061 |
| Shared-response positive-part shrinkage | 120 | 0.119538 | 0.234775 | 0.1688 | 0.1210 |
| Gene-specific variance shrinkage | 120 | 0.119557 | 0.234578 | 0.1608 | 0.1090 |
| Shared-response pooled Stein-form shrinkage | 120 | 0.119783 | 0.235984 | 0.1778 | 0.1227 |
| Shared-response compound shrinkage | 120 | 0.119949 | 0.235783 | 0.1719 | 0.1215 |
| Positive-part gene shrinkage | 120 | 0.119963 | 0.235079 | 0.1560 | 0.1100 |
| Separate shared-response and intervention amplitudes | 120 | 0.120405 | 0.235842 | 0.1687 | 0.1205 |
| Pooled Stein-form shrinkage | 120 | 0.120896 | 0.236118 | 0.1367 | 0.1034 |
| Perturbation reliability | 120 | 0.120897 | 0.236101 | 0.1338 | 0.1015 |
| Unit-penalty pooled Stein-form shrinkage | 120 | 0.121055 | 0.236361 | 0.1367 | 0.1034 |
| Nicheformer (frozen encoder) | 120 | 0.121606 | 0.236169 | 0.1375 | 0.1045 |
| Geneformer V2 (frozen encoder) | 120 | 0.121629 | 0.236228 | 0.1370 | 0.1043 |
| Nicheformer (fine-tuned encoder) | 120 | 0.121653 | 0.236212 | 0.1366 | 0.1035 |
| Nicheformer architecture (random initialization) | 120 | 0.121747 | 0.236332 | 0.1351 | 0.1025 |
| scGPT architecture (random initialization) | 120 | 0.121807 | 0.236413 | 0.1338 | 0.1013 |
| Global response scaling | 120 | 0.121818 | 0.236506 | 0.1338 | 0.1015 |
| Geneformer V1 architecture (random initialization) | 120 | 0.121830 | 0.236438 | 0.1335 | 0.1013 |
| Geneformer V2 architecture (frozen random encoder) | 120 | 0.121839 | 0.236446 | 0.1334 | 0.1011 |
| scGPT (fine-tuned encoder) | 120 | 0.121865 | 0.236474 | 0.1332 | 0.1016 |
| Low-rank response | 120 | 0.122374 | 0.236995 | 0.1227 | 0.0845 |
| scGPT (frozen encoder) | 120 | 0.122739 | 0.237700 | 0.1233 | 0.0950 |
| Shared source response | 120 | 0.123941 | 0.239471 | 0.1483 | 0.0992 |
| Geneformer V1 (frozen encoder) | 120 | 0.126781 | 0.243091 | 0.0953 | 0.0748 |
| Geneformer V1 (fine-tuned encoder) | 120 | 0.127571 | 0.243811 | 0.0891 | 0.0719 |
| Unit-penalty positive-part gene shrinkage | 120 | 0.128995 | 0.247449 | 0.1560 | 0.1100 |
| Mean source response | 120 | 0.157885 | 0.280424 | 0.1338 | 0.1015 |

### Donor 3

Evaluation gene panel: 5,317 genes.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| scPerturbMix | 124 | 0.155580 | 0.263980 | 0.1616 | 0.1225 |
| Gene reliability | 124 | 0.156268 | 0.264590 | 0.1455 | 0.1065 |
| Gene-specific variance shrinkage | 124 | 0.156365 | 0.264568 | 0.1485 | 0.1094 |
| Shared-response gene shrinkage | 124 | 0.156654 | 0.264936 | 0.1478 | 0.1083 |
| Shared-response positive-part shrinkage | 124 | 0.156691 | 0.265012 | 0.1468 | 0.1082 |
| Positive-part gene shrinkage | 124 | 0.156703 | 0.265005 | 0.1436 | 0.1094 |
| Perturbation reliability | 124 | 0.157722 | 0.265869 | 0.1255 | 0.1019 |
| Pooled Stein-form shrinkage | 124 | 0.158152 | 0.266071 | 0.1278 | 0.1034 |
| Geneformer V2 (frozen encoder) | 124 | 0.158389 | 0.266025 | 0.1286 | 0.1032 |
| Unit-penalty pooled Stein-form shrinkage | 124 | 0.158404 | 0.266342 | 0.1278 | 0.1034 |
| Nicheformer (frozen encoder) | 124 | 0.158591 | 0.266216 | 0.1263 | 0.1019 |
| Global response scaling | 124 | 0.158605 | 0.266320 | 0.1255 | 0.1019 |
| Nicheformer architecture (random initialization) | 124 | 0.158615 | 0.266240 | 0.1258 | 0.1020 |
| Nicheformer (fine-tuned encoder) | 124 | 0.158628 | 0.266237 | 0.1258 | 0.1017 |
| scGPT architecture (random initialization) | 124 | 0.158629 | 0.266248 | 0.1255 | 0.1016 |
| Geneformer V1 architecture (random initialization) | 124 | 0.158631 | 0.266264 | 0.1255 | 0.1019 |
| Geneformer V2 architecture (frozen random encoder) | 124 | 0.158634 | 0.266267 | 0.1255 | 0.1019 |
| scGPT (fine-tuned encoder) | 124 | 0.158651 | 0.266315 | 0.1254 | 0.1024 |
| Low-rank response | 124 | 0.158811 | 0.266216 | 0.1221 | 0.0977 |
| Shared-response compound shrinkage | 124 | 0.158977 | 0.266712 | 0.1168 | 0.0961 |
| Shared-response pooled Stein-form shrinkage | 124 | 0.159429 | 0.267157 | 0.1117 | 0.0919 |
| Separate shared-response and intervention amplitudes | 124 | 0.159534 | 0.266880 | 0.1142 | 0.0953 |
| scGPT (frozen encoder) | 124 | 0.159840 | 0.267748 | 0.1126 | 0.0943 |
| Geneformer V1 (frozen encoder) | 124 | 0.160420 | 0.268541 | 0.1094 | 0.0913 |
| Geneformer V1 (fine-tuned encoder) | 124 | 0.161480 | 0.269615 | 0.0989 | 0.0844 |
| Unit-penalty positive-part gene shrinkage | 124 | 0.166738 | 0.276968 | 0.1436 | 0.1094 |
| Shared source response | 124 | 0.168035 | 0.272681 | 0.0453 | 0.0515 |
| Mean source response | 124 | 0.195780 | 0.307577 | 0.1255 | 0.1019 |

### Pooled myeloid cells

Evaluation gene panel: 5,317 genes.

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

## Cellarity drug responses in primary cells

The Cellarity DrugReflector study compares cultured cells with primary human cells exposed to drugs. Six cultured backgrounds provide training responses. Four primary populations supply the targets: blood progenitors, T cells, airway epithelial cells and adipocyte precursors.

### CD34+ blood progenitors

Evaluation gene panel: 13,290 genes.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| scPerturbMix | 44 | 0.028721 | 0.115434 | 0.2250 | 0.2041 |
| Gene reliability | 44 | 0.029001 | 0.115918 | 0.2165 | 0.1942 |
| Pooled Stein-form shrinkage | 44 | 0.029080 | 0.115940 | 0.2104 | 0.1907 |
| Gene-specific variance shrinkage | 44 | 0.029087 | 0.116277 | 0.2173 | 0.1968 |
| Unit-penalty pooled Stein-form shrinkage | 44 | 0.029105 | 0.116015 | 0.2104 | 0.1907 |
| Perturbation reliability | 44 | 0.029110 | 0.116153 | 0.2104 | 0.1907 |
| Positive-part gene shrinkage | 44 | 0.029149 | 0.116441 | 0.2165 | 0.1968 |
| Shared-response gene shrinkage | 44 | 0.029167 | 0.116707 | 0.2164 | 0.1953 |
| Shared-response pooled Stein-form shrinkage | 44 | 0.029192 | 0.116718 | 0.2128 | 0.1949 |
| Shared-response positive-part shrinkage | 44 | 0.029193 | 0.116700 | 0.2162 | 0.1950 |
| Shared-response compound shrinkage | 44 | 0.029251 | 0.116945 | 0.2115 | 0.1939 |
| Low-rank response | 44 | 0.029253 | 0.116798 | 0.2055 | 0.1895 |
| Separate shared-response and intervention amplitudes | 44 | 0.029497 | 0.117457 | 0.2115 | 0.1927 |
| Global response scaling | 44 | 0.029509 | 0.117447 | 0.2104 | 0.1907 |
| Unit-penalty positive-part gene shrinkage | 44 | 0.029767 | 0.118107 | 0.2165 | 0.1972 |
| Mean source response | 44 | 0.032082 | 0.124431 | 0.2104 | 0.1907 |
| Shared source response | 44 | 0.033252 | 0.124391 | 0.1095 | 0.1029 |

### CD8+ T cells

Evaluation gene panel: 13,290 genes.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| Global response scaling | 4 | 0.014803 | 0.085284 | 0.2934 | 0.2816 |
| scPerturbMix | 4 | 0.014821 | 0.084703 | 0.2824 | 0.2719 |
| Separate shared-response and intervention amplitudes | 4 | 0.014851 | 0.085525 | 0.2895 | 0.2781 |
| Low-rank response | 4 | 0.014890 | 0.085827 | 0.2555 | 0.2511 |
| Gene-specific variance shrinkage | 4 | 0.014917 | 0.084905 | 0.2899 | 0.2834 |
| Positive-part gene shrinkage | 4 | 0.014934 | 0.085260 | 0.2900 | 0.2811 |
| Pooled Stein-form shrinkage | 4 | 0.014954 | 0.085052 | 0.2934 | 0.2816 |
| Shared-response compound shrinkage | 4 | 0.014955 | 0.085871 | 0.2830 | 0.2722 |
| Shared-response gene shrinkage | 4 | 0.014970 | 0.085574 | 0.2856 | 0.2724 |
| Shared-response positive-part shrinkage | 4 | 0.014973 | 0.085623 | 0.2869 | 0.2723 |
| Shared-response pooled Stein-form shrinkage | 4 | 0.014993 | 0.085941 | 0.2852 | 0.2742 |
| Perturbation reliability | 4 | 0.015035 | 0.085191 | 0.2934 | 0.2816 |
| Unit-penalty pooled Stein-form shrinkage | 4 | 0.015040 | 0.085308 | 0.2934 | 0.2816 |
| Gene reliability | 4 | 0.015056 | 0.085026 | 0.2940 | 0.2829 |
| Unit-penalty positive-part gene shrinkage | 4 | 0.016429 | 0.089480 | 0.2871 | 0.2785 |
| Shared source response | 4 | 0.017860 | 0.093870 | 0.1167 | 0.1117 |
| Mean source response | 4 | 0.018816 | 0.097987 | 0.2934 | 0.2816 |

### Bronchial epithelial cells

Evaluation gene panel: 13,290 genes.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| scPerturbMix | 44 | 0.046215 | 0.144379 | 0.2198 | 0.1932 |
| Unit-penalty pooled Stein-form shrinkage | 44 | 0.046289 | 0.144622 | 0.2112 | 0.1881 |
| Pooled Stein-form shrinkage | 44 | 0.046326 | 0.144649 | 0.2112 | 0.1881 |
| Perturbation reliability | 44 | 0.046383 | 0.144858 | 0.2112 | 0.1881 |
| Gene reliability | 44 | 0.046391 | 0.144734 | 0.2131 | 0.1899 |
| Shared-response pooled Stein-form shrinkage | 44 | 0.046876 | 0.145912 | 0.2145 | 0.1916 |
| Unit-penalty positive-part gene shrinkage | 44 | 0.046921 | 0.146080 | 0.2097 | 0.1888 |
| Shared-response compound shrinkage | 44 | 0.047048 | 0.146220 | 0.2139 | 0.1911 |
| Gene-specific variance shrinkage | 44 | 0.047075 | 0.145693 | 0.2109 | 0.1914 |
| Positive-part gene shrinkage | 44 | 0.047139 | 0.145916 | 0.2114 | 0.1899 |
| Shared-response gene shrinkage | 44 | 0.047183 | 0.146175 | 0.2138 | 0.1917 |
| Shared-response positive-part shrinkage | 44 | 0.047202 | 0.146189 | 0.2133 | 0.1911 |
| Low-rank response | 44 | 0.047414 | 0.146242 | 0.2054 | 0.1836 |
| Separate shared-response and intervention amplitudes | 44 | 0.047726 | 0.147051 | 0.2132 | 0.1900 |
| Global response scaling | 44 | 0.047771 | 0.147047 | 0.2112 | 0.1881 |
| Mean source response | 44 | 0.048404 | 0.150117 | 0.2112 | 0.1881 |
| Shared source response | 44 | 0.053483 | 0.155172 | 0.1258 | 0.1158 |

### Preadipocytes

Evaluation gene panel: 13,290 genes.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| scPerturbMix | 44 | 0.033806 | 0.122431 | 0.2219 | 0.2040 |
| Pooled Stein-form shrinkage | 44 | 0.034099 | 0.122878 | 0.2102 | 0.1936 |
| Gene reliability | 44 | 0.034104 | 0.122941 | 0.2147 | 0.1964 |
| Unit-penalty pooled Stein-form shrinkage | 44 | 0.034126 | 0.122940 | 0.2102 | 0.1936 |
| Perturbation reliability | 44 | 0.034188 | 0.123111 | 0.2102 | 0.1936 |
| Gene-specific variance shrinkage | 44 | 0.034190 | 0.123316 | 0.2141 | 0.1983 |
| Positive-part gene shrinkage | 44 | 0.034235 | 0.123478 | 0.2135 | 0.1979 |
| Shared-response pooled Stein-form shrinkage | 44 | 0.034313 | 0.123790 | 0.2089 | 0.1924 |
| Shared-response positive-part shrinkage | 44 | 0.034318 | 0.123811 | 0.2113 | 0.1922 |
| Shared-response gene shrinkage | 44 | 0.034320 | 0.123823 | 0.2117 | 0.1927 |
| Shared-response compound shrinkage | 44 | 0.034405 | 0.124048 | 0.2074 | 0.1910 |
| Global response scaling | 44 | 0.034585 | 0.124431 | 0.2102 | 0.1936 |
| Low-rank response | 44 | 0.034601 | 0.124229 | 0.1986 | 0.1860 |
| Separate shared-response and intervention amplitudes | 44 | 0.034629 | 0.124523 | 0.2099 | 0.1934 |
| Unit-penalty positive-part gene shrinkage | 44 | 0.034901 | 0.124940 | 0.2124 | 0.1970 |
| Mean source response | 44 | 0.037290 | 0.130650 | 0.2102 | 0.1936 |
| Shared source response | 44 | 0.038559 | 0.131298 | 0.0967 | 0.0916 |

## Parse cytokine responses in monocytes

Cytokines are proteins that coordinate immune activity. This blood-cell screen predicts CD14-positive and CD16-positive monocyte responses in twelve donor holdouts. All methods in this group use the same capped input cell panel and 2,000 source-selected genes per fold. Native and control-anchored predictions are distinct outputs.

### CD14+ monocytes

Evaluation gene panel: 2,000 genes.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| Replicated-cytokine reliability | — | 0.018915 | 0.094445 | 0.2441 | 0.1803 |
| Source-selected replicated reliability | — | 0.018915 | 0.094445 | 0.2441 | 0.1803 |
| Gaussian context kernel | — | 0.018999 | 0.094784 | 0.2373 | 0.1727 |
| Linear context kernel | — | 0.019008 | 0.094875 | 0.2359 | 0.1714 |
| Source-selected context kernel | — | 0.019009 | 0.094769 | 0.2357 | 0.1714 |
| Two-amplitude context kernel | — | 0.019026 | 0.094835 | 0.2362 | 0.1716 |
| scPerturbMix (fixed-parameter sensitivity) | — | 0.019174 | 0.093835 | 0.2435 | 0.1825 |
| Replicated-gene reliability | — | 0.019181 | 0.094690 | 0.2412 | 0.1797 |
| scPerturbMix | — | 0.019294 | 0.094726 | 0.2431 | 0.1829 |
| Gene reliability | — | 0.019298 | 0.094733 | 0.2426 | 0.1823 |
| Calibrated mean response | — | 0.019302 | 0.094815 | 0.2418 | 0.1821 |
| Global response scaling | — | 0.019302 | 0.094815 | 0.2418 | 0.1821 |
| Perturbation reliability | — | 0.019311 | 0.094808 | 0.2418 | 0.1821 |
| Low-rank response | — | 0.019329 | 0.094864 | 0.2368 | 0.1771 |
| scPerturbMix fixed OP3 parameters | — | 0.019549 | 0.095177 | 0.2441 | 0.1824 |
| Mean source response | — | 0.019831 | 0.096851 | 0.2418 | 0.1821 |
| scGen (control-anchored) | — | 0.020190 | 0.098133 | 0.1571 | 0.1261 |
| No-change control | — | 0.021046 | 0.096086 | — | — |
| scVIDR (original solver, control-anchored) | — | 0.021693 | 0.103248 | 0.1460 | 0.1248 |
| scVIDR (stable solver, control-anchored) | — | 0.021742 | 0.103367 | 0.1451 | 0.1241 |
| scGen | — | 0.022112 | 0.101459 | 0.3605 | 0.3857 |
| scVIDR (original numerical solver) | — | 0.024065 | 0.107494 | 0.3501 | 0.3757 |
| scVIDR (stable solver) | — | 0.024118 | 0.107623 | 0.3495 | 0.3752 |

### CD16+ monocytes

Evaluation gene panel: 2,000 genes.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| Replicated-cytokine reliability | — | 0.023843 | 0.107571 | 0.2477 | 0.1848 |
| Source-selected replicated reliability | — | 0.023843 | 0.107571 | 0.2477 | 0.1848 |
| Gaussian context kernel | — | 0.023911 | 0.107898 | 0.2415 | 0.1787 |
| Linear context kernel | — | 0.023916 | 0.107973 | 0.2404 | 0.1777 |
| Source-selected context kernel | — | 0.023932 | 0.107887 | 0.2400 | 0.1777 |
| Two-amplitude context kernel | — | 0.023933 | 0.107946 | 0.2404 | 0.1777 |
| Replicated-gene reliability | — | 0.024095 | 0.107901 | 0.2434 | 0.1829 |
| scPerturbMix (fixed-parameter sensitivity) | — | 0.024235 | 0.107442 | 0.2431 | 0.1825 |
| Calibrated mean response | — | 0.024340 | 0.108271 | 0.2417 | 0.1822 |
| Global response scaling | — | 0.024340 | 0.108271 | 0.2417 | 0.1822 |
| scPerturbMix | — | 0.024343 | 0.108210 | 0.2428 | 0.1829 |
| Gene reliability | — | 0.024351 | 0.108224 | 0.2424 | 0.1824 |
| Perturbation reliability | — | 0.024361 | 0.108297 | 0.2417 | 0.1822 |
| Low-rank response | — | 0.024368 | 0.108327 | 0.2371 | 0.1776 |
| scPerturbMix fixed OP3 parameters | — | 0.024717 | 0.108808 | 0.2437 | 0.1825 |
| scGen (control-anchored) | — | 0.024836 | 0.110279 | 0.1801 | 0.1420 |
| Mean source response | — | 0.024916 | 0.110142 | 0.2417 | 0.1822 |
| scVIDR (stable solver, control-anchored) | — | 0.025390 | 0.112753 | 0.1771 | 0.1473 |
| scVIDR (original solver, control-anchored) | — | 0.025401 | 0.112766 | 0.1766 | 0.1465 |
| No-change control | — | 0.026446 | 0.110174 | — | — |
| scGen | — | 0.026689 | 0.113715 | 0.3490 | 0.3788 |
| scVIDR (original numerical solver) | — | 0.027593 | 0.116767 | 0.3462 | 0.3751 |
| scVIDR (stable solver) | — | 0.027611 | 0.116787 | 0.3461 | 0.3755 |

## Kang interferon responses in monocytes

Interferon-beta is an immune signal. This study measures blood immune cells from eight people with lupus before and after stimulation. Models predict two monocyte populations in the held-out donor, using the same 2,000 genes per fold. FCGR3A encodes CD16, which identifies the second population.

### CD14+ monocytes

Evaluation gene panel: 2,000 genes.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| scPerturbMix fixed OP3 parameters | — | 0.051356 | 0.139769 | 0.7888 | 0.4359 |
| Perturbation reliability | — | 0.052678 | 0.140905 | 0.7881 | 0.4370 |
| Gene reliability | — | 0.052871 | 0.140584 | 0.7882 | 0.4365 |
| scPerturbMix | — | 0.052871 | 0.140584 | 0.7882 | 0.4365 |
| scVIDR (original numerical solver) | — | 0.053375 | 0.137688 | 0.8039 | 0.5795 |
| scVIDR (stable solver) | — | 0.053393 | 0.137635 | 0.8040 | 0.5794 |
| Mean source response | — | 0.054077 | 0.141531 | 0.7881 | 0.4370 |
| scVIDR (stable solver, control-anchored) | — | 0.054583 | 0.138366 | 0.8044 | 0.5634 |
| scGen | — | 0.055909 | 0.138687 | 0.8083 | 0.5787 |
| Global response scaling | — | 0.056342 | 0.142728 | 0.7881 | 0.4370 |
| Low-rank response | — | 0.056373 | 0.142764 | 0.7880 | 0.4368 |
| scPerturbMix (fixed-parameter sensitivity) | — | 0.067911 | 0.149879 | 0.7893 | 0.4345 |
| CPA (post-warmup, control-anchored) | 8 | 0.079118 | 0.157746 | 0.7571 | 0.4369 |
| CPA | 8 | 0.082858 | 0.155302 | 0.6187 | 0.5166 |
| CPA (control-anchored) | 8 | 0.083636 | 0.160522 | 0.7323 | 0.4140 |
| CPA (post-warmup) | 8 | 0.093255 | 0.160871 | 0.5054 | 0.3835 |
| biolord (control-anchored) | 8 | 0.093568 | 0.169550 | 0.5562 | 0.4693 |
| biolord | 8 | 0.093962 | 0.172178 | 0.5619 | 0.4776 |
| No-change control | — | 0.124769 | 0.182156 | — | — |

### FCGR3A+ monocytes

Evaluation gene panel: 2,000 genes.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| scVIDR (stable solver) | — | 0.038559 | 0.125226 | 0.8091 | 0.6323 |
| scVIDR (original numerical solver) | — | 0.038652 | 0.125421 | 0.8090 | 0.6318 |
| scGen | — | 0.040419 | 0.125964 | 0.8088 | 0.6340 |
| scVIDR (stable solver, control-anchored) | — | 0.041771 | 0.133465 | 0.7992 | 0.5295 |
| scPerturbMix fixed OP3 parameters | — | 0.042364 | 0.137598 | 0.7765 | 0.4393 |
| Perturbation reliability | — | 0.042690 | 0.138029 | 0.7773 | 0.4399 |
| Gene reliability | — | 0.042946 | 0.137986 | 0.7764 | 0.4397 |
| scPerturbMix | — | 0.042946 | 0.137986 | 0.7764 | 0.4397 |
| Mean source response | — | 0.043450 | 0.138544 | 0.7773 | 0.4399 |
| Global response scaling | — | 0.044873 | 0.139648 | 0.7773 | 0.4399 |
| Low-rank response | — | 0.044897 | 0.139677 | 0.7772 | 0.4398 |
| scPerturbMix (fixed-parameter sensitivity) | — | 0.053673 | 0.146808 | 0.7765 | 0.4383 |
| CPA (post-warmup, control-anchored) | 8 | 0.063314 | 0.154657 | 0.7644 | 0.4342 |
| CPA (control-anchored) | 8 | 0.064070 | 0.156058 | 0.7395 | 0.3910 |
| CPA | 8 | 0.068149 | 0.152016 | 0.5869 | 0.4939 |
| CPA (post-warmup) | 8 | 0.077975 | 0.154930 | 0.5042 | 0.4624 |
| biolord (control-anchored) | 8 | 0.079414 | 0.169951 | 0.5715 | 0.4162 |
| biolord | 8 | 0.096413 | 0.177241 | 0.5408 | 0.4783 |
| No-change control | — | 0.102908 | 0.177429 | — | — |

## Wood blood-cell responses with pretrained Stack

This independent blood-cell study exposes donor cells to immune stimuli in two experimental batches. The Stack comparison supplies no stimulated target cells and uses a common 14,748-gene vocabulary and count denominator. Each batch forms a separate target group.

### Batch A

Evaluation gene panel: 14,748 genes.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| Stack-Large-Aligned (control-anchored) | — | 0.089598 | 0.209672 | 0.5128 | 0.3953 |
| Stack-Large-Aligned | — | 0.098221 | 0.218160 | 0.5605 | 0.5504 |
| Calibrated mean response | — | 0.113308 | 0.236042 | 0.2944 | 0.1647 |
| Gaussian context kernel | — | 0.113805 | 0.236920 | 0.2946 | 0.1646 |
| Mean source response | — | 0.118037 | 0.242331 | 0.2944 | 0.1647 |
| Linear context kernel | — | 0.119680 | 0.245135 | 0.2747 | 0.1482 |
| No-change control | — | 0.124607 | 0.245642 | — | — |

### Batch B

Evaluation gene panel: 14,748 genes.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| Linear context kernel | — | 0.051891 | 0.158203 | 0.1867 | 0.1479 |
| Stack-Large-Aligned (control-anchored) | — | 0.052368 | 0.160703 | 0.2510 | 0.1781 |
| Gaussian context kernel | — | 0.052708 | 0.159758 | 0.1785 | 0.1473 |
| Calibrated mean response | — | 0.052771 | 0.159654 | 0.1734 | 0.1434 |
| No-change control | — | 0.053644 | 0.158862 | — | — |
| Mean source response | — | 0.058438 | 0.171724 | 0.1734 | 0.1434 |
| Stack-Large-Aligned | — | 0.101268 | 0.229656 | 0.3743 | 0.3662 |

## sci-Plex3 drug-dose interpolation

This chemical screen measures drug responses in lung cancer, leukaemia and breast cancer cell lines. Models predict 54 held-out intermediate-dose conditions on a fixed 512-gene panel. GPerturb and State use task-specific dose adaptations. State is trained from scratch.

### All held-out dose conditions

Evaluation gene panel: 512 genes.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| scPerturbMix dose model | 54 | 0.007270 | 0.040597 | 0.5525 | 0.3713 |
| Low-rank dose interpolation | 54 | 0.007375 | 0.040485 | 0.5532 | 0.3786 |
| Scaled log-dose interpolation | 54 | 0.007451 | 0.040112 | 0.5577 | 0.3855 |
| Shrunken dose interpolation | 54 | 0.007637 | 0.040999 | 0.5558 | 0.3734 |
| Log-dose interpolation | 54 | 0.008428 | 0.041873 | 0.5577 | 0.3855 |
| GPerturb (dose adaptation) | 54 | 0.010380 | 0.048503 | 0.3624 | 0.2580 |
| State (dose adaptation, from scratch) | 54 | 0.011691 | 0.050284 | 0.5398 | 0.3514 |

## sci-Plex2 dense drug-dose interpolation

This experiment measures lung cancer cells exposed to four drugs over a dense concentration series. Models predict seven eligible held-out conditions across 32,418 genes. Six conditions interpolate measured source doses, and one condition extrapolates beyond the eligible source doses.

### All held-out conditions

Evaluation gene panel: 32,418 genes.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| Selected hybrid dose response | 7 | 0.091080 | 0.198912 | 0.7533 | 0.6834 |
| Dose model without low-rank responses | 7 | 0.091180 | 0.199538 | 0.7421 | 0.6667 |
| Dose model without variance weighting | 7 | 0.091180 | 0.199538 | 0.7421 | 0.6667 |
| Scaled log-dose response | 7 | 0.091180 | 0.199538 | 0.7421 | 0.6667 |
| Variance-weighted low-rank dose response | 7 | 0.091180 | 0.199538 | 0.7421 | 0.6667 |
| Log-transformed dose response | 7 | 0.092506 | 0.196859 | 0.7421 | 0.6667 |
| Linear-dose response | 7 | 0.092805 | 0.197773 | 0.7359 | 0.6614 |
| Log-dose response | 7 | 0.093655 | 0.197613 | 0.7411 | 0.6655 |
| Saturating dose response | 7 | 0.095583 | 0.202748 | 0.7458 | 0.6820 |
| Nearest measured dose | 7 | 0.116417 | 0.218147 | 0.7112 | 0.6323 |
| Highest measured dose | 7 | 0.128436 | 0.229637 | 0.6978 | 0.6204 |
| No-change control | 7 | 0.222314 | 0.299139 | — | — |

## PerturbFate genetic responses across drug environments

This melanoma experiment combines gene repression with an anticancer drug. The task supplies each evaluation gene’s response under the vehicle condition and predicts its response under drug treatment. It is evaluated on 26,357 genes.

### All held-out conditions

Evaluation gene panel: 26,357 genes.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| Reduced-rank response | 27 | 0.280323 | 0.389799 | 0.2900 | 0.2713 |
| scPerturbMix conditional genetic model | 27 | 0.280323 | 0.389799 | 0.2900 | 0.2713 |
| Matched PCA-ridge | 27 | 0.280388 | 0.389829 | 0.2895 | 0.2709 |
| PCA-ridge | 27 | 0.280388 | 0.389829 | 0.2895 | 0.2709 |
| Expression kernel ridge | 27 | 0.280516 | 0.389944 | 0.2898 | 0.2709 |
| Mean genetic effect under vemurafenib | 27 | 0.281021 | 0.390343 | 0.2886 | 0.2696 |
| Scaled vehicle genetic effect | 27 | 0.281021 | 0.390343 | 0.2886 | 0.2696 |
| Drug-environment control | 27 | 0.304503 | 0.401472 | — | — |
| Noise-aware low-rank interaction | 27 | 0.487962 | 0.485460 | 0.1153 | 0.1261 |
| Low-rank interaction | 27 | 0.487974 | 0.485468 | 0.1153 | 0.1261 |
| Shared interaction offset | 27 | 0.488230 | 0.485563 | 0.1152 | 0.1261 |
| Additive response | 27 | 0.530139 | 0.518258 | 0.0073 | 0.0250 |

## Glioblastoma expression prediction

This brain-tumour experiment combines gene repression and drug treatment in glioblastoma cell lines. The development task predicts full expression profiles on a 512-gene panel. Pretrained gene embeddings and random embeddings use matched ridge-response heads.

### All held-out conditions

Evaluation gene panel: 512 genes.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| Without crossed interactions | 4647 | 0.056403 | 0.108335 | 0.3854 | 0.6640 |
| Without gene-level response | 4647 | 0.056403 | 0.108335 | 0.3854 | 0.6640 |
| scPerturbMix expression model | 4647 | 0.056403 | 0.108335 | 0.3854 | 0.6640 |
| Background-only model | 4647 | 0.056483 | 0.108616 | 0.3854 | 0.6648 |
| Without drug-dose response | 4647 | 0.056483 | 0.108616 | 0.3854 | 0.6648 |
| Without context adjustment | 4647 | 0.056817 | 0.105652 | 0.3855 | 0.6642 |
| Source-location-only model | 4647 | 0.056880 | 0.106042 | 0.3854 | 0.6648 |
| Mean source expression | 4647 | 0.056904 | 0.105791 | 0.3853 | 0.6645 |
| scGPT contextual embeddings with ridge | 4647 | 0.056916 | 0.107356 | 0.3696 | 0.6477 |
| Nicheformer gene embeddings with ridge | 4647 | 0.057326 | 0.105319 | 0.3744 | 0.6550 |
| scGPT gene embeddings with ridge | 4647 | 0.057399 | 0.105345 | 0.3722 | 0.6539 |
| Ridge expression model | 4647 | 0.057408 | 0.105243 | 0.3694 | 0.6365 |
| Random gene embeddings with ridge | 4647 | 0.057481 | 0.105606 | 0.3710 | 0.6525 |
| One-hot gene encoding with ridge | 4647 | 0.057742 | 0.105520 | 0.3656 | 0.6489 |
| Selective response shrinkage | 4647 | 0.059997 | 0.131817 | 0.0955 | 0.1487 |
| Drug-dose mean response | 4647 | 0.060004 | 0.131894 | 0.0949 | 0.1478 |
| Invariant low-rank response (rank 16) | 4647 | 0.060205 | 0.131848 | 0.0924 | 0.1440 |
| Ridge response model | 4647 | 0.060537 | 0.132530 | 0.0853 | 0.1325 |
| Untreated target mean | 4647 | 0.061276 | 0.143907 | — | — |

## Glioblastoma paired drug-response prediction

This task uses the same glioblastoma study to predict paired treatment-induced changes on the 512-gene panel. Full-expression prediction and drug-response prediction measure different aspects of model performance.

### All held-out conditions

Evaluation gene panel: 512 genes.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| Nicheformer gene embeddings with ridge | 4125 | 0.105065 | 0.153625 | 0.0511 | 0.0737 |
| scGPT contextual embeddings with ridge | 4125 | 0.105069 | 0.153642 | 0.0507 | 0.0733 |
| Random gene embeddings with ridge | 4125 | 0.105082 | 0.153508 | 0.0504 | 0.0731 |
| scGPT gene embeddings with ridge | 4125 | 0.105082 | 0.153515 | 0.0503 | 0.0732 |
| One-hot gene encoding with ridge | 4125 | 0.105082 | 0.153484 | 0.0504 | 0.0733 |
| Ridge expression model | 4125 | 0.105091 | 0.155014 | 0.0440 | 0.0598 |
| scPerturbMix expression model | 4125 | 0.105335 | 0.151589 | 0.0406 | 0.0541 |
| Mean source expression | 4125 | 0.105830 | 0.148839 | — | — |

## Immune Dictionary in vivo cytokine responses

This independent mouse study measures immune-cell gene expression in lymph nodes after cytokine stimulation. Six lymphoid populations provide source responses. The authors’ population analysis objects contain 117,282 cells. The fixed fitting rule is refitted to mouse source data and predicts 438 eligible conditions in six macrophage or dendritic-cell populations. The 83 source-complete cytokines include 82 represented among the target conditions.

### Macrophage subpopulation

Evaluation gene panel: 2,000 genes.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| Low-rank response | 31 | 0.050216 | 0.164876 | 0.1038 | 0.0679 |
| scPerturbMix | 31 | 0.050288 | 0.165135 | 0.1096 | 0.0702 |
| Cross-context programme basis | 31 | 0.050343 | 0.165246 | 0.1067 | 0.0683 |
| Gene reliability | 31 | 0.050344 | 0.165281 | 0.1065 | 0.0707 |
| Perturbation reliability | 31 | 0.050393 | 0.165507 | 0.1048 | 0.0708 |
| Global response scaling | 31 | 0.050419 | 0.165278 | 0.1048 | 0.0708 |
| Unchanged control | 31 | 0.052176 | 0.165506 | — | — |
| Mean source response | 31 | 0.052768 | 0.170443 | 0.1048 | 0.0708 |

### CD103+ dendritic cells

Evaluation gene panel: 2,000 genes.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| scPerturbMix | 82 | 0.012673 | 0.081027 | 0.2574 | 0.1306 |
| Cross-context programme basis | 82 | 0.012694 | 0.081028 | 0.2511 | 0.1290 |
| Low-rank response | 82 | 0.012694 | 0.081343 | 0.2400 | 0.1190 |
| Gene reliability | 82 | 0.012761 | 0.081137 | 0.2311 | 0.1217 |
| Global response scaling | 82 | 0.012768 | 0.081732 | 0.2215 | 0.1219 |
| Perturbation reliability | 82 | 0.012846 | 0.081449 | 0.2215 | 0.1219 |
| Unchanged control | 82 | 0.013532 | 0.080630 | — | — |
| Mean source response | 82 | 0.015025 | 0.090040 | 0.2215 | 0.1219 |

### Conventional and CD209+ dendritic cells

Evaluation gene panel: 2,000 genes.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| scPerturbMix | 82 | 0.016911 | 0.094276 | 0.3110 | 0.1858 |
| Cross-context programme basis | 82 | 0.017008 | 0.094536 | 0.3011 | 0.1790 |
| Low-rank response | 82 | 0.017195 | 0.094819 | 0.2943 | 0.1750 |
| Gene reliability | 82 | 0.017265 | 0.095108 | 0.2751 | 0.1607 |
| Perturbation reliability | 82 | 0.017336 | 0.095279 | 0.2660 | 0.1615 |
| Global response scaling | 82 | 0.017589 | 0.095892 | 0.2660 | 0.1615 |
| Mean source response | 82 | 0.018473 | 0.100367 | 0.2660 | 0.1615 |
| Unchanged control | 82 | 0.020074 | 0.098525 | — | — |

### Migratory dendritic subpopulation

Evaluation gene panel: 2,000 genes.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| Unchanged control | 81 | 0.013434 | 0.084122 | — | — |
| Global response scaling | 81 | 0.014196 | 0.088274 | 0.0786 | 0.0423 |
| Low-rank response | 81 | 0.014353 | 0.088315 | 0.0729 | 0.0366 |
| Gene reliability | 81 | 0.014444 | 0.087983 | 0.0828 | 0.0422 |
| Perturbation reliability | 81 | 0.014486 | 0.088260 | 0.0786 | 0.0423 |
| Cross-context programme basis | 81 | 0.014536 | 0.088225 | 0.0838 | 0.0417 |
| scPerturbMix | 81 | 0.014635 | 0.088548 | 0.0800 | 0.0390 |
| Mean source response | 81 | 0.017681 | 0.098655 | 0.0786 | 0.0423 |

### Langerhans cells

Evaluation gene panel: 2,000 genes.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| Unchanged control | 82 | 0.016244 | 0.093606 | — | — |
| Global response scaling | 82 | 0.016446 | 0.095656 | 0.1244 | 0.0741 |
| Low-rank response | 82 | 0.016539 | 0.095521 | 0.1273 | 0.0698 |
| Cross-context programme basis | 82 | 0.016764 | 0.095566 | 0.1403 | 0.0787 |
| scPerturbMix | 82 | 0.016779 | 0.095630 | 0.1397 | 0.0767 |
| Gene reliability | 82 | 0.016797 | 0.095642 | 0.1302 | 0.0734 |
| Perturbation reliability | 82 | 0.016837 | 0.095872 | 0.1244 | 0.0741 |
| Mean source response | 82 | 0.019473 | 0.104326 | 0.1244 | 0.0741 |

### Plasmacytoid dendritic cells

Evaluation gene panel: 2,000 genes.

| Model | Conditions | MSE ↓ | MAE ↓ | Response Pearson ↑ | Response Spearman ↑ |
| --- | --- | --- | --- | --- | --- |
| Low-rank response | 80 | 0.016174 | 0.095981 | 0.1986 | 0.1162 |
| scPerturbMix | 80 | 0.016210 | 0.095867 | 0.2113 | 0.1249 |
| Cross-context programme basis | 80 | 0.016238 | 0.095886 | 0.2051 | 0.1214 |
| Global response scaling | 80 | 0.016286 | 0.096496 | 0.1826 | 0.1136 |
| Gene reliability | 80 | 0.016351 | 0.096147 | 0.1894 | 0.1134 |
| Perturbation reliability | 80 | 0.016390 | 0.096346 | 0.1826 | 0.1136 |
| Unchanged control | 80 | 0.017194 | 0.096732 | — | — |
| Mean source response | 80 | 0.018441 | 0.103174 | 0.1826 | 0.1136 |

## Reading model settings

Native outputs are model-generated treated profiles. Control-anchored outputs add the generated treated-minus-control response to the measured target-control mean. Frozen encoder adaptations train a response head while preserving the encoder weights. Fine-tuned adaptations update the stated encoder layers. Random controls use the same architecture with random weights, with their training or freezing convention recorded in the model name and [encoder guide](benchmark_evidence.md#encoder-comparison).

Both Geneformer V2 rows use source-selected pooling. Its official default uses the penultimate-layer classification-token representation. Source selection also considers mean pooling of final-layer gene tokens. The encoder guide identifies the representation selected in each setting. This adds a selection dimension to the V2 experiment.

The downloadable metrics retain additional endpoints, including gene-set responses, large-response-gene recovery and cell-distribution distances where available. [Mechanism comparisons](mechanism_evidence.md) and the [mouse cytokine evaluation](external_validation.md) explain the associated component and external-study experiments.
