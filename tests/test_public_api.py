import unittest
from pathlib import Path
import numpy as np
from scperturbmix import predict_response


class PublicInterfaceTests(unittest.TestCase):
    def test_public_api_replays_programme_model(self):
        root = Path(__file__).resolve().parents[1]
        with np.load(root / 'tests/program_reference.npz', allow_pickle=False) as z:
            r = {key: z[key] for key in z.files}
        predicted, effect, genes = predict_response(
            r['control'], r['gene_ids'], r['compounds'], r['doses_uM'],
            r['times_hours'], root / 'models/response_transfer/op3_programs')
        np.testing.assert_allclose(predicted, r['prediction'], rtol=0, atol=1e-12)


if __name__ == '__main__':
    unittest.main()
