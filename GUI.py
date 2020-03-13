import pdb
from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from MonthlyExpense import MonthlyExpense

root = Tk()
root.title('Monthly Expense')

incomeframe = Frame(master = root)
incomeframe.pack(side = LEFT, padx = 20, pady =20)

expenseframe = Frame(master = root)
expenseframe.pack(side = LEFT,  padx = 20, pady =20)

submitframe = Frame(master = root)
submitframe.pack(side = LEFT,  padx = 20, pady =20)

title_income = Label(incomeframe, text = 'Income')
title_income.grid(row =0, column=0, columnspan = 3)

def check(val):
    if val.isdigit():
        return True
    elif val is "":
        return True
    else:
        return False

income_types = ['Salary', 'Rent', 'Other']
expense_types = ['Shopping', 'Dinner','Movie', 'Travel']
incomeentries = {}
incomeresult = {}
expenseentries = {}
expenseresult = {}

for i, iname in enumerate(income_types):
    income_name_label = Label(incomeframe, text = iname)
    income_name_label.grid(row =i+1, column=0)
    income_amount = Entry(incomeframe, width=30)
    income_amount.grid(row =i+1, column=1)
    income_amount.config(validate = "key", validatecommand = (income_amount.register(check), '%P'))
    incomeentries[iname] = income_amount

title_expense = Label(expenseframe, text = 'Expense')
title_expense.grid(row =0, column=0, columnspan = 3)

for i, ename in enumerate(expense_types):
    expense_name_label = Label(expenseframe, text = ename)
    expense_name_label.grid(row =i+1, column=0)
    expense_amount = Entry(expenseframe, width=30)
    expense_amount.grid(row =i+1, column=1)
    expense_amount.config(validate = "key", validatecommand = (expense_amount.register(check), '%P'))
    expenseentries[ename] = expense_amount

def clear():
    for key, value in expenseentries.items():
        value.delete(0, END)
    for key, value in incomeentries.items():
        value.delete(0, END)

def button_click():
    for key, value in expenseentries.items():
        if value.get() != "":
            expenseresult[key] = int(value.get()) 
    expenseresult['date'] = ent.get()
    for key, value in incomeentries.items():
        if value.get() != "":
            incomeresult[key] = int(value.get())   
    incomeresult['date'] = ent.get()
    
    monthly_expense1 = MonthlyExpense('Income')
    monthly_expense1.input_data(incomeresult)
    monthly_expense2 = MonthlyExpense('Expense')
    monthly_expense2.input_data(expenseresult)
    
    clear()

Label(submitframe, text = "Date").pack(padx=10, pady=10)
ent = DateEntry(submitframe, width = 15, backgroud = 'blue', foreground = 'red', borderwidth = 3)
ent.pack(padx = 10, pady = 10)
submitbutton = Button(submitframe, text = 'submit', command=lambda:button_click())
submitbutton.pack()
report = Button(submitframe, text = 'Report', command=lambda:button_click())
report.pack()

root.mainloop()