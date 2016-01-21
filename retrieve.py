# import modules
import shelve
from player import Player
#import regex
import requests
import pandas as pd
import matplotlib.pyplot as plt
import urllib
import seaborn as sns
from matplotlib.offsetbox import OffsetImage
from court import Draw_court
from visualize import Visualize, HeatMap
import re

#%matplotlib inline

# open the shelve that stored the player-id pair
db = shelve.open('HRroster-shelve')

# let user input player name
name_raw = raw_input('Input player last name:\n==>')

input_name = name_raw.lower()
try:
	db[input_name]
except:
	print '!!No such player!!'

# let user input the season
season_raw = raw_input('Season (in yyyy format):\n==>')
# TODO: check season format with regex
# try:
# 	^[12][0-9].+?
# except:
#	print 'Wrong season input!'
season = season_raw+'-'+str((int(season_raw)+1))[-2:]

# use the input content to compose the url
url = ('http://stats.nba.com/stats/shotchartdetail?CFID=33&'
	   'CFPARAMS=%s&'
	   'ContextFilter=&ContextMeasure=FGA&DateFrom=&DateTo=&GameID=&'
	   'GameSegment=&LastNGames=0&LeagueID=00&Location=&'
	   'MeasureType=Base&'
	   'Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&'
	   'PerMode=PerGame&Period=0&'
	   'PlayerID=%s&'
	   'PlusMinus=N&Position=&Rank=N&RookieYear=&'
	   'Season=%s&SeasonSegment=&SeasonType=Regular+Season&TeamID=0&'
	   'VsConference=&VsDivision=&mode=Advanced&showDetails=0&'
	   'showShots=1&showZones=0' %(season, db[input_name].ID, season))


# params = {'CFPARAMS': season, 'ContextFilter':''}

# fetch data using the requests module
# response = requests.get(url, params)
response = requests.get(url)
response.raise_for_status()
response.json()
# create a pandas dataframe from the returned json file
headers = response.json()['resultSets'][0]['headers']
shots = response.json()['resultSets'][0]['rowSet']
shot_df = pd.DataFrame(shots, columns = headers)

# sanity check
# print shot_df.head()

# separate the shots made from the shots missed shots
made = shot_df[shot_df['SHOT_MADE_FLAG'] == 1]
miss = shot_df[shot_df['SHOT_MADE_FLAG'] == 0]
# fetch a photo of the player
pic = urllib.urlretrieve('http://stats.nba.com/media/players/'
						 '230x185/%s.png' %(db[input_name].ID))
# sanity check of photo
player_pic = plt.imread(pic[0])
# fig, ax = plt.subplots(figsize = (5,5))
# ax.imshow(player_pic)
# ax.set_axis_off()
# plt.show()}

Visualize(made.LOC_X, made.LOC_Y,
	      miss.LOC_X, miss.LOC_Y,
	      pic = player_pic,
	      name = input_name,
	      season_str = season)
HeatMap(shot_df.LOC_X, shot_df.LOC_Y,
		pic = player_pic,
	    name = input_name,
	    season_str = season)

