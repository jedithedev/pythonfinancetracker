import saveinfo
import graph.py
from saveinfo import Info
from graph import json

try : 
  file = saveinfo.fileopen('finances.json')
  print(file)
except FileNotFoundError:
  file = saveinfo.filesave(Info(fileinfo['income'], fileinfo['expenses']), 'finances.json')

income_input = input(str())


print("What are your incomes?")
income_input = input(str())
print(income_input)

print("What are your expenses")
expenses_input input(str())
print(expenses_input)

finances = {
  'income' : income_input
  'expenses' : expenses_input
}
