# -*- coding: utf-8 -*-
import unittest
import sample

class SampleTest(unittest.TestCase):
    def setUp(self):
        self.util = sample.IntUtil()
    def test_twice(self):
        # 足した数と同値か
        import random
        roop = 0
        while roop != 10000:
            n = random.randint(0, 100)
            ans = n + n
            self.assertEqual(self.util.twice(n), ans)
            roop += 1

if __name__ == '__main__':
    unittest.main()
