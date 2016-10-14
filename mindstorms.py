import turtle

def draw_art():
	window = turtle.Screen()
	window.bgcolor('red')

	brad = turtle.Turtle()
	brad.color('yellow')
	brad.shape('turtle')
	brad.speed(2)
	draw_triangle(brad)
	for i in range(0,36):
		brad.right(10)
		draw_triangle(brad)



	window.exitonclick()



def draw_triangle(some_turtle):
	for i in range(0,3):
		some_turtle.backward(100)
		some_turtle.right(120)

	

draw_art()	
