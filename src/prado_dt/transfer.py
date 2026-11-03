"""CPU inference for fitted scPerturbMix response models."""
import argparse,csv,json
from pathlib import Path
import numpy as np

def _predict_indices(control,gene_ids,indices,directory,meta):
    genes=list(map(str,gene_ids));expected=meta['gene_ids'];n=len(indices)
    if not n:raise ValueError('Supply at least one condition.')
    if len(set(genes))!=len(genes) or set(genes)!=set(expected):raise ValueError('Control gene identities must match the model exactly and be unique.')
    control=np.asarray(control,float)
    if control.shape not in [(len(genes),),(n,len(genes))] or not np.isfinite(control).all():raise ValueError('Provide one finite control vector, or one per condition.')
    order=[genes.index(g) for g in expected];control=control[...,order]
    with np.load(directory/'model.npz',allow_pickle=False) as a:
        p=a['mean_effect'][indices];v=a['between_context_variance_of_mean'][indices]
        program={k:a[k] for k in ['program_basis','program_mean','program_variance']} if 'program_parameters' in meta else None
    c=meta['selected_parameters'];t=c['reliability'];mix=c['gene_gate_mix'];signal=p*p
    if t==0:effect=c['scale']*p
    else:
        compound=signal.mean(1)/(signal.mean(1)+t*v.mean(1)+1e-12)
        gene=signal/(signal+t*v+1e-12)
        effect=c['scale']*((1-mix)*compound[:,None]+mix*gene)*p
    if program is not None:
        pc=meta['program_parameters'];rank=pc['rank'];u=program['program_basis'][:,:rank]
        pm=program['program_mean'][indices,:rank];pv=program['program_variance'][indices,:rank]
        def unscaled(mean,variance,penalty,mixture):
            if penalty==0:return mean
            square=mean*mean
            cg=square.mean(1)/(square.mean(1)+penalty*variance.mean(1)+1e-12)
            gg=square/(square+penalty*variance+1e-12)
            return ((1-mixture)*cg[:,None]+mixture*gg)*mean
        gene_effect=unscaled(p,v,t,mix)
        program_effect=unscaled(pm,pv,pc['program_reliability'],pc['program_gate_mix'])@u.T
        effect=pc['scale']*((1-pc['program_blend'])*gene_effect+pc['program_blend']*program_effect)
    return control+effect,effect,np.asarray(expected)

def predict(control,gene_ids,compounds,doses_uM,times_hours,model_dir):
    """Predict registered drug conditions with doses in micromolar and times in hours."""
    directory=Path(model_dir);meta=json.loads((directory/'model.json').read_text())
    if meta.get('condition_schema','drug_dose_time')!='drug_dose_time':
        raise ValueError('This model uses condition IDs. Use predict_conditions with its registered condition IDs.')
    n=len(compounds)
    if not n or len(doses_uM)!=n or len(times_hours)!=n:raise ValueError('Supply equal, nonempty condition lists.')
    lookup={(d['drug'].casefold(),float(d['dose_uM']),float(d['time_hours'])):i for i,d in enumerate(meta['conditions'])}
    indices=[]
    for drug,dose,time in zip(compounds,doses_uM,times_hours):
        key=(str(drug).casefold(),float(dose),float(time))
        if key not in lookup:raise ValueError('Unsupported drug, dose or time: '+str(key))
        indices.append(lookup[key])
    return _predict_indices(control,gene_ids,indices,directory,meta)

def predict_conditions(control,gene_ids,condition_ids,model_dir):
    """Predict registered conditions without converting their physical dose units.

    Conditions must match the model catalogue exactly. Supply one untreated
    expression vector or a matrix with one matched control per requested condition.
    Returns predicted expression, response effects, and genes in model order.
    """
    directory=Path(model_dir);meta=json.loads((directory/'model.json').read_text())
    if meta.get('condition_schema')!='condition_id':
        raise ValueError('This model uses drug, dose and time. Use predict_response.')
    lookup={str(d['condition_id']):i for i,d in enumerate(meta['conditions'])}
    if len(lookup)!=len(meta['conditions']):raise ValueError('Model condition IDs must be unique.')
    indices=[]
    for condition in condition_ids:
        key=str(condition)
        if key not in lookup:raise ValueError('Unsupported condition ID: '+key)
        indices.append(lookup[key])
    return _predict_indices(control,gene_ids,indices,directory,meta)

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--model-dir',required=True)
    p.add_argument('--control',required=True);p.add_argument('--conditions',required=True);p.add_argument('--output',required=True);a=p.parse_args()
    with open(a.control) as f:ctl=list(csv.DictReader(f))
    with open(a.conditions) as f:cond=list(csv.DictReader(f))
    ids=[r['condition_id'] for r in cond]
    if len(set(ids))!=len(ids):raise ValueError('Condition IDs must be unique.')
    meta=json.loads((Path(a.model_dir)/'model.json').read_text())
    control=[float(r['expression']) for r in ctl];gene_ids=[r['gene_id'] for r in ctl]
    if meta.get('condition_schema')=='condition_id':
        prediction,effect,genes=predict_conditions(control,gene_ids,ids,a.model_dir)
    else:
        prediction,effect,genes=predict(control,gene_ids,[r['drug'] for r in cond],
            [float(r['dose_uM']) for r in cond],[float(r['time_hours']) for r in cond],a.model_dir)
    np.savez_compressed(a.output,prediction=prediction,effect=effect,gene_ids=genes,condition_id=np.asarray(ids))
    print('Saved '+str(len(prediction))+' predicted conditions.')
if __name__=='__main__':main()
