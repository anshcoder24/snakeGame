import turtle
import random
import time
import tkinter as tk


delay= 0.1
score=0
heighestscore=0
# snake bodies
bodies=[]
# getting a screen  | canvas
s=turtle.Screen()
s.title("Snake game")
s.bgcolor("gray")
s.setup(width=600, height=600)
s.tracer(0) # Turn off auto-update for smoooth animation

# create a snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("pink")
head.fillcolor("blue")
head.penup()
head.goto(0,0)
head.direction="stop"

# snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.fillcolor("green")
food.penup()
food.ht()
food.goto(0,200)
food.st()

# snake board
sb=turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250,-250)
sb.write("score:0 | heighest score:0")
def moveup():
    if head.direction!="down":
        head.direction="up"
def movedown():
    if head.direction!="up":
        head.direction="down"
def moveleft():
    if head.direction!="right":
        head.direction="left"
def moveright():
    if head.direction!="left":
        head.direction="right"
def movestop():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.ycor()
        head.sety(x-20)
    if head.direction=="right":
        x=head.ycor()
        head.setx(x+20)

# Event hamdling-key mapt
import turtle as t
screen=t.Screen()
s.listen()
s.onkey(moveup,"Up")
s.onkey(movedown,"Down")
s.onkey(moveleft,"Left")
s.onkey(moveright,"Right")
s.onkey(movestop,"space")
t.done()
# main loop
try:
    while True:
       s.update()# update the screen not the turtle
       move()
    #check collission  with border
    #  rest of your screen game code
       t._update_data()
    
    
    if head.xcor()>290:
        head.setx(-290)
    if head.xcor()<-290:
        head.setx(290)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)
# check collision with food
    if head.distance(food)<20:
    #move the food to new random place
     x = random.randint(-290,290)
     y= random.randint(-290,290)
     food.goto(x,y)
     # increase the lenght of the snake 
     body= turtle.Turtle()
     body.speed(0)
     body.penup()
     body.shape("square")
     body.color("red")
     body.fillcolor("black")
     bodies.append(body)# append new body

     # increase the score
     score+=10
     # change delay
     delay-=0.001
     # update the heighest score 
     if score>heighestscore:
        highestscore=score
     sb.clear()
     sb.write("score: {} heighest score: {}". formt(score,heighestscore))
except:
    pass # or print game over
# move the snake bodies 
for index in range (len(bodies)-1,0,-1):
    x=bodies[index-1].xcor()
    y=bodies[index].goto(x,y)

if len(bodies)>0:
    x=head.xcor()
    y=head.ycor()
    bodies[0].goto(x,y)
    move()
# check collision with snake body
for body in bodies:
    if body.distance(head)<20:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        # hide bodies
        for body in bodies:
            body.ht()
        bodies.clear ()

        score=0 
        delay=0.1
        # update score board
        sb.clear()
        sb.writes("score: {} highest score: {}". format(score,heighestscore))
time.sleep(delay)
s.mainloop()
# this is the end of our snake game