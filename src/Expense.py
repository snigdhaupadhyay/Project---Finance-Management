from datetime import datetime

class Expense:
    def __init__(self, amount, category, date):
        self.amount = float(amount)
        self.category = category
        self.date = self.convert_to_datetime(date)  # Convert date to datetime 

    def convert_to_datetime(self, date):
        if isinstance(date, str):  # If the date is already a string, convert it to a datetime object
            return datetime.strptime(date, '%Y-%m-%d')
        return date  

    def __str__(self):
        # Ensure that self.date is a datetime object
        if isinstance(self.date, datetime):
            return f"{self.date.strftime('%Y-%m-%d')} - {self.category} - ${self.amount:.2f}"
        return f"{self.date} - {self.category} - ${self.amount:.2f}"  
