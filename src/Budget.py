class Budget: 

    def __init__(self, category, limit):
        self.category = category
        self.limit = limit
        self.total_spent = 0
    
    def __getstate__(self) -> object:
        pass

    def add_expense(self, expense):
        if expense.category == self.category:
            self.total_spent += expense.amount

    def check_limit(self):
        return self.limit >= self.total_spent

    