import matplotlib
from cycler import cycler

matplotlib.rcParams['font.size'] = 7
matplotlib.rcParams['axes.labelsize'] = 7
matplotlib.rcParams['xtick.labelsize'] = 7
matplotlib.rcParams['ytick.labelsize'] = 7
matplotlib.rcParams['legend.fontsize'] = 7
matplotlib.rcParams['legend.frameon'] = False

matplotlib.rcParams['xtick.direction']      = 'out'
matplotlib.rcParams['ytick.direction']      = 'out'
matplotlib.rcParams['xtick.minor.visible']  = True
matplotlib.rcParams['ytick.minor.visible']  = True
matplotlib.rcParams['xtick.top']            = False
matplotlib.rcParams['ytick.right']          = False

# blue, orange, green, red, purple, brown, pink, grey, yellow, teal
matplotlib.rcParams['axes.prop_cycle'] = cycler('color', ['#d32f2f', '#1976d2', '#388e3c', '#f57c00', '#7b1fa2', '#fbc02d'])

matplotlib.rcParams['lines.markersize'] = 3.0
matplotlib.rcParams['errorbar.capsize'] = matplotlib.rcParams['lines.markersize'] / 2
matplotlib.rcParams['lines.markerfacecolor'] = 'white'
matplotlib.rcParams['lines.markeredgewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['xtick.major.size'] = matplotlib.rcParams['lines.markersize']
matplotlib.rcParams['xtick.minor.size'] = matplotlib.rcParams['lines.markersize'] / 2
matplotlib.rcParams['ytick.major.size'] = matplotlib.rcParams['lines.markersize']
matplotlib.rcParams['ytick.minor.size'] = matplotlib.rcParams['lines.markersize'] / 2

matplotlib.rcParams['axes.linewidth'] = 0.5
matplotlib.rcParams['xtick.major.width'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['xtick.minor.width'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['ytick.major.width'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['ytick.minor.width'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['lines.linewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['patch.linewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['hatch.linewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['boxplot.flierprops.linewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['boxplot.boxprops.linewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['boxplot.whiskerprops.linewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['boxplot.capprops.linewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['boxplot.medianprops.linewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['boxplot.meanprops.linewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['grid.linewidth'] = matplotlib.rcParams['axes.linewidth']