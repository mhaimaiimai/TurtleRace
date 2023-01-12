from turtle import Turtle, Screen
import random

screen_width = 500
screen_height = 400
start_turtle_position_x = -230
start_turtle_position_y = -80

def make_turtle_ready(turtle, color, position_y):
    global start_turtle_position_x
    #set color
    turtle.color(color)
    #set position
    turtle.penup()
    turtle.setposition(x=start_turtle_position_x, y=position_y)
    position_y += 30
    return position_y

def turtle_walk(turtle):
    turtle.forward(random.randint(0,10))

def main():
    screen = Screen()
    screen.setup(width=screen_width, height=screen_height)
    guess_winner = screen.textinput(title="Make your bet", 
                                    prompt="Which turtle will win the race? Enter a color: ").lower()
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]   
    
    if guess_winner in colors:
        all_turtles = []
        current_position_y = start_turtle_position_y
        for n_turtle in range (6):
            turtle = Turtle(shape="turtle")
            current_position_y = make_turtle_ready(turtle, colors[n_turtle], current_position_y)  
            all_turtles.append(turtle)

        is_race_on = True
        while(is_race_on):
            for turtle in all_turtles:
                turtle_walk(turtle)
                if turtle.position()[0]>=(screen_width/2):
                    if turtle.pencolor() == guess_winner:
                        result = "You win the bet!"
                    else:
                        result = "You lose the bet!"
                    screen.textinput(title="result", 
                                    prompt=f"{result} Press enter to exit")
                    is_race_on = False
                    break
    screen.bye()

main()