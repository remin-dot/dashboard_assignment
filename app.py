import dash
from dash import html, dcc, Output, Input
import plotly.express as px
import pandas as pd

# load sample dataset
df = px.data.iris()

app = dash.Dash(__name__)

# layout with dropdown and three graphs
app.layout = html.Div([
    html.H1("Simple Interactive Dashboard"),
    dcc.Dropdown(
        id="species-dropdown",
        options=[{"label": s, "value": s} for s in df["species"].unique()],
        value=df["species"].unique().tolist(),
        multi=True,
        placeholder="Select species"
    ),
    dcc.Graph(id="scatter-graph"),
    dcc.Graph(id="line-graph"),
    dcc.Graph(id="bar-graph"),
])

# callbacks to update graphs based on selected species
@app.callback(
    Output("scatter-graph", "figure"),
    Output("line-graph", "figure"),
    Output("bar-graph", "figure"),
    Input("species-dropdown", "value")
)
def update_graphs(selected_species):
    # filter data
    if not selected_species:
        filtered = df
    else:
        filtered = df[df["species"].isin(selected_species)]

    # scatter: sepal vs petal
    scatter = px.scatter(filtered,
                         x="sepal_width", y="petal_width",
                         color="species",
                         title="Sepal width vs Petal width")

    # line: mean sepal length by species
    line_data = filtered.groupby("species")["sepal_length"].mean().reset_index()
    line = px.line(line_data, x="species", y="sepal_length",
                   title="Average Sepal Length by Species")

    # bar: count of samples per species
    bar_data = filtered["species"].value_counts().reset_index()
    bar_data.columns = ["species", "count"]
    bar = px.bar(bar_data, x="species", y="count", title="Sample Count by Species")

    return scatter, line, bar

if __name__ == "__main__":
    # `run_server` was replaced by `run` in newer Dash versions
    app.run(debug=True)
