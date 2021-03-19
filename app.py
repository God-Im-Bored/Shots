import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
from kawhi_shot import full_fig
from kd_shot import kd_full_fig
from pg_shot import pg_full_fig
from bron_shot import bron_full_fig
from demar_shot import demar_full_fig
from ben_shot import ben_full_fig

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1('Player Shot Charts'),
    html.H3('Graphed using Plotly'),
    html.H3('Rendered using Dash'),
    html.H5('by: Aram Martin'),
    dcc.Dropdown(
        id='shot-chart-dropdown',
        options=[
            {'label': 'Kawhi Leonard', 'value': 'full_fig'},
            {'label': 'Kevin Durant', 'value': 'kd_full_fig'},
            {'label': 'Paul George', 'value': 'pg_full_fig'},
            {'label': 'Lebron James', 'value': 'bron_full_fig'},
            {'label': 'DeMar DeRozan', 'value': 'demar_full_fig'},
            {'label': 'Ben Simmons', 'value': 'ben_full_fig'}
        ],
        placeholder='Select a player',
    ),

    dcc.Graph(
        id='kawhi_shot_chart',
        figure=full_fig
    ),
    dcc.Graph(
        id='kd_shot_chart',
        figure=kd_full_fig
    ),
    dcc.Graph(
       id='pg_shot_chart',
       figure=pg_full_fig
    ),
    dcc.Graph(
       id='bron_shot_chart',
       figure=bron_full_fig
    ),
    dcc.Graph(
       id='demar_shot_chart',
       figure=demar_full_fig
    ),
    dcc.Graph(
       id='ben_shot_chart',
       figure=ben_full_fig
    )

]
)


@app.callback([
    Output('kawhi_shot_chart', 'figure'),
    Output('kd_shot_chart', 'figure'),
    Output('pg_shot_chart', 'figure'),
    Output('bron_shot_chart', 'figure'),
    Output('demar_shot_chart', 'figure'),
    Output('ben_shot_chart', 'figure'),
    Input('shot-chart-dropdown', 'value')
])

# server = app.run_server(debug=True)


def update_output(value):
    return 'You have selected "{}"'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
