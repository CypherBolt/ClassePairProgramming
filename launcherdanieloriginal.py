import pgzrun
HEIGHT = 600
WIDTH = 800
cy = 550
cx = -70
r = 50
d1 = 1
d2 = 0
speed = 2
speed1 = 2
speed2 = 550
count = 0
shoot = 0
def on_mouse_down(pos):
    global d1, d2,speed, speed1, speed2, cx, cy, shoot
    cx = pos[0]
    cy = pos[1]
    d1 = 1
    speed = 2
    speed1 = 2
    speed2 = 550
    shoot = 1
def draw():
    screen.clear()
    screen.draw.filled_circle((cx, cy), r, "white")
def update():
    global cx,cy,r,d1,d2,speed,speed1,speed2
    if d1 == 0:
        speed2 = speed * speed1
        speed1 = speed1 * 1.1
        cy += speed2
        if cy >= HEIGHT - r:
            d1 = 2
    if d1 == 1:
        speed2 = speed * speed1
        speed1 = speed1 / 1.1
        cy -= speed2
        if speed1 <= 1:
            d1 = 0
    if shoot == 1:
        if cx <= WIDTH + r:
            cx += speed*10
    draw()
pgzrun.go()