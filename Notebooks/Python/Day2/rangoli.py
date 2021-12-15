import turtle
p = turtle.Pen()
p.color('red', 'yellow')
p.speed(0)
p.begin_fill()

for counter in range(300):
	p.forward(350)
	p.left(171)

p.end_fill()
turtle.exitonclick()