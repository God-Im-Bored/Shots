from nba_api.stats.endpoints import shotchartdetail
import pandas as pd
import json
import pandas as pd
import plotly.graph_objs as go
from kawhi_shot import court_shapes

response = shotchartdetail.ShotChartDetail(
        team_id=0,
        player_id=1627732,
        season_nullable='2020-21',
        season_type_all_star='Regular Season'
)
ben_data = json.loads(response.get_json())

results = ben_data['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
ben_df = pd.DataFrame(rows)
ben_df.columns = headers

ben_df.to_csv(r'/home/aram/Downloads/ben.csv', index=False)

ben_df = pd.read_csv('/home/aram/Downloads/ben.csv', encoding='Latin-1')

trace_shot = go.Scatter(
        x = ben_df['LOC_X'],
        y = ben_df['LOC_Y'],
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
    title='<b>Ben Simmons<b>' + ' FGM<br>' + '<i>2020-21 Season<i>',
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

ben_full_fig = go.Figure(data=data, layout=layout)