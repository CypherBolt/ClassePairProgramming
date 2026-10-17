import pgzrun

mouseX = 0
mouseY = 0
bulletX = mouseX
bulletY = mouseY
firing = False
yVel = 5
WIDTH = 1000
HEIGHT = 800

 
def draw():
    screen.clear()
    screen.draw.filled_circle((bulletX,bulletY),10,"white")
    screen.draw.filled_circle((mouseX,mouseY),20,"green")
  

def update():
    global bulletX, bulletY, firing, yVel
    if firing == False:
        bulletX = mouseX + 10
        bulletY = mouseY - 10
    else:
        bulletX += 10
        bulletY -= yVel
        yVel -= .2
        
    if bulletX >= 1020 or bulletY >= 820:
        firing = False
        bulletX = mouseX + 10
        bulletY = mouseY - 10
        yVel = 5

def on_mouse_down(button):
    global firing
    if button == mouse.LEFT:
        if firing == False:
            firing = True

def on_mouse_move(pos):
  global mouseX, mouseY
  mouseX, mouseY = pos
  
pgzrun.go()