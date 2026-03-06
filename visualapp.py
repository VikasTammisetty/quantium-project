import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

df = pd.read_csv("formated_sales_data.csv")

df["Date"] = pd.to_datetime(df["Date"])

app = Dash(__name__)

app.layout = html.Div([

    html.H1(
        "Pink Morsel Sales Dashboard",
        style={
            "textAlign": "center",
            "color": "#2c3e50",
            "marginBottom": "30px"
        }
    ),

    html.Label("Select Region:", style={"fontWeight": "bold"}),

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
        inline=True,
        style={"marginBottom": "20px"}
    ),

    dcc.Graph(id="sales-chart")

], style={
    "width": "80%",
    "margin": "auto",
    "padding": "20px",
    "fontFamily": "Arial"
})

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
        title= "Pink Morsel Sales Over Time"
    )

    fig.update_layout(
        xaxis_title = "Date",
        yaxis_title = "Sales ($)",
        template = "plotly_white"
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)