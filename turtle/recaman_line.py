import turtle

window = turtle.Screen()
window.setup(width=800, height=600, startx=10, starty=0.5)
dot = turtle.Turtle()
dot.shape("turtle")
scale = 5

# translate to start on left side
dot.penup()
dot.setpos(-390, 0)
dot.pendown()

current = 0
seen = set()

for step_size in range(100):
	backwards = current - step_size

	if backwards > 0 and backwards not in seen:
		dot.setheading(180)
		dot.penup()
		dot.forward(scale * step_size/2)
		dot.pendown()
		dot.setheading(90)
		dot.forward(scale * step_size/2)
		dot.penup()
		dot.setheading(270)
		dot.forward(scale * step_size/2)
		dot.pendown()
		current = backwards
		seen.add(current)
	else:
		dot.setheading(0)
		dot.penup()
		dot.forward(scale * step_size/2)
		dot.pendown()
		dot.setheading(270)
		dot.forward(scale * step_size/2)
		dot.penup()
		dot.setheading(90)
		dot.forward(scale * step_size/2)
		dot.pendown()
		current += step_size
		seen.add(current)


turtle.done()
