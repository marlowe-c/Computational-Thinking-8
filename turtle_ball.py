# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite.shape(image_file)
def create_sprite(image_filename, x=0, y=0):
	sprite = turtle.Turtle()
	set_image(sprite, image_filename)
	sprite.penup()
	sprite.goto(x,y)
	return sprite
def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)
window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
s1 = create_sprite("crush (1) (1)",0,-120)
s2 = create_sprite("vball (1)",-50,150)
set_background("court (1)")

s1.setheading(90)
def move_up():
	s1.setheading(90)
	s1.forward(15)

# Section 3: Controls
def Left():
	s1.setheading(180)
	s1.forward(10)
def Right():
	s1.setheading(0)
	s1.forward(10)
window.onkeypress(Left, "a")
window.onkeypress(Right, "d")


# Section 4: Game Loop
window.listen()
timer = 0
score = 0
while True:
	time.sleep(0.1)
	timer += 1  
	s2.setheading(270)
	s2.forward(8)
	if s2.ycor() < -300:
		s2.goto(random.randint(-200,200),100) 
		s2.showturtle()

	if get_distance (s1,s2) < 50:
		score += 1
		s2.goto(random.randint(-50,50),100) 


	if score == 10 :
		s1.write("GAME OVER",font = ("Arial", 40, "normal"))
		break

	 
    
 	# TODO - code for automatic actions






	window.update()

