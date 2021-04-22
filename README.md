# day23-turtle-crossing-start
## Turtle crossing game

1. Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north.
```
# In main.py
screen.listen()
screen.onkey(fun=player.go_up, key='Up')

# In player.py
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(TURTLE_HEAD_DIRECTION)
        self.penup()
        self.go_to_start()

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
```
2. Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. No cars should be generated in the top and bottom 50px of the screen
```
class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            random_position = (300, random_y)
            new_car.goto(random_position)
            self.all_cars.append(new_car)
```
3. Detect when the turtle player collides with a car and stop the game if this happens.
```
for car in car_manager.all_cars:
    if car.distance(player) < 20:
        scoreboard.game_over()
        game_is_on = False
```
4. Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). When this happens, return the turtle to the starting position and increase the speed of the cars.
```
# In main.py
if player.is_at_finish_line():
    player.go_to_start()
    car_manager.level_up() # This speeds up the cars
    scoreboard.increase_level()
    scoreboard.update_scoreboard()

# In car_manager.py
def move_cars(self):
    for car in self.all_cars:
        car.backward(self.car_speed)

def level_up(self):
    self.car_speed += MOVE_INCREMENT
```
5. Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre.
```
from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        # self.color("black")
        self.goto(-260, 260)
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"LEVEL: {self.level}", move=False, font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(-0, 0)
        self.write(f"GAME OVER", move=False, align="center", font=FONT)
```

## Lessons
1. Reading code is harder than writing one
2. It's about thinking, not writing the code
3. Slow down. Come back at it next day if you want--no need to show off
