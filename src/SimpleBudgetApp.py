import tkinter as tk
from tkinter import messagebox

import Expense
import FinanceTracker

class SimpleBudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SimpleBudget - Personal Finance Tracker")
        
        self.tracker = FinanceTracker()
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.expense_label = tk.Label(self.frame, text="Expense Amount:")
        self.expense_label.grid(row=0, column=0, padx=5, pady=5)
        self.expense_entry = tk.Entry(self.frame)
        self.expense_entry.grid(row=0, column=1, padx=5, pady=5)

        self.category_label = tk.Label(self.frame, text="Category:")
        self.category_label.grid(row=1, column=0, padx=5, pady=5)
        self.category_entry = tk.Entry(self.frame)
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)

        self.date_label = tk.Label(self.frame, text="Date (YYYY-MM-DD):")
        self.date_label.grid(row=2, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(self.frame)
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        self.log_button = tk.Button(self.frame, text="Log Expense", command=self.log_expense)
        self.log_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.budget_label = tk.Label(self.frame, text="Set Category Budget:")
        self.budget_label.grid(row=4, column=0, padx=5, pady=5)
        self.budget_entry = tk.Entry(self.frame)
        self.budget_entry.grid(row=4, column=1, padx=5, pady=5)

        self.budget_category_label = tk.Label(self.frame, text="Category for Budget:")
        self.budget_category_label.grid(row=5, column=0, padx=5, pady=5)
        self.budget_category_entry = tk.Entry(self.frame)
        self.budget_category_entry.grid(row=5, column=1, padx=5, pady=5)

        self.set_budget_button = tk.Button(self.frame, text="Set Budget", command=self.set_budget)
        self.set_budget_button.grid(row=6, column=0, columnspan=2, pady=10)
        
        self.summary_button = tk.Button(self.frame, text="Show Summary", command=self.show_summary)
        self.summary_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.expense_display = tk.Label(self.frame, text="Logged Expenses will appear here.")
        self.expense_display.grid(row=8, column=0, columnspan=2, pady=10)

    def log_expense(self):
        try:
            amount = self.expense_entry.get()
            category = self.category_entry.get()
            date = self.date_entry.get()
            if not amount or not category:
                raise ValueError("Amount and Category are required fields.")
            
            expense = Expense(amount, category, date)
            self.tracker.log_expense(expense)
            self.expense_display.config(text=f"Logged Expense: {expense}")
            
            self.expense_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def set_budget(self):
        try:
            category = self.budget_category_entry.get()
            limit = self.budget_entry.get()
            if not category or not limit:
                raise ValueError("Category and Budget Limit are required fields.")
            
            self.tracker.set_budget(category, limit)
            self.budget_category_entry.delete(0, tk.END)
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
