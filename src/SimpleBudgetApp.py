import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry  # Import DateEntry from tkcalendar
import datetime

from Expense import Expense
from FinanceTracker import FinanceTracker

class SimpleBudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SimpleBudget - Personal Finance Tracker")
        
        self.tracker = FinanceTracker()
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Define available categories once
        self.categories = ["Food", "Transportation", "Entertainment", "Utilities", "Healthcare"]

        # Expense Amount Entry
        self.expense_label = tk.Label(self.frame, text="Expense Amount:")
        self.expense_label.grid(row=0, column=0, padx=5, pady=5)
        self.expense_entry = tk.Entry(self.frame)
        self.expense_entry.grid(row=0, column=1, padx=5, pady=5)

        # Category Dropdown for Expense
        self.category_label = tk.Label(self.frame, text="Category:")
        self.category_label.grid(row=1, column=0, padx=5, pady=5)
        self.category_var = tk.StringVar(self.frame)
        self.category_var.set("Select Category")  # Default value
        self.category_menu = tk.OptionMenu(self.frame, self.category_var, *self.categories)
        self.category_menu.grid(row=1, column=1, padx=5, pady=5)

        # Date Picker
        self.date_label = tk.Label(self.frame, text="Date (YYYY-MM-DD):")
        self.date_label.grid(row=2, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(self.frame, date_pattern="yyyy-mm-dd", set_date=datetime.date.today())  # Corrected initialization
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        # Log Expense Button
        self.log_button = tk.Button(self.frame, text="Log Expense", command=self.log_expense)
        self.log_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Budget Limit Entry
        self.budget_label = tk.Label(self.frame, text="Set Category Budget:")
        self.budget_label.grid(row=4, column=0, padx=5, pady=5)
        self.budget_entry = tk.Entry(self.frame)
        self.budget_entry.grid(row=4, column=1, padx=5, pady=5)

        # Budget Category Dropdown
        self.budget_category_label = tk.Label(self.frame, text="Category for Budget:")
        self.budget_category_label.grid(row=5, column=0, padx=5, pady=5)
        self.budget_category_var = tk.StringVar(self.frame)
        self.budget_category_var.set("Select Category")  # Default value
        self.budget_category_menu = tk.OptionMenu(self.frame, self.budget_category_var, *self.categories)
        self.budget_category_menu.grid(row=5, column=1, padx=5, pady=5)

        # Set Budget Button
        self.set_budget_button = tk.Button(self.frame, text="Set Budget", command=self.set_budget)
        self.set_budget_button.grid(row=6, column=0, columnspan=2, pady=10)
        
        # Show Summary Button
        self.summary_button = tk.Button(self.frame, text="Show Summary", command=self.show_summary)
        self.summary_button.grid(row=7, column=0, columnspan=2, pady=10)

        # Display Logged Expenses
        self.expense_display = tk.Label(self.frame, text="Logged Expenses will appear here.")
        self.expense_display.grid(row=8, column=0, columnspan=2, pady=10)

    def log_expense(self):
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
                if amount <= 0: #ensuring value is greater than 0
                    raise ValueError("Amount must be greater than 0.")
            except ValueError:
                raise ValueError("Amount must be a valid number.")

            budget_limit = self.tracker.get_budget(category)
            if budget_limit and amount > budget_limit:
                messagebox.showwarning(
                    "Budget Warning",
                    f"Expense amount exceeds the budget of ${budget_limit} for {category}!"
                )

            # Create Expense object and log it
            expense = Expense(amount, category, date)
            self.tracker.log_expense(expense)
            messagebox.showinfo("Success", "Espense added Successfully!!!")
            # Update the display with the logged expense
            self.expense_display.config(text=f"Logged Expense: {expense}")

            current_text = self.expense_display.cget("text")
            new_entry = f"{expense}\n"
            self.expense_display.config(text=current_text + new_entry)
            
            # Clear the input fields
            self.expense_entry.delete(0, tk.END)
            self.category_var.set("Select Category")  # Reset category dropdown
            self.date_entry.set_date(datetime.date.today())  # Reset date to today

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def set_budget(self):
        try:
            category = self.budget_category_var.get()
            limit = self.budget_entry.get()
            
            if not category or category == "Select Category" or not limit:
                raise ValueError("Category and Budget Limit are required fields.")
            
            self.tracker.set_budget(category, limit)
            self.budget_category_var.set("Select Category")  # Reset category dropdown
            self.budget_entry.delete(0, tk.END)
            messagebox.showinfo("Budget Set", f"Budget for {category} set to ${limit}.")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def show_summary(self):
        summary = self.tracker.show_summary()
        self.expense_display.config(text=summary)


if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleBudgetApp(root)
    root.mainloop()

#everything sould be clear, needs to run in an environment with the GUI