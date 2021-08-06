import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=400)
screen.bgcolor("white")
screen.tracer(0)
score = Scoreboard()

player = Player((0, -180))
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # Detect a successful crossing
    if player.is_at_finish():
        player.go_to_start()
        car_manager.level_up()
        score.increase_level()

screen.exitonclick()
