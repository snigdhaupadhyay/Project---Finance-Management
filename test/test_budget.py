import unittest
from Budget import Budget  # Assuming Budget is a separate class

class TestBudget(unittest.TestCase):

    def setUp(self):
        self.budget = Budget(category="Food", limit=500)

    def test_budget_limit(self):
        self.assertEqual(self.budget.limit, 500)

    def test_exceed_budget(self):
        self.budget.add_expense(600)
        self.assertTrue(self.budget.is_exceeded())  # Assuming a method `is_exceeded` exists
    
if __name__ == '__main__':
    unittest.main()
