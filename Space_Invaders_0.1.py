
# Python 3.9.1 on Windows
import turtle
import math

# Set up the screen
main_screen = turtle.Screen()
main_screen.bgcolor("black")
main_screen.title("Space Invaders")
main_screen.tracer(0)

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

# Set the score to 0
score = 0

# Draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
score_string = "Score: {}".format(score)
score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -240)
player.setheading(90)

player_speed = 15

# Choose number of enemies
number_of_enemies = 30
# Create empty list of enemies
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
    # Create the enemy
    enemies.append(turtle.Turtle())

enemy_start_x = -225
enemy_start_y = 250
enemy_number = 0

for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = enemy_start_x + (50 * enemy_number)
    y = enemy_start_y
    enemy.setposition(x, y)
    # Update the enemy number
    enemy_number += 1
    if enemy_number == 10:
        enemy_start_y -= 50
        enemy_number = 0
enemy_speed = 0.2

# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.75, 0.75)
bullet.hideturtle()

bullet_speed = 2

# Define bullet state
# Ready -  ready to fire
# Fire - bullet is firing
bullet_state = "ready"


# Move player left and right
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    # Declare bullet state as global
    global bullet_state
    if bullet_state == "ready":
        bullet_state = "fire"
        # Move bullet above player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


# Create keyboard bindings
main_screen.listen()
main_screen.onkeypress(move_left, "Left")
main_screen.onkeypress(move_right, "Right")
main_screen.onkeypress(fire_bullet, "space")

# Main game loop
while True:
    main_screen.update()
    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        # Move the enemy back and down
        if enemy.xcor() > 280:
            # Move all the enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemy_speed *= -1

        if enemy.xcor() < -280:
            # Move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            # Change enemy direction
            enemy_speed *= -1

        # Check for a collision between the bullet and the enemy
        if isCollision(bullet, enemy):
            # Reset the bullet
            bullet.hideturtle()
            bullet_state = "ready"
            bullet.setposition(0, -400)
            # Reset the enemy
            enemy.setposition(0, 10000)
            # Update the score
            score += 10
            score_string = "Score: {}".format(score)
            score_pen.clear()
            score_pen.write(score_string, False, align="left", font=("Arial", 14, "normal"))

        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    # Move the bullet
    if bullet_state == "fire":
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

    # Check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bullet_state = "ready"

