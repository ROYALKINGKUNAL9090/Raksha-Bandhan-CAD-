import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("lightyellow")
screen.title("Raksha Bandhan Special")

rakhi = turtle.Turtle()
rakhi.speed(10)

# Draw Rakhi center (Main Circle)
rakhi.penup()
rakhi.goto(0, -50)
rakhi.pendown()
rakhi.color("orange")
rakhi.begin_fill()
rakhi.circle(50)
rakhi.end_fill()

# Draw colorful petals around the Rakhi
colors = ["red", "blue", "green", "purple", "deeppink", "gold"]
rakhi.width(2)
for i in range(12):
    rakhi.color(colors[i % 6])
    rakhi.penup()
    rakhi.goto(0, 0)
    rakhi.setheading(i * 30)
    rakhi.forward(50)
    rakhi.pendown()
    rakhi.begin_fill()
    rakhi.circle(15)
    rakhi.end_fill()

# Draw the Rakhi strings (Dhaga)
rakhi.penup()
rakhi.goto(-150, 0)
rakhi.color("red")
rakhi.width(6)
rakhi.pendown()
rakhi.goto(-50, 0)

rakhi.penup()
rakhi.goto(150, 0)
rakhi.pendown()
rakhi.goto(50, 0)

# Write Greeting Message
rakhi.penup()
rakhi.goto(0, 120)
rakhi.color("darkred")
rakhi.write("Happy Raksha Bandhan!", align="center", font=("Arial", 24, "bold"))

rakhi.hideturtle()
screen.mainloop()
