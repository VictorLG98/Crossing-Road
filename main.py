import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Crossing Road")

player = Player()
car = CarManager()
scoreboard = Scoreboard()


def move_up():
    player.move_up()


screen.listen()
screen.onkey(move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move_cars()

    # Detect collisions with cars
    for c in car.all_cars:
        if c.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()


screen.mainloop()
