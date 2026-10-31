import turtle
import random
import time

backround_text = turtle.Turtle()
backround_text.speed(1000)
screen = turtle.Screen()
screen.bgcolor("black")
backround_text.hideturtle()
backround_text.color("blue")
backround_text.penup()
backround_text.goto(-130,25)
backround_text.pendown()
backround_text.write("circle", font=("Arial", 50, "bold"))

backround_text.color("red")
backround_text.penup()
backround_text.goto(-130,-25)
backround_text.pendown()
backround_text.write("catcher", font=("Arial", 50, "bold"))

backround_text.color("white")
backround_text.penup()
backround_text.goto(-130,-100)
backround_text.pendown()
backround_text.write("press space bar to start the game", font=("Arial", 14, "bold"))

start = 0
def start_game():
    global start
    start = 1
    return start
screen.listen()
screen.onkey(start_game, "space")
run = True
while run:
 if start == 1:
  run = False  
  backround_text.clear()
  turtle.hideturtle()
  screen.bgcolor("lightblue")
  player = turtle.Turtle()
  circle = turtle.Turtle()
  circle.speed(1000)
  player.penup()

  score = 0
  speed = 1
  game_over = 0
  checker = 0

  turtle.penup()
  turtle.goto(-100,100)
  turtle.pendown()
  turtle.write("Score: " + str(score), font=("Arial", 16, "bold"))

  def circle_function():
   circle.clear()
   circle_x = random.randint(-180,180)
   circle_y = random.randint(-180,180)
   circle.penup()
   circle.goto(circle_x,circle_y)
   circle.dot(50)

 
  circle_function()

  def move():
   global score
   global speed
   global game_over
   global checker
   x = player.xcor()
   y = player.ycor()
   if game_over == 0:
    if x > 200 or x < -200 or y > 200 or y < -200:
     game_over = 1
    else:
     player.forward(speed)
     if player.distance(circle) < 25:
      turtle.clear()
      score = score+1
      turtle.write("Score: " + str(score), font=("Arial", 16, "bold"))
      circle_function()
      speed = speed+0.05
   else:
     if checker == 0:
      circle.clear()
      turtle.clear()
      turtle.hideturtle()
      circle.hideturtle()
      player.hideturtle()
      screen.bgcolor("red")
      turtle.write("you lose your score was "+str(score), font=("Arial",16,"bold"))
      checker = checker + 1

   screen.ontimer(move,10)


  def right():
   player.right(15)
 
  def left():
   player.left(15)
 
  screen.listen()
  screen.onkey(right, "right")
  screen.onkey(left, "left" )
  screen.onkey(right, "d" )
  screen.onkey(left, "a" )

  move()
