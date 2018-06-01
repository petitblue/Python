import unittest
import grading1

class TestGrading(unittest.TestCase):
    def test_is_passing(self):
        self.assertTrue(grading1.is_pass(85))
        self.assertFalse(grading1.is_pass(60))
        self.assertTrue(grading1.is_pass(70))
