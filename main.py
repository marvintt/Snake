from turtle import Screen
from snake import Snake
import time

# Crear el escenario
screen = Screen()  # Instanciar objeto
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Proyecto Juego Snake")

screen.tracer(0)

# Instanciar objeto serpiente
snake = Snake()

game_is_on = True

while game_is_on:
    screen.update()    
    time.sleep(0.1)
    snake.move_snake()
    
#Final
screen.exitonclick()