import turtle


def draw_square(some_turtle):
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90)
	

def draw_art(turtle):
	window = turtle.Screen()
	window.bgcolor("green")
	amr = turtle.Turtle()
	amr.shape("turtle")
	amr.color("yellow")
	amr.speed(4)

	i =0
	while i <45 :
		draw_square(turtle)
		turtle.right(15)
		i +=1
	turtle.forward(222)



	window.exitonclick()

#draw_square(turtle)
draw_art(turtle)