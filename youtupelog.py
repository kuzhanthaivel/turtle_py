import turtle

# set up the turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# draw the red rectangle
t.color("red")
t.begin_fill()
t.fd(200)
t.rt(90)
t.fd(50)
t.rt(90)
t.fd(200)
t.rt(90)
t.fd(50)
t.end_fill()

# move to the starting position of the triangle
t.penup()
t.goto(50, 25)
t.pendown()

# draw the white triangle
t.color("white")
t.begin_fill()
t.rt(30)
t.fd(70.71)
t.rt(120)
t.fd(141.42)
t.rt(120)
t.fd(70.71)
t.end_fill()

# move to the starting position of the play button
t.penup()
t.goto(70, 0)
t.pendown()

# draw the black play button triangle
t.color("black")
t.begin_fill()
t.rt(36.87)
t.fd(35.36)
t.lt(72.53)
t.fd(35.36)
t.lt(144.07)
t.fd(70.71)
t.end_fill()

# hide the turtle
t.hideturtle()

# keep the window open until it's closed
turtle.done()
