import json

class Info:
  def __init__(self, income, expenses):
    self.income = income
    self.expenses = expenses

def save(income, expenses, filename):
  s = Info(income, expenses)

  with open(filename, 'W') as f:
    json.dump(s, f)
  
