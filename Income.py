class Income:

    def __init__(self, input_data):
        self.income_dict = {}
        for key, value in input_data.items():
            self.income_dict[key] = value

    def total_income(self):
        return sum(self.income_dict.values())

    


