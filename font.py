import os
import matplotlib.font_manager

path = 'TTF'

def setup_font():

	for fname in os.listdir(path):
	  if '.ttf' in fname:
	    name = path + '/' + fname
	    matplotlib.font_manager.fontManager.addfont(name)
	    prop = matplotlib.font_manager.FontProperties(fname=name)
	    name = prop.get_name()
	    if name != matplotlib.rcParams['font.sans-serif'][0]:
	      matplotlib.rcParams['font.sans-serif'].insert(0, name)

	matplotlib.rcParams['mathtext.fontset'] = 'custom'
	for font in ['rm', 'bf', 'it', 'cal', 'sf', 'tt']:
	  matplotlib.rcParams[f'mathtext.{font}'] = name