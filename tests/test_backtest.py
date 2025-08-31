import unittest
from backtests.backtest_v1 import run_moving_average_backtest

class TestBacktest(unittest.TestCase):
    def test_moving_average_crossover(self):
        
        price_data = [10, 11, 12, 11, 10, 11, 12, 13, 14, 15, 14, 13, 12, 11]
        
        expected_final_value = 1000
        
        final_value = run_moving_average_backtest(price_data)
        
        self.assertEqual(final_value, expected_final_value)

if __name__ == '__main__':
    unittest.main()        