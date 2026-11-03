"""Exercise the documented real-data workflow against independently scored results."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / 'examples/immune_dictionary'
spec = importlib.util.spec_from_file_location('real_cytokine_example', EXAMPLE / 'run.py')
example = importlib.util.module_from_spec(spec)
spec.loader.exec_module(example)


class RealExampleTests(unittest.TestCase):
    def test_observed_profiles_reproduce_reported_metrics(self):
        with tempfile.TemporaryDirectory() as temporary:
            result = example.evaluate(EXAMPLE / 'observed_profiles.npz',
                                      ROOT / 'models/response_transfer/immune_dictionary', Path(temporary))
            expected = json.loads((EXAMPLE / 'expected_summary.json').read_text())
            self.assertEqual([x['model'] for x in result], [x['model'] for x in expected])
            for actual, reference in zip(result, expected):
                self.assertEqual(actual['conditions'], 438)
                for metric in ['mse', 'mae', 'response_pearson']:
                    if reference[metric] is None:
                        self.assertIsNone(actual[metric])
                    else:
                        self.assertAlmostEqual(actual[metric], reference[metric], places=10)
            with np.load(Path(temporary) / 'predictions.npz', allow_pickle=False) as output:
                self.assertEqual(output['prediction'].shape, (438, 2000))
                self.assertEqual(len(set(output['population'])), 6)

    def test_response_metric_uses_control_contrast_and_handles_zero_effect(self):
        measured = np.array([[1., -1., 2.], [-2., 3., 1.]])
        mse, mae, correlation = example.score(measured, measured)
        np.testing.assert_allclose(mse, 0)
        np.testing.assert_allclose(mae, 0)
        np.testing.assert_allclose(correlation, 1)
        _, _, zero_correlation = example.score(measured, np.zeros_like(measured))
        self.assertTrue(np.isnan(zero_correlation).all())


if __name__ == '__main__':
    unittest.main()
