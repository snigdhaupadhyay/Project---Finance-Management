import calendar
import datetime
from tkinter import messagebox
from Budget import Budget
from pymongo import MongoClient

class FinanceTracker:
    
    def __init__(self):
        self.expenses = []
        self.budgets = {}

   # MongoDB connection
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["Finance_Tracker"]
        self.expenses_collection = self.db["ExpenseDb"]
        self.budget_collection = self.db["CategoryBudgetDb"]
        
    def log_expense(self, expense):
        try:
       # self.expenses.append(expense)
             self.expenses_collection.insert_one(expense)
        except ValueError as e:
            messagebox.showerror(" Error", str(e))   
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to fetch summary: {e}")

    def set_budget(self, category,limit):
        try:
           # self.budgets[category] = Budget(category, limit)
           #check for existing budget
            existing_budget = self.budget_collection.find_one({"category": category})
            if existing_budget:
                # Update the budget if it exists
                self.budget_collection.update_one(
                    {"category": category},
                    {"$set": {"limit": limit}}
                )
                return 1               
            else:
                # Insert a new budget if it doesn't exist
                self.budget_collection.insert_one({"category": category, "limit": limit})
                return 2
        except ValueError as e:
            messagebox.showerror(" Error", str(e))   
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to fetch summary: {e}")

    def show_expenses(self):
        return "\n".join([str(expense) for expense in self.expenses])

    def show_summary(self):
        try:
            summary_data = self.expenses_collection.aggregate([
                    {"$group": {"_id": "$category", "total_amount": {"$sum": "$amount"}}}
                ])
        except ValueError as e:
            messagebox.showerror(" Error", str(e))   
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to fetch summary: {e}")
        return summary_data
   
    def get_allsummary(self):
         all_expenses = list(self.expenses_collection.find({}))
         return all_expenses

    def get_budget(self,category):
        try:
            budget_data = self.budget_collection.find_one({"category": category})
                   
        except ValueError as e:
            messagebox.showerror(" Error", str(e))   
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to fetch summary: {e}")
        return budget_data
    
    def get_allbudget(self):
        try:
            budget_data = self.budget_collection.find({})
                   
        except ValueError as e:
            messagebox.showerror(" Error", str(e))   
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to fetch summary: {e}")
        return budget_data
    
    def show_summarybymonth(self, month):
        try:
            month_num = list(calendar.month_name).index(month)
            current_year = datetime.date.today().year

                # Aggregate expenses by category for the selected month
            summary_data = self.expenses_collection.aggregate([
                    {
                        "$addFields": {
                            "month": {"$month": {"$dateFromString": {"dateString": "$date"}}},
                            "year": {"$year": {"$dateFromString": {"dateString": "$date"}}}
                        }
                    },
                    {"$match": {"month": month_num, "year": current_year}},
                    {"$group": {"_id": "$category", "total_amount": {"$sum": "$amount"}}}
                ])
        except ValueError as e:
            messagebox.showerror(" Error", str(e))   
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to fetch summary: {e}")
        return summary_data
            
    def show_summarybycategory(self,category):
        try:
            all_expenses = list(self.expenses_collection.find({}))
            filtered_expenses = [expense for expense in all_expenses if expense.get("category") == category]

             # Calculate the total amount for the selected category
            total_amount = sum(expense.get("amount", 0) for expense in filtered_expenses)

        except ValueError as e:
            messagebox.showerror(" Error", str(e))   
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to fetch summary: {e}")
        return filtered_expenses
    
   