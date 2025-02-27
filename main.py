import turtle as t
import os
import winsound

playerAscore = 0
playerBscore = 0

# window
window = t.Screen()
window.title("The Pong Game")
window.bgcolor("lightblue")
window.setup(width=800, height=600)
window.tracer(0)

# left paddle
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

# right paddle
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

# creating ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.shapesize(stretch_wid=1.5, stretch_len=1.5)
ball.goto(5,5)
ballxdirection = 0.1
ballydirection = 0.1

# pen for scorecard update
pen = t.Turtle()
pen.speed(0)
pen.color("Black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score", align="center", font=('Arial', 24, 'normal'))

# moving the left paddle
def leftpaddleup():
    y = leftpaddle.ycor()
    y = y + 90
    leftpaddle.sety(y)

def leftpaddledown():
    y = leftpaddle.ycor()
    y = y - 90
    leftpaddle.sety(y)

# moving the right paddle
def rightpaddleup():
    y = rightpaddle.ycor()
    y = y + 90
    rightpaddle.sety(y)

def rightpaddledown():
    y = rightpaddle.ycor()
    y = y - 90
    rightpaddle.sety(y)

# assign keys to play
window.listen()
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')

while True:
    window.update()

    # moving ball
    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)

    # border set up
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection = ballydirection * -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection = ballydirection * -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ballxdirection = ballxdirection * -1
        playerAscore = playerAscore + 1
        pen.clear()
        pen.write(" Player A: {}                 Player B: {} ".format(playerAscore, playerBscore), align="center", font=('Monaco', 24, "normal"))
        winsound.PlaySound("wallhit.wav", winsound.SND_ASYNC)

    if (ball.xcor()) < -390:  # Left width paddle Border
        ball.goto(0, 0)
        ballxdirection = ballxdirection * -1
        playerBscore = playerBscore + 1
        pen.clear()
        pen.write(" Player A: {}                 Player B: {} ".format(playerAscore, playerBscore), align="center", font=('Monaco', 24, "normal"))
        winsound.PlaySound("wallhit.wav", winsound.SND_ASYNC)

    if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 50 and ball.ycor() > rightpaddle.ycor() - 50):
        ball.setx(340)
        ballxdirection = ballxdirection * -1
        winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 50 and ball.ycor() > leftpaddle.ycor() - 50):
        ball.setx(-340)
        ballxdirection = ballxdirection * -1
        winsound.PlaySound("paddle.wav", winsound.SND_ASYNC)