

import turtle

class Lsystem:
	def __init__(self, forward_symbols, rules, start, angle, heading=0):
		self.fd = forward_symbols
		self.rules = rules
		self.start = start
		self.angle = angle
		self.head = heading

	def get_step(self, step):
		base = self.start
		for i in range(step):
			new_base = ''
			for char in base:
				if char in self.rules.keys():
					new_base += self.rules[char]
				else:
					new_base += char
			base = new_base
		return base

	def draw(self, turtl, size, step):
		base = self.get_step(step)
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
		return franklin
