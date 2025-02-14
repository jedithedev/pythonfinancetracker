import saveinfo
from saveinfo import Info

file = open('finances.json', 'r')

if len(file.read()) < 2:
  print('empty file')


saveinfo.save(['table'], ['table2'])

