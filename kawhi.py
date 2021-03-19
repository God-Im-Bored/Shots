from nba_api.stats.endpoints import shotchartdetail
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import  OffsetImage
import seaborn as sns
import urllib.request
import json
from court import court

# retrieve JSON: using the nba_api package and shot chart detail api endpoint
response = shotchartdetail.ShotChartDetail(
        team_id=0,
        player_id=202695,
        season_nullable='2020-21',
        season_type_all_star='Regular Season'
)
kawhi_data = json.loads(response.get_json())

# transform the JSON into Pandas dataframe
results = kawhi_data['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
kawhi_df = pd.DataFrame(rows)
kawhi_df.columns = headers

# write new dataframe to csv file
kawhi_df.to_csv(r'/home/aram/Downloads/kawhi.csv', index=False)

# plot makes over sns white-space
sns.set_style('white')
sns.set_color_codes()
plt.figure(figsize=(12,11))
fig_kawhi = plt.scatter(kawhi_df.LOC_X, kawhi_df.LOC_Y)
court()

# invert court to show accurate orientation
plt.xlim(-250,250)
plt.ylim(422.5, -47.5)

# show df superimposed onto drawn court
plt.show()

# grab player's image from url --> read image from file into multi-D array --> plot the image 
pic = urllib.request.urlretrieve('https://cdn.nba.com/headshots/nba/latest/1040x760/202695.png')
kawhi_pic = plt.imread(pic[0])
plt.imshow(kawhi_pic)

# Creating a jointplot
cmap=plt.cm.Greens

# n_levels sets the number of countour lines for the main kde plot
shot_chart = sns.jointplot(kawhi_df.LOC_X, kawhi_df.LOC_Y, kind='scatter', space=0, color=cmap(.8), cmap=cmap)
shot_chart.fig.set_size_inches(12,11)

# draw court onto ax_joint axis
ax = shot_chart.ax_joint
court(ax)

# adjust orientation of court/halcourt --> hoop at the top of the plot
ax.set_xlim(-250,250)
ax.set_ylim(422.5, -47.5)

# remove tick marks and axis lavels
ax.set_xlabel('')
ax.set_ylabel('')
ax.tick_params(labelbottom='off', labelleft='off')

# add title
ax.set_title('Kawhi Leonard FGM \n2020-21 Reg. Season', y=1.2, fontsize=18)

# add data source and author
ax.text(-250, 465, 'Data source: stats.nba.com' '\nAuthor: Aram Martin', fontsize=12)

# add image to the top right of our graph
img = OffsetImage(kawhi_pic, zoom=0.2)
img.set_offset((625, 650))

# add image
ax.add_artist(img)

plt.show()


