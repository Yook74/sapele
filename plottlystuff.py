import random
import numpy as np
from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from plotly import graph_objects as go
import plotly.express as px





app = Dash(__name__)

colors = ['aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'black',
          'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse',
          'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue',
          'darkcyan', 'darkgoldenrod', 'darkgray', 'darkgrey', 'darkgreen', 'darkkhaki',
          'darkmagenta', 'darkolivegreen', 'darkorange', 'darkorchid', 'darkred', 'darksalmon',
          'darkseagreen', 'darkslateblue', 'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet',
          'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue', 'firebrick', 'floralwhite',
          'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray', 'grey',
          'green', 'greenyellow', 'honeydew', 'hotpink', 'indianred', 'indigo', 'ivory', 'khaki',
          'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral',
          'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgrey', 'lightgreen', 'lightpink',
          'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 'lightsteelblue',
          'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue',
          'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen',
          'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'moccasin',
          'navajowhite', 'navy', 'oldlace', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid',
          'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip', 'peachpuff',
          'peru', 'pink', 'plum', 'powderblue', 'purple', 'red', 'rosybrown', 'royalblue', 'rebeccapurple',
          'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver', 'skyblue',
          'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle',
          'tomato', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen']

app.layout = html.Div([
    dcc.Graph('myGraph'),

    html.Button(id='get-fft', n_clicks=0, children='Get FFT', style={'margin-left': 80}),
    dcc.Checklist(['Average'], id='average-on', style={'margin-left': 60}),
    html.Div(id='output-state'),

    html.Hr(),
    html.Div(children=[
        html.Label('background color'),
        dcc.Dropdown(colors, value='lightgrey', id='bg-color'),
        html.Label('trace 1 color'),
        dcc.Dropdown(colors, value='blue', id='trace1-color'),
        html.Label('trace 2 color'),
        dcc.Dropdown(colors, value='yellow', id='trace2-color'),
    ], style={'width': '200px', 'padding-top': 1, 'padding-bottom': 10, 'margin-left': 0, 'flex': 1}),

    html.Div(children=[
        html.Br(),
        html.Label('tex box'),
        dcc.Input(value='test stuff', type='text', id='ip-address', style={'width': 90}),
    ], style={'padding-top': 10, 'padding-bottom': 20, 'flex': 1}),

    html.Div(children=[
        html.Br(),
        html.Label('count'),
        dcc.Input(value='0', type='text', id='count', style={'width': 90}),
    ], style={'padding-top': 10, 'padding-bottom': 20, 'flex': 1}),

])


def create_trace(length=601):
    x = []
    y = []
    for num in range(length):
        x.append(num)
        y.append(random.gauss(-80, 3))

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='TRACE 1',
                             line=dict(color=str('blue'), width=1), showlegend=True))
    fig.show()


@app.callback(Output('myGraph', 'figure'),
              Output('count', 'value'),
              Input('get-fft', 'n_clicks'),
              Input('bg-color', 'value'),
              Input('trace1-color', 'value'),
              Input('trace2-color', 'value'),
              State('count', 'value'),
              State('myGraph', 'figure'),
              State('average-on', 'value')
              )
def update_plot(_, bg_color, trace1_color, trace2_color, count, figure, average_on):

    counter = int(count)

    x, y = create_trace(600)
    if counter != 0:
        y = [
            (old_y * counter + new_y) / (counter + 1)
            for new_y, old_y in zip(y, figure['data'][0]['y'])
        ]

    x, yy = create_trace(600)
    if counter != 0:
        yy = [
            (old_y * counter + new_y) / (counter + 1)
            for new_y, old_y in zip(yy, figure['data'][0]['y'])
        ]

    if not average_on:
        counter = 0

    if counter != 0:
        y = [
            (old_y * counter + new_y) / (counter + 1)
            for new_y, old_y in zip(y, figure['data'][0]['y'])
        ]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='TRACE 1',
                             line=dict(color=str(trace1_color), width=1), showlegend=True))
    # fig.add_trace(go.Scatter(x=x, y=yy, mode='lines', name='TRACE 2',
    #                          line=dict(color=str(trace2_color), width=1), showlegend=True))
    fig.update_layout(autosize=False, width=1100, height=600, uirevision=True, plot_bgcolor=str(bg_color))
    fig.add_vrect(x0=290, x1=310)

    if not average_on:
        counter = 0
    else:
        counter += 1

    return fig, counter


if __name__ == '__main__':
    create_trace(601)
