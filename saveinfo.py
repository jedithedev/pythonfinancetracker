#Imports
import json

#Class for the self. variables (not really needed anymore but it would take a lot of work to change the code and remove the class)
class Info:
  def __init__(self):
    self.income = None
    self.expenses = None
    self.income_volume = 0
    self.expenses_volume = 0

#code used to save info into a .json file
def filesave(s : Info, filename : str):

  with open(filename, 'w') as f:
    json.dump({'income' : s.income, 'expenses' : s.expenses, 'income_volume' : s.income_volume, 'expenses_volume' : s.expenses_volume}, f, indent=2)

#code used to initialise the .json file
def fileopenclass(filename):
  file = open(filename, 'r')
  f = json.load(file)
  s = Info(f['income'], f['expenses'], f['income_volume'], f['expenses_volume'])
  return s

#code used to open the .json file
def fileopen(filename):
  file = open(filename, 'r')
  f = json.load(file)
  return f
