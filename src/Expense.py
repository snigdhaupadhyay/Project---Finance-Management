import datetime


class Expense:
        
    def __init__(self, amount, category, date=None):
        self.amount = float(amount)
        self.category = category
        self.date = date if date else datetime.now()

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d')} - {self.category} - ${self.amount:.2f}"