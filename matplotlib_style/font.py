import os
import matplotlib.font_manager
import pathlib


print('Adding fonts:')

path = pathlib.Path(__file__).parent.resolve()
path = path / 'TTF'

for fname in os.listdir(path):
  if '.ttf' in fname:
    name = path / fname
    print(name)
    matplotlib.font_manager.fontManager.addfont(str(name))
    prop = matplotlib.font_manager.FontProperties(fname=name)
    name = prop.get_name()
    if name != matplotlib.rcParams['font.sans-serif'][0]:
      matplotlib.rcParams['font.sans-serif'].insert(0, name)

matplotlib.rcParams['mathtext.fontset'] = 'custom'
matplotlib.rcParams[f'mathtext.rm'] = name
matplotlib.rcParams[f'mathtext.bf'] = name + ':bold'
matplotlib.rcParams[f'mathtext.it'] = name
matplotlib.rcParams[f'mathtext.cal'] = name
matplotlib.rcParams[f'mathtext.sf'] = name
matplotlib.rcParams[f'mathtext.tt'] = name