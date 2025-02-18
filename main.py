import saveinfo
import graph
file = open("finances.json", "w")

global income_input
global expenses_input

def user_input():
  global income_input
  global expenses_input
  print("What are your incomes? Seperate each one with a comma or a space.")
  income_input = input(str())
  income_input = str.split(income_input, ',')
  
  print(income_input)
  #file.write(str(income_input))

  inputs = saveinfo.Info()
  inputs.income = income_input
  
  print("What are your expenses")
  expenses_input = input(str())
  expenses_input = str.split(expenses_input, ',')
  inputs.expenses = expenses_input
  saveinfo.filesave(inputs, "finances.json")
def main():
  user_input()
  file.close()
  
main()

graph.graph()
