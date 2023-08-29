# Import packages
from dash import Dash, html, dash_table
import pandas as pd


# Incorporate data
df = (pd.read_csv('records/flute.csv'))


# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='Ordered Flute'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=2)

])


# Run the app
if __name__ == '__main__':
    app.run(debug=True)