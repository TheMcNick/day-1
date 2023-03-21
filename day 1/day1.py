from turtle import *

#i want to paint a house

#step 1: draw a square
shape("triangle")
speed(20)
width(5)
color("yellow")
begin_fill
forward (200)
left(90)

forward (200)
left(90)

forward (200)
left(90)

forward (200)
left(90)
end_fill()
#this is end of the square

#step 2 : draw a door

forward(70)
color("brown")
begin_fill
left(90)
forward(120) #height of the door
right(90)
forward(60)
right (120)
forward(120)
end_fill

#step 3 : draw a roof

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right (150)
forward(200)
left(120)
forward(200)
end_fill()

# step 4 : draw window #1
penup()
goto(50, 100)
pendown()

color("blue")
right (50)
forward(50)
left(50)
forward(50)
left(50)

#step 5 : draw window #2

penup()
goto(150, 100)
pendown()

color("blue")
forward (50)
left(50)

forward (50)
left(50)

forward (50)
left(50)

forward (200)
left(50)
end_fill()

exitonclick