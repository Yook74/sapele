import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objects as go

np.random.seed(42)

rand_x = np.random.randint(1,101,100)
rand_y = np.random.randint(1,101,100)

data = [go.Scatter(x=rand_x,
                   y=rand_y,
                   mode='markers',
                   marker=dict(
                       size=12,
                       color='rgb(51,204,153)',
                       symbol='pentagon',
                       line={'width':2}
                   ))]

layout = go.Layout(title='scat plot',
                   xaxis={'title':'My X Axis'},
                   yaxis=dict(title='My Y Axis'),
                   hovermode='closest')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig,filename='scatter.html')

