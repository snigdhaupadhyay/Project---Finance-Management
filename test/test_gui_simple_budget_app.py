import unittest
from tkinter import Tk, messagebox
from unittest.mock import patch
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from SimpleBudgetApp import SimpleBudgetApp

class TestSimpleBudgetAppGUI(unittest.TestCase):

    @patch("tkinter.messagebox.showinfo")
    @patch("tkinter.messagebox.showerror")
    def test_log_expense_button_click_valid(self, mock_showerror, mock_showinfo):
        root = Tk()
        app = SimpleBudgetApp(root)

        # Set the values in the UI
        app.expense_entry.insert(0, "100.0")
        app.category_var.set("Food")
        app.date_entry.set_date("2024-12-12")

        # Simulate button click
        app.log_expense()

        # Check if the success message was shown
        mock_showinfo.assert_called_once_with("Success", "Expense logged successfully!")
        mock_showerror.assert_not_called()

        # Check that the logged expense is updated in the UI
        self.assertEqual(app.expense_display.cget("text"), "Logged Expense: Amount=100.0, Category=Food, Date=2024-12-12")

        root.destroy()

    @patch("tkinter.messagebox.showerror")
    def test_log_expense_button_click_invalid_amount(self, mock_showerror):
        root = Tk()
        app = SimpleBudgetApp(root)

        # Set invalid value for amount
        app.expense_entry.insert(0, "not_a_number")
        app.category_var.set("Food")
        app.date_entry.set_date("2024-12-12")

        # Simulate button click
        app.log_expense()

        # Check that error message is shown
        mock_showerror.assert_called_once_with("Input Error", "Amount must be a valid number.")
        
        root.destroy()

if __name__ == "__main__":
    unittest.main()
