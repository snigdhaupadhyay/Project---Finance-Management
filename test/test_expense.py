import unittest
from datetime import datetime
from Expense import Expense  # Assuming Expense class is in a module named 'Expense'


class TestExpense(unittest.TestCase):

    def test_expense_initialization(self):
        # Test the initialization of Expense object
        expense = Expense(100.0, "Food", "2024-12-12")
        
        self.assertEqual(expense.amount, 100.0)
        self.assertEqual(expense.category, "Food")
        self.assertEqual(expense.date, datetime(2024, 12, 12))  # Ensure date is converted to datetime object

    def test_convert_to_datetime_with_string(self):
        # Test that a string date is converted correctly to a datetime object
        expense = Expense(100.0, "Food", "2024-12-12")
        
        self.assertEqual(expense.date, datetime(2024, 12, 12))

    def test_convert_to_datetime_with_datetime(self):
        # Test that a datetime object is passed as-is (no conversion)
        expense = Expense(100.0, "Food", datetime(2024, 12, 12))
        
        self.assertEqual(expense.date, datetime(2024, 12, 12))

    def test_str_method(self):
        # Test the string representation of the Expense object
        expense = Expense(100.0, "Food", "2024-12-12")
        
        # Expected string format should be '2024-12-12 - Food - $100.00'
        self.assertEqual(str(expense), "2024-12-12 - Food - $100.00")
    
    def test_str_method_with_non_datetime(self):
        # Test the string method when the date is not a datetime object
        expense = Expense(50.0, "Transport", "2024-12-12")
        
        # Check if the string format matches expected output
        self.assertEqual(str(expense), "2024-12-12 - Transport - $50.00")
