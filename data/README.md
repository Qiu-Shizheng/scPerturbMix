# Input data

Download experimental expression matrices from the original publication or GEO record and keep them outside version control. scPerturbMix includes fitted model parameters and example inputs.

For H5AD mode, the expression matrix is `adata.X` and the observation table must contain:

- a perturbation identifier (`perturbation`, `perturbation_name`, `condition` or `gRNA`);
- a cell-line or environment identifier (`cell_line`, `celltype`, `cell_type` or `line`);
- optional `drug`, `dose` and `time` columns. Missing values use explicit defaults.

Untreated context is defined from non-targeting/control rows at zero dose (`NTC`, `control`, `vehicle`, `non-targeting` or `random_region`). The held-out environment's treated labels are used only for the final evaluation.
