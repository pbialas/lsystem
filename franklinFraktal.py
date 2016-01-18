

import turtle

def Koch(turtl, size, step):
	if step == 0:
		turtl.fd(size)
	else:
		Koch(turtl, size/3, step-1)
		turtl.left(60)
		Koch(turtl, size/3, step-1)
		turtl.right(120)
		Koch(turtl, size/3, step-1)
		turtl.left(60)
		Koch(turtl, size/3, step-1)


def KochQudratic(turtl, size, step):
	if step == 0:
		turtl.fd(size)
	else:
		KochQudratic(turtl, size, step-1)
		turtl.left(90)
		KochQudratic(turtl, size, step-1)
		turtl.right(90)
		KochQudratic(turtl, size, step-1)
		turtl.right(90)
		KochQudratic(turtl, size, step-1)
		turtl.left(90)
		KochQudratic(turtl, size, step-1)

def KochQudratic2(turtl, size, step):
	if step == 0:
		turtl.fd(size)
	else:
		KochQudratic2(turtl, size, step-1)
		turtl.left(90)
		KochQudratic2(turtl, size, step-1)
		turtl.right(90)
		KochQudratic2(turtl, size, step-1)
		turtl.right(90)
		KochQudratic2(turtl, size, step-1)
		KochQudratic2(turtl, size, step-1)
		turtl.left(90)
		KochQudratic2(turtl, size, step-1)
		turtl.left(90)
		KochQudratic2(turtl, size, step-1)
		turtl.right(90)
		KochQudratic2(turtl, size, step-1)

def PentaKoch(turl, size, step, params = [2, 1, 45]):
	if step == 0:
		turl.fd(size)
	else:
		PentaKoch(turl, size, step-1)
		turl.right(params[2])
		PentaKoch(turl, size/params[0], step-1)
		turl.right(params[2])
		PentaKoch(turl, size/params[1], step-1)
		turl.right(params[2])
		PentaKoch(turl, size/params[0], step-1)
		turl.right(params[2])
		PentaKoch(turl, size, step-1)


def franklinBegin():
		turtle.screensize(3000, 3000)
		turtle.clearscreen()
		turtle.bgcolor('black')
		franklin = turtle.Turtle(visible = False)
		franklin.color('green', 'green')
		franklin.speed(0)
		return franklin

