from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from plotly import graph_objects as go
import time

app = Dash(__name__)

craft_menu = ['Blank Sizing', 'FH Placement', 'Reference Offset', 'Scale Notes', 'Change Key']
craft_menu2 = ['Blank ', 'FH ', 'Reference ', 'Scale ', 'Change ']
app.layout = html.Div([

    html.Hr(),
    html.Div(children=[
        html.Label('Craft Menu'),
        dcc.Dropdown(craft_menu, value='Blank Sizing', id='craft'),
    ], style={'width': '200px', 'padding-top': 1, 'padding-bottom': 10, 'margin-left': 0, 'flex': 1}),

    html.Div(children=[
        html.Br(),
        html.Label('Results'),
        dcc.Input(value='test stuff', type='text', id='test-text', style={'width': 500}),
    ], style={'padding-top': 10, 'padding-bottom': 20, 'flex': 1}),


    dcc.Input(placeholder='Enter value', type='text', id='my-input', value=''),
])


@app.callback(Output('test-text', 'value'),
              Input('craft', 'value'),
              Input('my-input', 'n-submit')
              )

def test(craft):


    item = craft
    # print(item)
    return item


if __name__ == '__main__':
    app.run_server(debug=True)
