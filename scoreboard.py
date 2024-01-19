from turtle import Screen, Turtle

class MessageHandler(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

    def show_message(self, message, font_size):
        self.hideturtle()
        self.goto(0, 0)
        self.write(message, align="center", font=("Verdana", font_size, "normal"))

    def clear_message(self):
        self.hideturtle()
