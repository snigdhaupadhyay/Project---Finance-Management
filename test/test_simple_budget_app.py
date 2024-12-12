import unittest
from unittest.mock import MagicMock, patch
from tkinter import Tk
from SimpleBudgetApp import SimpleBudgetApp
from FinanceTracker import FinanceTracker
from Expense import Expense
from tkinter import messagebox

class TestSimpleBudgetApp(unittest.TestCase):

    @patch.object(FinanceTracker, 'log_expense')
    @patch.object(FinanceTracker, 'get_budget')
    @patch.object(messagebox, 'showinfo')
    def test_log_expense_valid(self, mock_showinfo, mock_get_budget, mock_log_expense):
        root = Tk()
        app = SimpleBudgetApp(root)

        # Mock the get_budget to return a valid budget
        mock_get_budget.return_value = {"limit": 200.0}

        # Set the values in the UI
        app.expense_entry.insert(0, "50.0")
        app.category_var.set("Food")
        app.date_entry.set_date("2024-12-12")

        # Call log_expense function
        app.log_expense()

        # Check if the log_expense was called once and the message was shown
        mock_log_expense.assert_called_once()
        mock_showinfo.assert_called_once_with("Success", "Expense logged successfully!")

        # Clean up
        root.destroy()

    @patch.object(FinanceTracker, 'log_expense')
    @patch.object(messagebox, 'showerror')
    def test_log_expense_invalid_amount(self, mock_showerror, mock_log_expense):
        root = Tk()
        app = SimpleBudgetApp(root)

        # Set invalid amount
        app.expense_entry.insert(0, "invalid_amount")
        app.category_var.set("Food")
        app.date_entry.set_date("2024-12-12")

        # Call log_expense function
        app.log_expense()

        # Ensure error message is shown
        mock_showerror.assert_called_once_with("Input Error", "Amount must be a valid number.")
        mock_log_expense.assert_not_called()

        # Clean up
        root.destroy()

    @patch.object(FinanceTracker, 'set_budget')
    @patch.object(messagebox, 'showinfo')
    def test_set_budget_valid(self, mock_showinfo, mock_set_budget):
        root = Tk()
        app = SimpleBudgetApp(root)

        # Mock set_budget to return success
        mock_set_budget.return_value = 2

        # Set the values in the UI
        app.budget_entry.insert(0, "500.0")
        app.budget_category_var.set("Food")

        # Call set_budget function
        app.set_budget()

        # Check if the set_budget was called and message is shown
        mock_set_budget.assert_called_once_with("Food", 500.0)
        mock_showinfo.assert_called_once_with("Budget Set", "Set new budget for Food to $500.0.")

        # Clean up
        root.destroy()

    @patch.object(FinanceTracker, 'get_budget')
    @patch.object(messagebox, 'showerror')
    def test_get_budget_no_category(self, mock_showerror, mock_get_budget):
        root = Tk()
        app = SimpleBudgetApp(root)

        # Set category to default value (Select Category)
        app.budget_category_var.set("Select Category")

        # Call get_budget function
        app.get_budget()

        # Ensure that get_budget was called and no error was raised
        mock_get_budget.assert_called_once()
        mock_showerror.assert_not_called()

        # Clean up
        root.destroy()

    @patch.object(FinanceTracker, 'show_summary')
    @patch.object(messagebox, 'showerror')
    def test_show_summary_valid(self, mock_showerror, mock_show_summary):
        root = Tk()
        app = SimpleBudgetApp(root)

        # Mock show_summary to return a valid summary
        mock_show_summary.return_value = [
            {"_id": "Food", "total_amount": 100.0},
            {"_id": "Transportation", "total_amount": 50.0}
        ]

        # Set the values in the UI
        app.month_var.set("January")

        # Call show_summary function
        app.show_summary()

        # Ensure summary is displayed in expense_display
        self.assertEqual(app.expense_display.cget("text"), "Expense Summary for January 2024: \nFood: $100.00 \nTransportation: $50.00")

        # Clean up
        root.destroy()

if __name__ == "__main__":
    unittest.main()
