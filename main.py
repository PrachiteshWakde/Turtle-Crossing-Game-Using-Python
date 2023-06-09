import time
import car_manager
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

peaky = Player()
cars = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    screen.onkey(peaky.up,'Up')
    time.sleep(0.1)
    cars.create_car()
    cars.move_cars()
    screen.update()
    if peaky.is_at_finish():
        peaky.start()
        cars.speed_up()
        score.level_up()
    for car in cars.all_cars:
        if car.distance(peaky) < 20:
            game_is_on = False
            score.over()
screen.exitonclick()
