import pgzrun
import math

WIDTH = 1000
HEIGHT = 800

playerX = WIDTH // 2
playerY = HEIGHT - 50
bulletX = playerX
bulletY = playerY
firing = False
speed = 12

#where the mouse is pointing right now, separate from playerX and playerY
mouseX = WIDTH // 2
mouseY = 0
bulletVelX = 0
bulletVelY = 0

time_remaining=60

def tick():
    global time_remaining
    time_remaining -= 1
    if time_remaining <= 0:
        clock.unschedule(tick)
        #end game here

clock.schedule_interval(tick, 1.0) #one "tick" happens every sec

#points
score  = 0


def draw():
    screen.clear()
    screen.draw.filled_circle((bulletX,bulletY),10,"white")
    screen.draw.filled_circle((playerX,playerY),20,"green")
    screen.draw.text(f"Score: {score}", (10, 10), color = "white")
    screen.draw.text(f"Time: {time_remaining}", (10, 40), color = "white")


def update():
    global bulletX, bulletY, firing, playerX, playerY, score

    if firing == False:
        bulletX = playerX
        bulletY = playerY
    else:
        bulletX += bulletVelX
        bulletY += bulletVelY

    if bulletX < 0 or bulletX > WIDTH or bulletY < 0 or bulletY > HEIGHT:
        firing = False

    #user controls
    if keyboard.left:
        playerX -= 5
    if keyboard.right:
        playerX += 5
    if keyboard.up:
        playerY -= 5
    if keyboard.down:
        playerY += 5

def on_mouse_move(pos):
    global mouseX, mouseY
    mouseX, mouseY = pos

def on_mouse_down(button):
    global firing, bulletX, bulletY, bulletVelX, bulletVelY
    if button == mouse.LEFT:
        if firing == False:
            firing = True
            bulletX, bulletY = playerX, playerY
            dx = mouseX-playerX
            dy = mouseY-playerY
            distance = math.hypot(dx, dy)  #avoid dividing by zero
            bulletVelX = dx/distance*speed
            bulletVelY = dy/distance*speed


pgzrun.go()