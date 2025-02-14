import saveinfo
from saveinfo import Info

fileinfo = {
  'income' : {
    'unemployed' : 25,
    'selling grease' : 25
  },
  'expenses' : {
    'rent (cardboard box)' : 5,
    'mcdonalds' : 43
  }
}

try : 
  file = saveinfo.fileopen('finances.json')
  print(file)
except FileNotFoundError:
  file = saveinfo.filesave(Info(fileinfo['income'], fileinfo['expenses']), 'finances.json')
