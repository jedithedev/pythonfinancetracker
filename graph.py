import numpy as np
import plotly.graph_objects as go
from saveinfo import Info

def graph():
  f.open('finances.json', 'r')
  diagram = go.Figure(data=[
    go.Sankey(
      node = dict(
        thickness = 5,
        label = [f.income, f.expenses]
        color = "grey"
        ),
      link = dict(
        source = [],
        target = [],
        value = []))])
  
  fig.update_layout(
    title = name + "'s finance tracker"
    font = dict(size = 12 color = 'black')
  )
  fig.show()
