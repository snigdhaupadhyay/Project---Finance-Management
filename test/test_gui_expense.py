# import tkinter as tk
# import unittest
# from unittest.mock import patch, MagicMock
# from tkinter import messagebox
# import os
# import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
# from datetime import datetime
# from Expense import Expense


# class TestExpenseGUI(unittest.TestCase):

#     @patch("tkinter.messagebox.showerror")
#     @patch.object(Expense, "__str__")
#     def test_create_expense_button_click(self, mock_str, mock_messagebox):
#         # Create a Tkinter instance
#         root = tk.Tk()
#         root.geometry("400x400")
        
#         # Create the necessary widgets
#         amount_entry = tk.Entry(root)
#         category_entry = tk.Entry(root)
#         date_entry = tk.Entry(root)
#         create_button = tk.Button(root, text="Create Expense")
        
#         # Place widgets on the window
#         amount_entry.insert(0, "100.0")
#         category_entry.insert(0, "Food")
#         date_entry.insert(0, "2024-12-12")

#         # Define a callback for the button
#         def on_click():
#             amount = float(amount_entry.get())
#             category = category_entry.get()
#             date = date_entry.get()
            
#             # Create an Expense object
#             expense = Expense(amount, category, date)
#             # Simulate adding expense to the system (here, we mock the __str__ method)
#             mock_str.return_value = str(expense)
            
#             # Show a success message
#            # messagebox.showinfo("Success", f"Expense Created: {str(expense)}")
        
#         create_button.config(command=on_click)

#         # Simulate button click
#         create_button.invoke()

#         # Assert that the messagebox.showinfo was called with the correct message
#         mock_str.assert_called_once()
#         mock_messagebox.showinfo.assert_called_once_with("Success", "Expense Created: 2024-12-12 - Food - $100.00")

#         root.destroy()

#     @patch("tkinter.messagebox.showerror")
#     @patch.object(Expense, "__str__")
#     def test_create_expense_invalid_input(self, mock_str, mock_messagebox):
#         # Create a Tkinter instance
#         root = tk.Tk()
#         root.geometry("400x400")
        
#         # Create the necessary widgets
#         amount_entry = tk.Entry(root)
#         category_entry = tk.Entry(root)
#         date_entry = tk.Entry(root)
#         create_button = tk.Button(root, text="Create Expense")
        
#         # Place widgets on the window with invalid data
#         amount_entry.insert(0, "not_a_number")
#         category_entry.insert(0, "Food")
#         date_entry.insert(0, "2024-12-12")

#         # Define a callback for the button
#         def on_click():
#             try:
#                 amount = float(amount_entry.get())  # This should raise a ValueError
#                 category = category_entry.get()
#                 date = date_entry.get()
                
#                 # Create an Expense object
#                 expense = Expense(amount, category, date)
#                 # Simulate adding expense to the system (here, we mock the __str__ method)
#                 mock_str.return_value = str(expense)
                
#                 # Show a success message
#                 messagebox.showinfo("Success", f"Expense Created: {str(expense)}")
#             except ValueError:
#                 mock_messagebox.showerror("Invalid Input", "Amount must be a number.")

#         create_button.config(command=on_click)

#         # Simulate button click
#         create_button.invoke()

#         # Assert that an error messagebox was shown due to invalid input
#         mock_messagebox.showerror.assert_called_once_with("Invalid Input", "Amount must be a number.")

#         root.destroy()

