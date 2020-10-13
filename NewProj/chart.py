import plotly.graph_objects as go
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import json
import math

# Create figure
fig = go.Figure()

with open('chartData.json') as f:
    data = json.load(f)

y_data = data['y_pval']
y_pval = data['y_pvalcum']

fig.update_yaxes(range=[math.floor(min(y_data)), max(y_data)*1.1])
fig.update_xaxes(range=[-4, 4])

# Add traces, one for each slider step
indices = []

# num of indices:
for step in np.arange(-4, 4, 0.1):
    indices.append(y_data[int((step + 4) * 100)])
    fig.add_trace(
        go.Scatter(
            visible=False,
            line=dict(color="#00CED1", width=.1),
            # name="𝜈 = " + str(step),
            x=np.arange(-4, 4, 0.1),
            y=indices,
            fill='tozeroy'
        )
    )


# Create and add slider
steps = []
length = 80
for i in range(length + 1):
    step = dict(
        method="restyle",
        args=[{"visible": [False] * length + [True]},
              {"title": "Z-Score = " + str(round((i / 10) - 4, 1)) + " and P-Value = " + str(y_pval[i*10])}],  # layout attribute
    )
    if (i == 80):
        fig.add_trace(
            go.Scatter(
                visible=True,
                line=dict(color="#00CED1", width=6),
                x=np.arange(-4, 4, 0.1),
                y=indices
            )
        )
        step["args"][0]["visible"][79] = True
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

fig.data[80].visible = True

sliders = [dict(
    active=1,
    currentvalue={"prefix": "Frequency: "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    sliders=sliders
)

#fig.write_html("chart1.html")

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)
