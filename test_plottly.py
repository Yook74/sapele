# Import packages
from database.connection import get_session
from dash import Dash, html, dash_table
import pandas as pd


sess = get_session()
conn = sess.connection()

# Incorporate data
# df = (pd.read_csv('../../../../../Documents/sapele/records/flute.csv'))
df = (pd.read_sql('SELECT * from FHP', conn))

# Initialize the app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.Div(children='FH Percents'),
    dash_table.DataTable(data=df.to_dict('records'))

],
style={'width': '800px', 'padding-top': 1, 'padding-bottom': 10, 'margin-left': 100, 'flex': 1})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)