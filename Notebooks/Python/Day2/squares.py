import turtle
import random

colors = [ 'red', 'green', 'blue', 
'cyan', 'magenta', 'gold', 'silver', 'yellow' ]

pen = turtle.Pen()

x = -200
y = 200

width = 400

for c in range(10):
	pen.up()
	pen.goto(x, y)
	pen.down()
	
	pen.color('black', random.choice(colors))
	pen.begin_fill()

	for _ in range(4):
		pen.forward(width)
		pen.right(90)
	
	pen.end_fill()

	x = x + 20
	y = y - 20
	width = width - 40

turtle.exitonclick()


