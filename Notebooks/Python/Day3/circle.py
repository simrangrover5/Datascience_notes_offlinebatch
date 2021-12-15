import turtle

colors = [ "#feae51", "#98b2d1",  "#b35f44", "#f3df4d", "#3078b4",
           "#9fdbad", "#ec8b83", "#00a779", "#9369a8", "#cd4a77" ]

pen = turtle.Pen()

x, y = 0, -200

radius = 200

for color in colors:
    pen.up()
    pen.goto(x, y)
    pen.down()
    
    pen.color('black', color)
    pen.begin_fill()
    pen.circle( radius )
    pen.end_fill()
    
    radius = radius - 20
    y = y + 20
    
turtle.exitonclick()
