import matplotlib
from cycler import cycler

# blue, orange, green, red, purple, brown, pink, grey, yellow, teal
matplotlib.rcParams['axes.prop_cycle'] = cycler('color', ['#2196f3', '#ff9800', '#4caf50', '#f44336'])
matplotlib.rcParams['lines.linewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['lines.markersize'] = 4.5
matplotlib.rcParams['errorbar.capsize'] = matplotlib.rcParams['lines.markersize'] / 2
matplotlib.rcParams['lines.markerfacecolor'] = 'white'
matplotlib.rcParams['lines.markeredgewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['patch.linewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['hatch.linewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['boxplot.flierprops.linewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['boxplot.boxprops.linewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['boxplot.whiskerprops.linewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['boxplot.capprops.linewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['boxplot.medianprops.linewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['boxplot.meanprops.linewidth'] = matplotlib.rcParams['axes.linewidth']
matplotlib.rcParams['grid.linewidth'] = matplotlib.rcParams['axes.linewidth']