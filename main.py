import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create the turtle
player = Player()

# Create the cars
car_manager = CarManager()

# Create the scoreboard
scoreboard = Scoreboard()

# Move the turtle using keyboard
screen.listen()
screen.onkey(fun=player.go_up, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect when the turtle player collides with a car and stop the game if this happens.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect when the turtle player has reached the top edge of the screen
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up() # This speeds up the cars
        scoreboard.increase_level()
        scoreboard.update_scoreboard()

screen.exitonclick()
