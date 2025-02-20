import saveinfo
import graph
file = open("finances.json", "w")


global income_input
global expenses_input

def user_input():
  global income_input
  global expenses_input
  print("What are your sources of income?")
  print("Format : ")
  print("name of expense : amount")
  income_input = input(str())
  income_input = str.split(income_input, ',')
  
  inputs = saveinfo.Info()
  input1 = {}
  for i in income_input:
    s = str.split(i, ':')
    input1[s[0]] = s[1]
  inputs.income = input1
  
  print("What are your expenses")
  print("Format : ")
  print("name of expense : amount")
  expenses_input = input(str())
  expenses_input = str.split(expenses_input, ',')

  input2 = {}
  for i in expenses_input:
    s = str.split(i, ':')
    input2[s[0]] = s[1]
  inputs.expenses = input2
  saveinfo.filesave(inputs, "finances.json")
def main():
  if not file.exists():
    user_input()
  file.close()

main()

graph.graph()
