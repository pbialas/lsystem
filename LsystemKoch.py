

import turtle

def Koch(turtl, size, step):
	base = 'F'
	for i in range(step):
		new_base = ''
		for char in base:
			if char == 'F':
				new_base += 'F+F-F-F+F'
			else:
				new_base += char
		base = new_base
	for char in base:
		if char == 'F':
			turtl.forward(size)
		elif char == '+':
			turtl.left(90)
		elif char == '-':
			turtl.right(90)


def Sierpinski(turtl, size, step):
	base = 'A'
	for i in range(step):
		new_base = ''
		for char in base:
			if char == 'A':
				new_base += '+B-A-B+'
			elif char == 'B':
				new_base += '-A+B+A-'
			else:
				new_base += char
		base = new_base
	for char in base:
		if char == 'A' or char == 'B':
			turtl.forward(size)
		elif char == '+':
			turtl.left(60)
		elif char == '-':
			turtl.right(60)


def Dragon_curve(turtl, size, step):
	base = 'FX'
	for i in range(step):
		new_base = ''
		for char in base:
			if char == 'X':
				new_base += 'X+YF+'
			elif char == 'Y':
				new_base += '-FX-Y'
			else:
				new_base += char
		base = new_base
	for char in base:
		if char == 'F':
			turtl.forward(size)
		elif char == '+':
			turtl.left(90)
		elif char == '-':
			turtl.right(90)


def Fractal_plant(turtl, size, step):
	base = 'X'
	for i in range(step):
		new_base = ''
		for char in base:
			if char == 'X':
				new_base += 'F-[[X]+X]+F[+FX]-X'
			elif char == 'F':
				new_base += 'FF'
			else:
				new_base += char
		base = new_base
	ls = []
	turtl.setheading(90)
	for char in base:
		if char == 'F':
			turtl.forward(size)
		elif char == '[':
			ls.append(turtl.clone())
		elif char == ']':
			turtl = ls.pop()
		elif char == '+':
			turtl.left(25)
		elif char == '-':
			turtl.right(25)


def franklinBegin():
		turtle.screensize(3000, 3000)
		turtle.clearscreen()
		turtle.bgcolor('black')
		franklin = turtle.Turtle(visible = False)
		franklin.color('green', 'green')
		franklin.speed(0)
		return franklin
