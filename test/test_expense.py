import unittest
from Expense import Expense

class TestExpense(unittest.TestCase):

    def test_initialization(self):
        expense = Expense(amount="100", category="Food", date="2024-11-14")
        
        self.assertEqual(expense.amount, "100")
        self.assertEqual(expense.category, "Food")
        self.assertEqual(expense.date, "2024-11-14")
    
    def test_str_method(self):
        expense = Expense(amount="100", category="Food", date="2024-11-14")
        self.assertEqual(str(expense), "100 - Food on 2024-11-14")
    
if __name__ == '__main__':
    unittest.main()
