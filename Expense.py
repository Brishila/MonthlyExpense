class Expense:

    def __init__(self, input_data):
        self.expense_dict = {}
        for key, value in input_data.items():
            self.expense_dict[key] = value

    def total_expense(self):
        return sum(self.expense_dict.values())

















