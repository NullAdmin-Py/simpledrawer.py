import turtle
import keyboard
import time

turtle.Turtle()
turtle.shape('arrow')
turtle.left(90)
bg = turtle.Screen()
pen = True
i = True
color = 'black'
while i:
	turtle.pendown()
	if keyboard.is_pressed('w'):
		turtle.forward(1)
	elif keyboard.is_pressed('a'):
		turtle.left(45)
	elif keyboard.is_pressed('d'):
		turtle.right(45)
	elif keyboard.is_pressed('s'):
		turtle.backward(1)
	elif keyboard.is_pressed('shift'):
		i = False

	else:
		pass
exit()