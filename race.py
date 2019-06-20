#!/bin/python3
from turtle import *
from random import randint
penup()
speed(100)
trackLen=10
for step in range(1,trackLen+1):
  if(step==1):
    penup()
  else:
    penup()
  forward(20)
  write(step,align='center')
  
for step in range(int(trackLen/2)):
  pendown()
  right(90)
  forward(200)
  right(90)
  penup()
  forward(20)
  right(90)
  pendown()
  forward(200)
  penup()
  left(90)
  forward(20)
  right(180)
goto(0,0)

r=Turtle()
r.color("red")
r.shape("turtle")
r.speed(1)
r.penup()
r.goto(0,-40)
r.forward(20)

b=Turtle()
b.color("blue")
b.shape("turtle")
b.speed(1)
b.penup()
b.goto(0,-80)
b.forward(20)

g=Turtle()
g.color("green")
g.shape("turtle")
g.speed(1)
g.penup()
g.goto(0,-120)
g.forward(20)

y=Turtle()
y.color("gray")
y.shape("turtle")
y.penup()
y.goto(0,-160)
y.forward(20)
speed(1)
r.pendown()
g.pendown()
b.pendown()
y.pendown()

r.stamp()
g.stamp()
b.stamp()
y.stamp()

rc=0
gc=0
bc=0
yc=0
end=200
wr=1
wg=1
wb=1
wy=1
first="";
for steps in range(100):
  if(rc<=end):
    ri=(randint(0,5))
  else:
    ri=0
    if len(first)==0:
      first="Red"
  if(gc<=end):
    gi=(randint(0,5))
  else:
    gi=0
    if len(first)==0:
      first="Green"
  if(bc<=end):
    bi=(randint(0,5))
  else:
    bi=0
    if len(first)==0:
      first="Blue"
  if(yc<=end):
    yi=(randint(0,5))
  else:
    yi=0
    if len(first)==0:
      first="Gray"
  r.forward(ri)
  g.forward(ri)
  b.forward(ri)
  y.forward(ri)
  rc+=ri;
  gc+=gi;
  bc+=bi;
  yc+=yi;
print("FIRST is :: ",first)
