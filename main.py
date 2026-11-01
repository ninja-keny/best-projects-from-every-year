import turtle
import time

# setting the varibles
second = 0
on = 1
off = 1

# making the turtle reset
reset = turtle.Turtle()
reset.hideturtle()
reset.speed(1000)
reset.penup()
reset.goto(100,150)
reset.pendown()
reset.color("orange")
reset.hideturtle()

#make this seconds display
seconds = turtle.Turtle()
seconds.hideturtle()
seconds.penup()
seconds.goto(-50,10)
def write_seconds():
 seconds.clear()
 seconds.write("seconds:"+str(second),font=("Arial",20,"bold"))
write_seconds()

# drawing the rectangles for reset
for i in range(2):
  reset.begin_fill()
  reset.forward(100)
  reset.left(90)
  reset.forward(50)
  reset.left(90)
reset.end_fill()
reset.left(90)
reset.forward(25)
reset.right(90)
reset.forward(25)
reset.color("black")
reset.write("reset",font=("Arial",20,"bold"))
screen = turtle.Screen()
screen.bgcolor("blue")

# red_rectangle for the stop button
def red_rectangle():
    turtle.clear()
    turtle.goto(-50,0)
    turtle.color("red")
    turtle.begin_fill()
    for i in range(2):
     turtle.forward(150)
     turtle.right(90)
     turtle.forward(50)
     turtle.right(90)
    turtle.end_fill()
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(45)
    turtle.color("black")
    turtle.write("stop",font=("Arial",20,"bold"))
    turtle.goto(30,-30)
    
#  drawing the backround and rectangle
def green_rectangle():
  turtle.hideturtle()
  turtle.speed(1000)
  turtle.clear()
  turtle.goto(-50,0)
  turtle.color("green")
  turtle.begin_fill()
  for i in range(2):
   turtle.forward(150)
   turtle.right(90)
   turtle.forward(50)
   turtle.right(90)
  turtle.end_fill()
  turtle.right(90)
  turtle.forward(30)
  turtle.left(90)
  turtle.forward(45)
  turtle.color("black")
  turtle.write("start",font=("Arial",20,"bold"))
  turtle.goto(30,-30)
green_rectangle()

# a function for the click
def start(x,y):
 global on
 global off
 global second
 
 if reset.distance(x,y) < 75:
   second = 0
   write_seconds()
   
 if turtle.distance(x,y) < 75:
  if off == 0:
   on = 1
   off = 1
   start = 0
   green_rectangle()
   return
 
  if on == 1:
   on = 1
   red_rectangle()
   off = 0
screen.onscreenclick(start)


def tick():
    global second
    global on
    global off
    if on == 1 and off == 0:
     second += 1
     write_seconds()
    screen.ontimer(tick, 1000)

tick()

screen.mainloop()