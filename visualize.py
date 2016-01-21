import matplotlib.pyplot as plt
import seaborn as sns
from court import Draw_court
from matplotlib.offsetbox import OffsetImage

def Visualize(made_x, made_y, 
			  miss_x, miss_y, 
			  pic = None,
			  name = 'Somebody',
			  season_str = '-1'):
	'''
	made_x: x coordinate of the made shots
	made_y: y coordiante of the made shots
	miss_x: x coordinate of the missed shots
	miss_y: y coordinate of teh missed shots
	pic: the image object of the player
	'''
	fig1 = plt.figure(figsize=(12,11))
	ax = fig1.add_subplot((111))
	Draw_court(outer_lines=True)
	ax.scatter(made_x, made_y, marker = 'o',
           	   color = 'DodgerBlue', s = 20)
	ax.scatter(miss_x, miss_y, marker = 'x',
               color = '#B80000', s = 20, linewidth = 1)
	plt.xlim(-300,300)
	plt.ylim(422.5, -47.5)
	ax.set_axis_off()
	img = OffsetImage(pic, zoom=0.6)
	img.set_offset((20,610))
	ax.add_artist(img)
	ax.set_title('Shooting Chart of %s '
		         'in season %s' %(name.capitalize(), season_str),
				  fontsize = 20)
	ax.set_axis_bgcolor('r')
	plt.show()


def HeatMap(shot_x, shot_y,
			pic = None,
			name = 'Somebody',
			season_str = '-1'):
	cmap = plt.cm.coolwarm
	joint_shot_chart = sns.jointplot(shot_x, shot_y,
									 stat_func=None, kind='kde',
									 space=0, color = cmap(0.8),
	                                 cmap='coolwarm', n_levels=40)
	joint_shot_chart.fig.set_size_inches(16,14)
	ax2 = joint_shot_chart.ax_joint
	# Draw the court
	Draw_court(ax2)
	# set lat and lon
	ax2.set_xlim(-300,300)
	ax2.set_ylim(422.5, -47.5)
	# turn off the labels
	ax2.set_xlabel('')
	ax2.set_ylabel('')
	ax2.tick_params(labelbottom='off', labelleft='off')
	# add photo
	img = OffsetImage(pic, zoom=0.6)
	img.set_offset((625,630))
	ax2.add_artist(img)
	ax2.set_title('Shooting Chart of %s '
		          'in season %s' %(name.capitalize(), season_str),
				  fontsize = 20)
	plt.show()