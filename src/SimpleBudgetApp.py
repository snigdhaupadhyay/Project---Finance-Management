import calendar
from pymongo import MongoClient
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
        
         # Month Dropdown for Summary
        self.month_label = tk.Label(self.frame, text="Select Month:")
        self.month_label.grid(row=7, column=0, padx=5, pady=5)
        self.month_var = tk.StringVar(self.frame)
        self.month_var.set("Select Month")  # Default value
        self.month_menu = tk.OptionMenu(
            self.frame,
            self.month_var,
            *[calendar.month_name[i] for i in range(1, 13)]
        )
        self.month_menu.grid(row=7, column=1, padx=5, pady=5)
        
        # summary Budet Category Dropdown
        self.summary_category_label = tk.Label(self.frame, text="Category for Budget:")
        self.summary_category_label.grid(row=8, column=0, padx=5, pady=5)
        self.summary_category_var = tk.StringVar(self.frame)
        self.summary_category_var.set("Select Category")  # Default value
        self.summary_category_menu = tk.OptionMenu(self.frame, self.budget_category_var, *self.categories)
        self.summary_category_menu.grid(row=8, column=1, padx=5, pady=5)

        # Show Summary Button
        self.summary_button = tk.Button(self.frame, text="Show Summary", command=self.show_summary)
        self.summary_button.grid(row=9, column=0, columnspan=1, padx=5, pady=5)

        #Clear Summary
        self.clear_button = tk.Button(self.frame, text="Clear Summary", command=self.clear_summary)
        self.clear_button.grid(row=9, column=1, columnspan=1, padx=5, pady=5)

        # Display Logged Expenses
        self.expense_display = tk.Label(self.frame, text="Logged Expenses will appear here.")
        self.expense_display.grid(row=10, column=0, columnspan=2, pady=10)

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
            except ValueError:
                raise ValueError("Amount must be a valid number.")

            # Log expense in MongoDB
            expense_data = {
                "amount": amount,
                "category": category,
                "date": date
            }
            budget_data =  self.tracker.get_budget(category)
            set_amount = float(budget_data["limit"])
            if amount > set_amount:
                diff_amount = amount - set_amount
                messagebox.showwarning( "Budget Exceeded",f"Budget for   {category} has exceeded  by ${diff_amount}")
            self.tracker.log_expense(expense_data)

            messagebox.showinfo("Success", "Expense logged successfully!")
            # Update the display with the logged expense
            self.expense_display.config(text=f"Logged Expense: Amount={amount}, Category={category}, Date={date}")
            
            # Clear the input fields
            self.expense_entry.delete(0, tk.END)
            self.category_var.set("Select Category")  # Reset category dropdown
            self.date_entry.set_date(datetime.date.today())  # Reset date to today

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to log expense: {e}")


    def set_budget(self):
        try:
            category = self.budget_category_var.get()
            limit = self.budget_entry.get()
            
            if not category or category == "Select Category" or not limit:
                raise ValueError("Category and Budget Limit are required fields.")
            try:
                limit = float(limit)
            except ValueError:
                raise ValueError("Amount must be a valid number.")
            
            result =  self.tracker.set_budget(category, limit)
            if result ==1 :
                messagebox.showinfo("Budget Updated", f"Updated budget for {category} to ${limit}.")
            if result==2:
                messagebox.showinfo("Budget Set", f"Set new budget for {category} to ${limit}.")
            self.budget_category_var.set("Select Category")  # Reset category dropdown
            self.budget_entry.delete(0, tk.END)
           # messagebox.showinfo("Budget Set", f"Budget for {category} set to ${limit}.")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def show_summary(self):
        try:
            selected_month = self.month_var.get()
            current_year = datetime.date.today().year
            selected_category = self.summary_category_var.get()
            if selected_month == "Select Month":
                 summary_data = self.tracker.show_summary()
                 summary = f"Expense Summary: "
            else:
                summary_data = self.tracker.show_summarybymonth(selected_month)
                summary = f"Expense Summary for {selected_month} {current_year}: "

                       
            # Build a summary string
           # summary = f"Expense Summary for {selected_month} {current_year}: "
            for entry in summary_data:
                category = entry["_id"]
                total = entry["total_amount"]
                summary += f" {category}: ${total:.2f} "
            
            if summary == f"Expense Summary for {selected_month} {current_year}: ":
                summary += " No expenses recorded for this month."
            
            # Update the display with the summary
            self.expense_display.config(text=summary)
        
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to fetch summary: {e}")

    def clear_summary(self):
        # Clear the input fields
            self.expense_display.config(text="")
            self.month_var.set("Select Month")  # Reset category dropdown
            

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleBudgetApp(root)
    root.mainloop()