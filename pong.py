import turtle


window= turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)


#scoreboard:
score_a=0
score_b=0

#paddle A

paddle_a= turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)


#paddle b

paddle_b= turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)


#ball


ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.2
ball.dy=0.2


#score:
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier",20, "bold"))



#functions:

#for paddle A

def paddle_a_up():
    y= paddle_a.ycor()
    y+= 20
    paddle_a.sety(y)

def paddle_a_down():
    y= paddle_a.ycor()
    y-= 20
    paddle_a.sety(y)

#for paddle B

def paddle_b_up():
    y= paddle_b.ycor()
    y+= 20
    paddle_b.sety(y)

def paddle_b_down():
    y= paddle_b.ycor()
    y-= 20
    paddle_b.sety(y)




#keyboard binding

window.listen()
window.onkeypress(paddle_a_up,"w")
window.onkeypress(paddle_a_down,"s")
window.onkeypress(paddle_b_up,"Up")
window.onkeypress(paddle_b_down,"Down")

#main game loop
while True:
    window.update()

#move the ball
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

#border checking:


    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1
    
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier",20, "bold"))


    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier",20, "bold"))

    


    if (ball.xcor() >340 and ball.xcor() <350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1

    if score_a== 10:
        ball.dx=0
        ball.dy=0
        pen.goto(0,0)
        pen.write("Player A wins!! :)", align="center", font=("Courier",40, "bold"))

    if score_b== 10:
        ball.dx=0
        ball.dy=0
        pen.goto(0,0)
        pen.write("Player B wins!! :)", align="center", font=("Courier",40, "bold"))

    

    




