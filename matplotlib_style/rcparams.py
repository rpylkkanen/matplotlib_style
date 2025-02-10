import matplotlib
from cycler import cycler

# Misc
matplotlib.rcParams['axes.prop_cycle'] = cycler('color', ['#00897b' '#fb8c00' '#8e24aa'])
matplotlib.rcParams['legend.frameon'] = False
matplotlib.rcParams['path.snap'] = False

# Font sizes
fontsize = 18
matplotlib.rcParams['font.size'] = fontsize
matplotlib.rcParams['axes.labelsize'] = fontsize - 1
matplotlib.rcParams['xtick.labelsize'] = fontsize - 4
matplotlib.rcParams['ytick.labelsize'] = fontsize - 4
matplotlib.rcParams['legend.fontsize'] = fontsize - 6
matplotlib.rcParams['axes.titlesize'] = 'medium'

# Paddings
matplotlib.rcParams['ytick.major.pad'] = 1
matplotlib.rcParams['ytick.minor.pad'] = 1
matplotlib.rcParams['axes.labelpad'] = 3
matplotlib.rcParams['axes.titlepad'] = 6
matplotlib.rcParams['legend.borderpad'] = 0
matplotlib.rcParams['legend.labelspacing'] = 0.25
matplotlib.rcParams['legend.handlelength'] = 0.8
matplotlib.rcParams['legend.handleheight'] = 0.25
matplotlib.rcParams['legend.handletextpad'] = 0.5
matplotlib.rcParams['legend.borderaxespad'] = 0.5

# Ticks
matplotlib.rcParams['xtick.direction']      = 'out'
matplotlib.rcParams['ytick.direction']      = 'out'
matplotlib.rcParams['xtick.minor.visible']  = True
matplotlib.rcParams['ytick.minor.visible']  = True
matplotlib.rcParams['xtick.top']            = False
matplotlib.rcParams['ytick.right']          = False

# Line sizes
matplotlib.rcParams['axes.linewidth'] = 1.2
matplotlib.rcParams['xtick.major.width'] = matplotlib.rcParams['axes.linewidth'] 
matplotlib.rcParams['xtick.minor.width'] = matplotlib.rcParams['axes.linewidth'] 
matplotlib.rcParams['ytick.major.width'] = matplotlib.rcParams['axes.linewidth'] 
matplotlib.rcParams['ytick.minor.width'] = matplotlib.rcParams['axes.linewidth'] 
matplotlib.rcParams['lines.linewidth'] = matplotlib.rcParams['axes.linewidth'] * 2
matplotlib.rcParams['patch.linewidth'] = matplotlib.rcParams['axes.linewidth'] * 2
matplotlib.rcParams['hatch.linewidth'] = matplotlib.rcParams['axes.linewidth'] * 2
matplotlib.rcParams['boxplot.flierprops.linewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['boxplot.boxprops.linewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['boxplot.whiskerprops.linewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['boxplot.capprops.linewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['boxplot.medianprops.linewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['boxplot.meanprops.linewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['grid.linewidth'] = matplotlib.rcParams['axes.linewidth']

# Markers
matplotlib.rcParams['lines.markersize'] = 8
matplotlib.rcParams['errorbar.capsize'] = matplotlib.rcParams['lines.markersize'] / 2
matplotlib.rcParams['lines.markerfacecolor'] = 'white'
matplotlib.rcParams['lines.markeredgewidth'] = matplotlib.rcParams['axes.linewidth'] * 1.5
matplotlib.rcParams['xtick.major.size'] = matplotlib.rcParams['lines.markersize'] * 2/3
matplotlib.rcParams['xtick.minor.size'] = matplotlib.rcParams['lines.markersize'] * 1/3
matplotlib.rcParams['ytick.major.size'] = matplotlib.rcParams['lines.markersize'] * 2/3
matplotlib.rcParams['ytick.minor.size'] = matplotlib.rcParams['lines.markersize'] * 1/3