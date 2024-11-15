import unittest
from unittest.mock import MagicMock
from FinanceTracker import FinanceTracker
from Expense import Expense

class TestFinanceTracker(unittest.TestCase):

    def setUp(self):
        self.tracker = FinanceTracker()
        self.expense = Expense(amount="100", category="Food", date="2024-11-14")

    def test_log_expense(self):
        self.tracker.log_expense(self.expense)
        self.assertIn(self.expense, self.tracker.expenses)
    
    def test_set_budget(self):
        self.tracker.set_budget("Food", "500")
        self.assertEqual(self.tracker.budgets["Food"], 500)

    def test_show_summary(self):
        self.tracker.log_expense(self.expense)
        self.tracker.set_budget("Food", "500")
        
        summary = self.tracker.show_summary()
        self.assertIn("100", summary)  # Verifying that the expense amount is in the summary
        self.assertIn("Food", summary)  # Verifying that the category is in the summary

if __name__ == '__main__':
    unittest.main()
