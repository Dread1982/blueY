import unittest
import by_scikit_learn


class MyTestCase(unittest.TestCase):
    def test_get_mae_with_linear_regression(self):
        X, y = by_scikit_learn.get_dataset()

        mae = by_scikit_learn.get_mae_with_linear_regression(X, y)

        self.assertAlmostEqual(2.79752479362, mae)

    def test_get_mae_with_scale_and_linear_regression(self):
        X, y = by_scikit_learn.get_dataset()

        mae = by_scikit_learn.get_mae_with_scale_and_linear_regression(X, y)

        self.assertAlmostEqual(2.79752479362, mae)

if __name__ == '__main__':
    unittest.main()
