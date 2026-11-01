"""Validate the registered-condition API against independent study predictions."""
import unittest
from pathlib import Path
import numpy as np
from scperturbmix import predict_conditions, predict_response

ROOT=Path(__file__).resolve().parents[1]

class RegisteredConditionTests(unittest.TestCase):
    def setUp(self):
        with np.load(ROOT/'tests/immune_reference.npz',allow_pickle=False) as z:
            self.ref={k:z[k] for k in z.files}
        self.model=ROOT/'models/response_transfer/immune_dictionary'

    def test_independent_prediction_replay_and_axis_order(self):
        r=self.ref
        actual=predict_conditions(r['control'],r['gene_ids'],r['condition_ids'],self.model)[0]
        np.testing.assert_allclose(actual,r['prediction'],rtol=0,atol=1e-12)
        order=np.arange(len(r['gene_ids']))[::-1]
        reordered=predict_conditions(r['control'][::-1,order],r['gene_ids'][order],r['condition_ids'][::-1],self.model)[0]
        np.testing.assert_array_equal(reordered,actual[::-1])

    def test_shared_control_and_condition_specific_controls(self):
        r=self.ref
        one=predict_conditions(r['control'][0],r['gene_ids'],r['condition_ids'],self.model)
        many=predict_conditions(np.tile(r['control'][0],(3,1)),r['gene_ids'],r['condition_ids'],self.model)
        np.testing.assert_array_equal(one[0],many[0])
        np.testing.assert_array_equal(one[1],many[1])

    def test_dose_schema_and_input_errors(self):
        r=self.ref
        with self.assertRaisesRegex(ValueError,'condition IDs'):
            predict_response(r['control'][0],r['gene_ids'],['IL2'],[5],[4],self.model)
        with self.assertRaisesRegex(ValueError,'drug, dose and time'):
            predict_conditions(r['control'],r['gene_ids'],r['condition_ids'],ROOT/'models/response_transfer/op3')
        for conditions in ([],['unknown cytokine']):
            with self.assertRaises(ValueError):predict_conditions(r['control'][0],r['gene_ids'],conditions,self.model)
        for ctl,genes in [(r['control'][:,:-1],r['gene_ids'][:-1]),
                          (np.full_like(r['control'],np.nan),r['gene_ids']),
                          (r['control'],np.repeat(r['gene_ids'][0],len(r['gene_ids'])) )]:
            with self.assertRaises(ValueError):predict_conditions(ctl,genes,r['condition_ids'],self.model)

if __name__=='__main__':unittest.main()
