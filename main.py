from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import MessageHandler

turtle = Turtle()
screen = Screen()
message_handler = MessageHandler()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)

game_is_on = False  # Initialize game state

# paddal and ball creation (-20)
paddle = Paddle((0, -250))
ball = Ball((0, -230))

all_brick = []


def start_game():
    global game_is_on
    message_handler.show_message("Press Space \r to Start Game", 30)
    game_is_on = False


def create_brick():
    for i in range(-360, 370, 48):
        for j in range(0, 280, 24):
            all_brick.append(Brick((i, j)))


def game_control():
    global game_is_on
    message_handler.clear_message()
    while game_is_on:
        screen.update()
        ball.move()
        win_game()
        # brick bounce and destroy
        for brick in all_brick:
            if ball.distance(brick) < 27:
                all_brick.remove(brick)
                brick.hideturtle()
                brick.clear()
                ball.bounce_y()

        if ball.distance(paddle) < 60 and ball.ycor() < -230:
            ball.bounce_y()
        if ball.xcor() < -390 or ball.xcor() > 390:
            ball.bounce_x()
        if ball.ycor() < -250:
            game_over()
        if ball.ycor() > 290:
            ball.bounce_y()


def win_game():
    if len(all_brick) == 0:
        game_over()
        message_handler.clear()
        message_handler.show_message("You win\r Press space to replay ", 30)


def game_over():
    global game_is_on
    game_is_on = False
    [brick.hideturtle() for brick in all_brick]
    all_brick.clear()
    message_handler.clear()
    message_handler.show_message("Game over\r Press space to replay ", 30)
    screen.update()


def reset_game():
    global game_is_on
    message_handler.clear()

    for brick in all_brick:
        brick.clear()
        brick.hideturtle()

    all_brick.clear()
    create_brick()
    ball.reset_position()
    game_is_on = True  # Reset the game state
    game_control()  # Start the game loop


create_brick()

screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")
screen.onkey(reset_game, "space")

screen.listen()
start_game()  # Display the start message initially

screen.exitonclick()
