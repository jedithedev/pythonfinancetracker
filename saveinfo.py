import json

class Info:
  def __init__(self, income, expenses):
    self.income = income
    self.expenses = expenses

  def input_data(self):
    
    print(What are your incomes?")
    income_input = input(str())
    self.income = income_input
  
    print(What are your expenses?")
    expenses_input = input(str())
    self.expenses = expenses_input

def filesave(s : Info, filename : str):

  with open(filename, 'w') as f:
    json.dump({'income' : s.income, 'expenses' : s.expenses}, f, indent=2)

def fileopenclass(filename):
  file = open(filename, 'r')
  f = json.load(file)
  s = Info(f['income'], f['expenses'])

  return s

def fileopen(filename):
  file = open(filename, 'r')
  f = json.load(file)

  return f
