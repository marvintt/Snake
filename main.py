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

#Movimientos serpiente
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.down,"Down")

game_is_on = True

while game_is_on:
    screen.update()    
    time.sleep(0.1)
    snake.move_snake()
    
#Final
screen.exitonclick()
