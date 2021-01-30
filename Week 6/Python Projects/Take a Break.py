import turtle
def draw():
	window = turtle.Screen()
	window.bgcolor("blue")

	b = turtle.Turtle()
	b.forward(100)
	b.right(90)
	b.forward(100)
	b.right(90)
	b.forward(100)
	b.right(90)
	b.forward(100)
	b.right(15)

	window.exitonclick()

i=0
while i>50:
	draw()
	i=i+1