import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry  # Import DateEntry from tkcalendar
import datetime

from Expense import Expense
from FinanceTracker import FinanceTracker
@@ -31,10 +33,10 @@ def __init__(self, root):
        self.category_menu = tk.OptionMenu(self.frame, self.category_var, *self.categories)
        self.category_menu.grid(row=1, column=1, padx=5, pady=5)

        # Date Picker
        self.date_label = tk.Label(self.frame, text="Date (YYYY-MM-DD):")
        self.date_label.grid(row=2, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(self.frame, date_pattern="yyyy-mm-dd", set_date=datetime.date.today())  # Corrected initialization
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        # Log Expense Button
@@ -71,18 +73,30 @@ def log_expense(self):
        try:
            amount = self.expense_entry.get()
            category = self.category_var.get()
            date = self.date_entry.get()  # Get the date from the DateEntry widget

            # Check if any of the required fields are empty
            if not amount or category == "Select Category" or not date:
                raise ValueError("Amount, Category, and Date are required fields.")

            # Check if amount is a valid number
            try:
                amount = float(amount)
            except ValueError:
                raise ValueError("Amount must be a valid number.")
            # Create Expense object and log it
            expense = Expense(amount, category, date)
            self.tracker.log_expense(expense)
            messagebox.showinfo("Success", "Espense added Successfully!!!")
            # Update the display with the logged expense
            self.expense_display.config(text=f"Logged Expense: {expense}")

            # Clear the input fields
            self.expense_entry.delete(0, tk.END)
            self.category_var.set("Select Category")  # Reset category dropdown
            self.date_entry.set_date(datetime.date.today())  # Reset date to today
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))