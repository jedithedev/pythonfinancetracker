import numpy as np
import plotly.graph_objects as go
from saveinfo import Info
f.open('finances.json', 'r')
diagram = go.Figure(data=[
  go.Sankey
    node = dict(
      thickness = 5,
      label = [i for i in f]
      color = "grey"
      ),
    link = dict(
      source = [ ],
      target = [ ],
      value = [ ]))])

fig.update_layout(
  title = name + "'s finance tracker"
  font = dict(size = 12 color = 'black')
)
fig.show()
