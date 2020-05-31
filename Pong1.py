import turtle
import os # interact with operating systems through text commands

wn = turtle.Screen()
wn.title("Ping-Pong game by @Josh")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)


#Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3 #every time, when the ball moves, it will move 3 pixells to x direction
ball.dy = -3

# Score Pen 
pen = turtle.Turtle()
pen.speed(0) # Animation Speed
pen.color("white")
pen.penup() 
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align = "center", font = ("Courier", 24, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor() #get the y-coordinate
    y += 20 #add 20 to the y-coordinate
    paddle_a.sety(y) #set the y paddle to the new y-coordinate

def paddle_a_down():
    y = paddle_a.ycor() #get the y-coordinate
    y -= 20 #subtract 20 to the y-coordinate
    paddle_a.sety(y) #set the y paddle to the new y-coordinate

def paddle_b_up():
    y = paddle_b.ycor() #get the y-coordinate
    y += 20 #add 20 to the y-coordinate
    paddle_b.sety(y) #set the y paddle to the new y-coordinate

def paddle_b_down():
    y = paddle_b.ycor() #get the y-coordinate
    y -= 20 #subtract 20 to the y-coordinate
    paddle_b.sety(y) #set the y paddle to the new y-coordinate

    

# Keybord binding
wn.listen() # listen keybord input
wn.onkeypress(paddle_a_up, "w") # when user press "w", call the function paddle_a_up
wn.onkeypress(paddle_a_down, "s") # when user press "s", call the function paddle_a_down

wn.onkeypress(paddle_b_up, "Up") # when user press "Up" key, call the function paddle_b_up
wn.onkeypress(paddle_b_down, "Down") # when user press "Down" key, call the function paddle_b_down


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx) #first time the ball moves 2, and next moves more 2, 2, 2, 2
    ball.sety(ball.ycor() + ball.dy)


    # Border Checking (make the ball to bounce)
    if ball.ycor() > 290: # if hit the top border, it will bounce
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290: # if hit the down border, it will bounce
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390: # if hit the right border, the ball will move on to the center
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear() # If we did not do this, score 1 will be not mixed with 0
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))


    if ball.xcor() < -390: # if hit the left border, the ball will move on to the center
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))


    
    # Paddle and Ball Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    