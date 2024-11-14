class FinanceTracker:
    def __init__(self):
        self.expenses = []
        self.budgets = {}

    def log_expense(self, expense):
        self.expenses.append(expense)

    def set_budget(self, category, limit):
        self.budgets[category] = Budget(category, limit)

    def show_expenses(self):
        return "\n".join([str(expense) for expense in self.expenses])

    def show_summary(self):
        summary = []
        for category, budget in self.budgets.items():
            status = 'Within Budget' if budget.is_within_budget() else 'Over Budget'
            summary.append(f"Category: {category}, Limit: ${budget.limit:.2f}, Spent: ${budget.total_spent:.2f}, {status}")
        return "\n".join(summary)
