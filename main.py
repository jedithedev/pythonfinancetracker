#Plotly must be installed in the directory using pip install plotly

#Imports
import saveinfo
import graph
from saveinfo import Info

#Open the .json file
file = open("finances.json", "w")

#Define "Global" variables
global income_input
global expenses_input
global income_volume
global expenses_volume
global target_list

#Fincance inputs for the file
def user_input():
  # Define endtable and global variables
  endtable = {'k' : '000', 'm' : '000000', 'b' : '000000000', 't' : '000000000000', "$" : " "}
  global income_input
  global expenses_input
  global income_volume
  global expenses_volume
  global target_list
  
  inputs = saveinfo.Info()
  print("What are your incomes? Seperate each one with a comma.")
  income_input = input(str())
  income_input = str.split(income_input, ', ' or ',' or ' ')

  income_volume = []
  expenses_volume = []

  for i in income_input:
    print("How much money comes from " + i + "?")
    temp_input = input()

    for i in endtable:
      if temp_input.lower()[-1] == i and endtable[i]:
        temp_input = temp_input.lower().replace(i, "")
        temp_input = float(temp_input) * int('1' + endtable[i])
        temp_input = int(temp_input)
        break
        

    income_volume.append(int(temp_input))

  print("What are your expenses? Seperate each one with a comma.")
  expenses_input = input(str())
  expenses_input = str.split(expenses_input, ',')
  
  for i in expenses_input:
    print("How much money goes into " + i + "?")
    temp_input = input()
    for i in endtable:
      if temp_input.lower()[-1] == i and endtable[i]:
        temp_input = temp_input.lower().replace(i, "")
        temp_input = float(temp_input) * int('1' + endtable[i])
        temp_input = int(temp_input)
        break
    expenses_volume.append(int(temp_input))
    

  #Send the inputs to be saved in the .json file
  inputs.income = income_input
  inputs.expenses = expenses_input
  inputs.income_volume = income_volume
  inputs.expenses_volume = expenses_volume
  saveinfo.filesave(inputs, "finances.json")
  
#Main code that runs when the program starts
def main():
  user_input()
  file.close()
  graph.graph()
#Line that runs the code
main()
