from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd 

app = Dash(__name__)

df = pd.read_csv('processed_data.csv')
df = df.sort_values('date')
fig = px.line(df, x='date', y='sales', color='region', title='Pink Morsel Sales Over Time')
fig.update_layout(xaxis_title='Date', yaxis_title='Sales ($)', legend_title='Region')

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Dashboard'),
    dcc.Graph(
        id='sales-over-time',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run()
