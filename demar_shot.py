from nba_api.stats.endpoints import shotchartdetail
import pandas as pd
import json
import pandas as pd
import plotly.graph_objs as go
from kawhi_shot import court_shapes

response = shotchartdetail.ShotChartDetail(
        team_id=0,
        player_id=201942,
        season_nullable='2020-21',
        season_type_all_star='Regular Season'
)
demar_data = json.loads(response.get_json())

results = demar_data['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
demar_df = pd.DataFrame(rows)
demar_df.columns = headers

demar_df.to_csv(r'/home/aram/Downloads/demar.csv', index=False)

demar_df = pd.read_csv('/home/aram/Downloads/demar.csv', encoding='Latin-1')

trace_shot = go.Scatter(
        x = demar_df['LOC_X'],
        y = demar_df['LOC_Y'],
        mode = 'markers',
        name = 'Made Field Goal',
        marker = dict(
            size = 5,
            color = 'rgba(0, 200, 100, .8)',
            line = dict(
                width = 1,
                color = 'rgb(0, 0, 0, 1)'
            )
        ) 
)

data = [trace_shot]
layout = go.Layout(
    showlegend=False,
    height=800,
    width=800
)

fig = go.Figure(data=data, layout=layout)

data = [trace_shot]
layout = go.Layout(
    title='<b>DeMar DeRozan<b>' + ' FGM<br>' + '<i>2020-21 Season<i>',
    showlegend=True,
    xaxis=dict(
        showgrid=False,
        range=[-300, 300]
    ),
    yaxis=dict(
        showgrid=False,
        range=[-100, 500]
    ),
    height=750,
    width=800,
    shapes=court_shapes
)

demar_full_fig = go.Figure(data=data, layout=layout)