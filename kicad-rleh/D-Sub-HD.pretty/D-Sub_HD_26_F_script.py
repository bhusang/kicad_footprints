#!/bin/python3

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

num_rows = 3

x_delta = -2.29

y = [-2.54,
	 0,
	 2.54,
	 ]
y_cnt = [9, 9, 8]
x_start = [-4 * x_delta - 0.51,
		   -4 * x_delta + 0.64,
		   -4 * x_delta - 0.51,
		   ]

p = []

for y_i in range(num_rows):
	for x_i in range(y_cnt[y_i]):
		x = x_start[y_i] + (x_delta * x_i)
		p.append(Point(x, y[y_i]))
#		print('  x_i = {}'.format(x_i))
#	print(' y_i = {}'.format(y_i))

#print('# =========================================')

for pin in range(0,len(p)):
	print('  (pad {} thru_hole circle (at {:.2f} {:.2f}) (size 1.35 1.35) (drill 1.05) (layers *.Cu *.Mask))'.format(pin+1, p[pin].x, p[pin].y))
