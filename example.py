import matplotlib.pyplot
from color import colors
from font import setup_font
import numpy

setup_font()

n = 100
x = numpy.linspace(-50, 50, num=n)

fig, ax = matplotlib.pyplot.subplots()

for i, (name, array) in enumerate(colors.items()):
	a = - 1
	b = 0
	c = - 2 * n * i
	y = a * x ** 2 + b * x + c
	color = array[5]
	label = f'color[{name}][5]'
	ax.plot(
		x, 
		y,
		color=color, 
		label=label,
	)

title = matplotlib.rcParams['font.sans-serif'][0]
ax.set_title(title)
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')

print()

loc = 'center'
bbox_to_anchor = (1.05, 0.5)
fig.legend(
	loc=loc,
	bbox_to_anchor=bbox_to_anchor,
)

fig.savefig('example.png', bbox_inches='tight', figsize=(3, 3), dpi=100)