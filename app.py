

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv("formated_sales_data.csv")

df["Date"] = pd.to_datetime(df["Date"])

df = df.sort_values("Date")

fig = px.line(
    df, 
    x="Date", 
    y="Sales", 
    title ="Pink Morsels Sales Over Time", 
    labels= {"Date": "Date", "Sales": "Sales ($)"}
)


app = Dash(__name__)

app.layout = html.Div([

    html.H1("Soul Foods Sales Visualiser", style={"textAlign": "Center"}),
    dcc.Graph(id="sales-line-chart", figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)