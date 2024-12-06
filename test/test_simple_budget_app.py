import unittest
from unittest.mock import MagicMock, patch
import tkinter as tk
from tkinter import messagebox
from SimpleBudgetApp import SimpleBudgetApp
from Expense import Expense
from FinanceTracker import FinanceTracker
class TestSimpleBudgetApp(unittest.TestCase):
    @patch('SimpleBudgetApp.FinanceTracker')  # Mock FinanceTracker
    @patch('SimpleBudgetApp.Expense')  # Mock Expense
    def setUp(self, MockExpense, MockFinanceTracker):
        self.root = tk.Tk()
        self.app = SimpleBudgetApp(self.root)
        
        self.mock_tracker = MockFinanceTracker.return_value
        self.mock_expense = MockExpense.return_value
        self.mock_tracker.log_expense = MagicMock()
        self.mock_tracker.set_budget = MagicMock()
        self.mock_tracker.show_summary = MagicMock(return_value="Summary: $100 spent.")
        
        self.mock_expense.amount = 100
        self.mock_expense.category = "Food"
        self.mock_expense.date = "2024-11-14"
    def test_log_expense_valid_input(self):
        self.app.expense_entry.insert(0, "100")
        self.app.category_var.set("Food")
        self.app.date_entry.insert(0, "2024-11-14")
        
        self.app.log_expense()
        
        self.mock_tracker.log_expense.assert_called_once_with(self.mock_expense)
        self.assertEqual(self.app.expense_display.cget("text"), f"Logged Expense: {self.mock_expense}")
    def test_log_expense_invalid_amount(self):
        self.app.expense_entry.insert(0, "")
        self.app.category_var.set("Food")
        self.app.date_entry.insert(0, "2024-11-14")
        
        with patch.object(messagebox, 'showerror') as mock_messagebox:
            self.app.log_expense()
            mock_messagebox.assert_called_with("Input Error", "Amount and Category are required fields.")
    def test_set_budget_valid_input(self):
        self.app.budget_entry.insert(0, "500")
        self.app.budget_category_var.set("Food")
        
        self.app.set_budget()
        
        self.mock_tracker.set_budget.assert_called_once_with("Food", "500")
        
        with patch.object(messagebox, 'showinfo') as mock_messagebox:
            mock_messagebox.assert_called_with("Budget Set", "Budget for Food set to $500.")
    def test_set_budget_invalid_input(self):
        self.app.budget_entry.insert(0, "")
        self.app.budget_category_var.set("Food")
        
        with patch.object(messagebox, 'showerror') as mock_messagebox:
            self.app.set_budget()
            mock_messagebox.assert_called_with("Input Error", "Category and Budget Limit are required fields.")
    def test_show_summary(self):
        self.app.show_summary()
        
        self.mock_tracker.show_summary.assert_called_once()
        self.assertEqual(self.app.expense_display.cget("text"), "Summary: $100 spent.")
if __name__ == '__main__':
    unittest.main()