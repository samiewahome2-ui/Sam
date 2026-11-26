import unittest
from evaluate import score

class EvaluationTests(unittest.TestCase):
    def test_pass(self):
        self.assertEqual(score(dict(accuracy=2, adherence=2, clarity=1, critical="no")), (5, "PASS"))

    def test_override(self):
        self.assertEqual(score(dict(accuracy=2, adherence=2, clarity=2, critical="yes")), (6, "REVIEW"))

    def test_invalid_rating(self):
        with self.assertRaises(ValueError):
            score(dict(accuracy=3, adherence=2, clarity=2, critical="no"))

if __name__ == "__main__":
    unittest.main()
