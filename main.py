import saveinfo
import graph

try : 
  file = fileopen('finances.json')
  print(file)
except FileNotFoundError:
  file = filesave(Info(fileinfo['income'], fileinfo['expenses']), 'finances.json')

def user_input():
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
