#snake game tutorial from TokyoEdtech
import turtle
import time
import random

delay = 0.1

#score
score = 0
highscore = 0

# screen
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=1250, height=700)
window.tracer(0) 

# snake head
snakeHead = turtle.Turtle()
snakeHead.speed(0)
snakeHead.shape("square")
snakeHead.color("green")
snakeHead.penup()
snakeHead.goto(0,0)
snakeHead.direction = "stop"

# food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0    High Score: 0"
, align="center", font=("Courier", 24, "normal"))


# func
def goUp():
    if snakeHead.direction != "down":
        snakeHead.direction = "up"
def goDown():
    if snakeHead.direction != "up":
        snakeHead.direction = "down"
def goLeft():
    if snakeHead.direction != "right":
        snakeHead.direction = "left"
def goRight():
    if snakeHead.direction != "left":
        snakeHead.direction = "right"

def move():
    if snakeHead.direction == "up":
        y = snakeHead.ycor()
        snakeHead.sety(y+20)

    if snakeHead.direction == "down":
        y = snakeHead.ycor()
        snakeHead.sety(y-20)

    if snakeHead.direction == "left":
        x = snakeHead.xcor()
        snakeHead.setx(x-20)

    if snakeHead.direction == "right":
        x = snakeHead.xcor()
        snakeHead.setx(x+20)

# kybd
window.listen()
window.onkeypress(goUp, "Up")
window.onkeypress(goDown, "Down")
window.onkeypress(goLeft, "Left")
window.onkeypress(goRight, "Right")

# main game loop
while True:
        window.update()

        # collision w border
        if snakeHead.xcor()>600 or snakeHead.xcor()<-600 or snakeHead.ycor()>325 or snakeHead.ycor()<-325:
            time.sleep(1)
            snakeHead.goto(0, 0)
            snakeHead.direction = "stop"

            # hide seg
            for segment in segments:
                segment.goto(1000, 1000)

            # clear seg list
            segments.clear()

            # reset score
            score = 0;
            pen.clear()
            pen.write("Score: {}    High Score: {}".format(score, highscore)
            , align="center", font=("Courier", 24, "normal"))

        # collision of head and food
        if snakeHead.distance(food) < 20:
            x = random.randint(-600, 600)
            y = random.randint(-325, 325)
            food.goto(x, y)

            # add segment
            newSeg = turtle.Turtle()
            newSeg.speed(0)
            newSeg.shape("square")
            newSeg.color("grey")
            newSeg.penup()
            segments.append(newSeg)

            # shorten delay
            delay -= .001

            # increase score
            score += 10
            if score > highscore:
                highscore = score
            
            pen.clear()
            pen.write("Score: {}    High Score: {}".format(score, highscore)
            , align="center", font=("Courier", 24, "normal"))

        # move end seg 1st in reverse
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)

        # move seg 0 to head
        if len(segments) > 0:
            x = snakeHead.xcor()
            y = snakeHead.ycor()
            segments[0].goto(x, y)

        move()

        # check for body collision
        for segment in segments:
            if segment.distance(snakeHead) < 20:
                time.sleep(1)
                snakeHead.goto(0, 0)
                snakeHead.direction = "stop"

                # hide seg
                for segment in segments:
                    segment.goto(1000, 1000)

                # clear seg list
                segments.clear()

                # reset score
                score = 0
                pen.clear()
                pen.write("Score: {}    High Score: {}".format(score, highscore)
                , align="center", font=("Courier", 24, "normal"))

        time.sleep(delay)

window.mainloop()
