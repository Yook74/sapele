from dash import Dash, dcc, html, Input, Output, callback
import main3

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
dd_list = ['one', 'two', 'three']
dd_list2 = ['four', 'five', 'six']
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('OWF'),
    dcc.Tabs(id="main-menu", value='main-menu', children=[
        dcc.Tab(label='Craft Flute', value='craft-flute',
            children=[dcc.Dropdown(dd_list, value='two', id='dd-one', style={'width': '100px'}),]),
        dcc.Tab(label='Create Orders', value='create-order',
            children=[dcc.Dropdown(dd_list2, value='five', id='dd-two', style={'width': '100px'}),]),
        dcc.Tab(label='View Orders', value='view-order'),
        dcc.Tab(label='View Sales', value='view-sales'),
    ]),

    html.Div(id='main')
],style={'width': '1200px', 'margin-left': 200})


@callback(Output('main', 'children'),
            Input('main-menu', 'value'),
            Input('dd-one', 'value'),
            Input('dd-two', 'value'))
def render_content(tab, dd1, dd2):
    if tab == 'craft-flute':

        return dd1

    elif tab == 'create-order':
        return 'test 2'

    elif tab == 'view-order':
        return 'test 3'

    elif tab == 'view-sales':
        return 'test 4'

if __name__ == '__main__':
    app.run(debug=True)