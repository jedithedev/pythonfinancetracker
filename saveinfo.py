import json

class Info:
  def __init__(self, income, expenses):
    self.income = income
    self.expenses = expenses

def save(s : Info, filename : string):

  with open(filename, 'W') as f:
    json.dump(s, f)

def open(filename):
  file = open(filename, 'r').read()
  f = json.load(file)
  s = Info(f['income'], f['expenses'])

  return s
