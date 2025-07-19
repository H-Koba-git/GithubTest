#!/usr/bin/env python3
"""
掛け算プログラムのテスト
"""

import unittest
from multiply import multiply

class TestMultiply(unittest.TestCase):
    """掛け算関数のテストクラス"""
    
    def test_positive_numbers(self):
        """正の数の掛け算テスト"""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(5, 7), 35)
        self.assertEqual(multiply(10, 10), 100)
    
    def test_negative_numbers(self):
        """負の数の掛け算テスト"""
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(2, -3), -6)
        self.assertEqual(multiply(-2, -3), 6)
    
    def test_zero(self):
        """ゼロとの掛け算テスト"""
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, 0), 0)
    
    def test_decimal_numbers(self):
        """小数の掛け算テスト"""
        # 浮動小数点数の精度問題を避けるため、assertAlmostEqualを使用
        self.assertAlmostEqual(multiply(2.5, 2), 5.0, places=10)
        self.assertAlmostEqual(multiply(1.5, 3), 4.5, places=10)
        self.assertAlmostEqual(multiply(0.1, 0.1), 0.01, places=10)
        self.assertAlmostEqual(multiply(0.3, 0.3), 0.09, places=10)

if __name__ == "__main__":
    unittest.main() 