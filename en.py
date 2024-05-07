from turtle import *
import turtle

screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)

speed(10)
color('cyan')
bgcolor('black')
b=200
while b>0:
    left(b)
    forward(b * 3)
    b= b - 1
