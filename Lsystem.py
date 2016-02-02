

import turtle
import random

class Lsystem:
	def __init__(self, forward_symbols, rules, start, angle, heading=0):
		self.fd = forward_symbols
		self.rules = rules
		self.start = start
		self.angle = angle
		self.head = heading

	def get_step(self, step, colors):
		base = self.start
		for i in range(step):
			new_base = ''
			for char in base:
				if char in self.rules.keys():
					new_base += self.rules[char]
				else:
					new_base += char
			base = new_base
		if colors:
			F = lambda ls, k: map(lambda j:ls[(j*len(ls))/k: ((j+1)*len(ls))/k],
                                  range(k))
			base = reduce(lambda x,y: x + y,
                          map(lambda x: x + 'c', F(base, colors)))
		return base

	def draw(self, size, step, colors = 0, so_fast = False, turtl = None):
		if not turtl:
			turtl = franklinBegin()
		base = self.get_step(step, colors = colors)
		angle = self.angle
		ls = []
		turtl.setheading(self.head)
		for char in base:
			if char in self.fd:
				turtl.forward(size)
			elif char == '+':
				turtl.left(angle)
			elif char == '-':
				turtl.right(angle)
			elif char == '[':
				ls.append(turtl.clone())
			elif char == ']':
				turtl = ls.pop()
			elif char == 'R':
				turtl.right(360*random.random())
			elif char == 'c':
					newcolor = (0.3 + 0.7*random.random(),
                                0.3 + 0.7*random.random(),
                                0.3 + 0.7*random.random())
					turtl.color(newcolor, newcolor)
			if not so_fast:
				turtle.update()
		turtle.update()

Koch = Lsystem(['F'], {'F': 'F+F-F-F+F'}, 'F', 90)
Sierpinski = Lsystem(['A', 'B'], {'A': '+B-A-B+', 'B': '-A+B+A-'}, 'A', 60)
Hilbert = Lsystem(['F'], {'X': '+YF-XFX-FY+', 'Y': '-XF+YFY+FX-'}, 'X', 90)
Dragon_curve = Lsystem(['F'], {'X': 'X+YF+', 'Y': '-FX-Y'}, 'FX', 90)
Fractal_plant = Lsystem(['F'], {'X': 'F-[[X]+X]+F[+FX]-X', 'F': 'FF'},
                        'FX', 25, heading = 90)


def franklinBegin():
		turtle.screensize(3000, 3000)
		turtle.clearscreen()
		turtle.bgcolor('black')
		franklin = turtle.Turtle(visible = False)
		franklin.color('green', 'green')
		franklin.speed(0)
		turtle.tracer(0, 0)
		return franklin
