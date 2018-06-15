from p5 import *
from random import randint

bars = 10
bar_h = [1] * bars

def setup():
	size(500, 500)

def draw():
	background(255)
	amount = int(width // bars)
	global bar_h
	fill(0)
	stroke(200)
	for x in range(0, bars):
		rect((x*amount, height), amount, -bar_h[x])
	r_bar = randint(0, bars - 1)
	bar_h[r_bar] += 1
	print(bar_h)

run()