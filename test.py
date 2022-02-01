import matplotlib_style

for name, values in matplotlib_style.colors.items():
	print(f'{name}:')
	for index, value in values.items():
		print(f'  {index}: {value}')