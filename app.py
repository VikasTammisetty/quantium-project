from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# Load data
df = pd.read_csv("formated_sales_data.csv")

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Create app
app = Dash(__name__)
server = app.server

app.layout = html.Div([

    html.H1("Soul Foods Sales Visualiser", style={"textAlign": "center"}),

    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "South", "value": "south"},
            {"label": "East", "value": "east"},
            {"label": "West", "value": "west"}
        ],
        value="all",
        inline=True
    ),

    dcc.Graph(id="sales-chart")

])


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)

def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        title="Pink Morsel Sales Over Time",
        labels={"Date": "Date", "Sales": "Sales ($)"}
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)