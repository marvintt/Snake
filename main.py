from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

# Crear el escenario
screen = Screen()  # Instanciar objeto
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Proyecto Juego Snake")

screen.tracer(0)

# Instanciar objeto serpiente
snake = Snake()

# Instanciar objeto comida
food = Food()

# Instanciar objeto scoreboard
scoreboard = Scoreboard()


# Movimientos serpiente
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Detectar colision con comida
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detectar colision con pared
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False
        scoreboard.game_over()
    
    # Detectar colision con cola
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# Final
screen.exitonclick()
