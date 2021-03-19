import pandas as pd
import plotly.graph_objs as go


kawhi_df = pd.read_csv('/home/aram/Downloads/kawhi.csv', encoding='Latin-1')

trace_shot = go.Scatter(
        x = kawhi_df['LOC_X'],
        y = kawhi_df['LOC_Y'],
        mode = 'markers'   
)

data = [trace_shot]
layout = go.Layout(
    showlegend=False,
    height=800,
    width=800
)

fig = go.Figure(data=data, layout=layout)
fig.show()

court_shapes = []

outer_lines_shape = dict(
  type='rect',
  xref='x',
  yref='y',
  x0='-250',
  y0='-47.5',
  x1='250',
  y1='422.5',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1
  )
)

court_shapes.append(outer_lines_shape)
hoop_shape = dict(
  type='circle',
  xref='x',
  yref='y',
  x0='7.5',
  y0='7.5',
  x1='-7.5',
  y1='-7.5',
  line=dict(
    color='rgba(10, 10, 10, 1)',
    width=1
  )
)

court_shapes.append(hoop_shape)
backboard_shape = dict(
  type='rect',
  xref='x',
  yref='y',
  x0='-30',
  y0='-7.5',
  x1='30',
  y1='-6.5',
  line=dict(
    color='rgba(10, 10, 10, 1)',
    width=1
  ),
  fillcolor='rgba(10, 10, 10, 1)'
)

court_shapes.append(backboard_shape)
outer_three_sec_shape = dict(
  type='rect',
  xref='x',
  yref='y',
  x0='-80',
  y0='-47.5',
  x1='80',
  y1='143.5',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1
  )
)

court_shapes.append(outer_three_sec_shape)
inner_three_sec_shape = dict(
  type='rect',
  xref='x',
  yref='y',
  x0='-60',
  y0='-47.5',
  x1='60',
  y1='143.5',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1
  )
)

court_shapes.append(inner_three_sec_shape)
left_line_shape = dict(
  type='line',
  xref='x',
  yref='y',
  x0='-220',
  y0='-47.5',
  x1='-220',
  y1='92.5',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1
  )
)

court_shapes.append(left_line_shape)
right_line_shape = dict(
  type='line',
  xref='x',
  yref='y',
  x0='220',
  y0='-47.5',
  x1='220',
  y1='92.5',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1
  )
)

court_shapes.append(right_line_shape)
three_point_arc_shape = dict(
  type='path',
  xref='x',
  yref='y',
  path='M -220 92.5 C -70 300, 70 300, 220 92.5',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1
  )
)

court_shapes.append(three_point_arc_shape)

center_circle_shape = dict(
  type='circle',
  xref='x',
  yref='y',
  x0='60',
  y0='482.5',
  x1='-60',
  y1='362.5',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1
  )
)

court_shapes.append(center_circle_shape)

res_circle_shape = dict(
  type='circle',
  xref='x',
  yref='y',
  x0='20',
  y0='442.5',
  x1='-20',
  y1='402.5',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1
  )
)

court_shapes.append(res_circle_shape)

free_throw_circle_shape = dict(
  type='circle',
  xref='x',
  yref='y',
  x0='60',
  y0='200',
  x1='-60',
  y1='80',
  line=dict(
      color='rgba(10, 10, 10, 1)',
      width=1
  )
)

court_shapes.append(free_throw_circle_shape)
res_area_shape = dict(
  type='circle',
  xref='x',
  yref='y',
  x0='40',
  y0='40',
  x1='-40',
  y1='-40',
  line=dict(
    color='rgba(10, 10, 10, 1)',
    width=1,
    dash='dot'
  )
)

court_shapes.append(res_area_shape)

trace_shot = go.Scatter(
        x = kawhi_df['LOC_X'],
        y = kawhi_df['LOC_Y'],
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
    title='<b>Kawhi Leonard<b>' + ' FGM<br>' + '<i>2020-21 Season<i>',
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
    shapes=court_shapes,
)



full_fig = go.Figure(data=data, layout=layout)

# full_fig.add_layout_image(
#         dict (
#           source='https://cdn.nba.com/headshots/nba/latest/1040x760/202695.png',
#           x=1, y=1.05,
#           sizex=0.2, sizey=0.2,
#           xanchor='right', yanchor='bottom'
#         )
# )

# full_fig.update_layout(
#         autosize=False,
#         height=800,
#         width=800,
        
# )

# full_fig.show()
