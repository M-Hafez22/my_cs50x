import turtle

def square(length, background_color):
	#drawing a single square
	window = turtle.Screen()
	window.bgcolor(background_color)
	turtle.color("blue")
	turtle.shape("square")
	turtle.speed(10)

	i = 0
	while i <4 :
		turtle.forward(length)
		turtle.right(90)
		i += 1
#testing square
#square(200,"yellow")

def circle_of_squares(length, background_color,angle):
	#drawing circle of squares with the square()
	window = turtle.Screen()
	window.bgcolor(background_color)
	for i in range(0,360,angle):
		square(length, background_color)
		turtle.left(angle)

	window.exitonclick()

#circle_of_squares(100,"red",15)



def draw_square(some_turtle):
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_circle(some_turtle):
	turtle.color("blue")
	turtle.shape("square")
	turtle.speed(10)

	some_turtle.circle(100)


def draw_square_and_circle():
	window = turtle.Screen()
	window.bgcolor("yellow")

	shape = turtle.Turtle()
	shape.shape("turtle")
	shape.color("blue")
	shape.speed(2)
	draw_square(shape)
	draw_circle(shape)

	window.exitonclick()
draw_square_and_circle()

def draw_circle():
	window = turtle.Screen()
	window.bgcolor("blue")
	turtle.color("blue")
	turtle.shape("square")
	turtle.speed(10)

	b = turtle.Turtle()
	b.circle(100)
	window.exitonclick()

#draw_circle()
