import saveinfo
from saveinfo import Info

try : 
  file = open('finances.json', 'r')
except FileNotFoundError:
  file = saveinfo.filesave(Info(100, 50), 'finances.json')
