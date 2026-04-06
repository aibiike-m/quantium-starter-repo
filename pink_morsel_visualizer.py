from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("processed_data.csv")
df = df.sort_values("date")

app.layout = html.Div(
    style={"textAlign": "center", "fontFamily": "sans-serif"},
    children=[
        html.H1(children="Pink Morsel Sales Dashboard", id="header"),
        dcc.RadioItems(
            id="region-picker",
            options=[
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
                {"label": "All", "value": "all"},
            ],
            value="all",
            inline=True,
            style={"padding": "20px", "fontSize": "20px"},
        ),
        dcc.Graph(id="visualization"),
    ],
)


@app.callback(Output("visualization", "figure"), Input("region-picker", "value"))
def update_graph(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df, x="date", y="sales", title=f"Sales for {selected_region} region"
    )
    fig.update_layout(xaxis_title="Date", yaxis_title="Sales ($)")
    return fig


if __name__ == "__main__":
    app.run()
