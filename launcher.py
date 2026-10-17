import pgzrun

HEIGHT = 600
WIDTH = 800
circlerad = 20
objs = []

class bullett:
    def __init__(self,bulletposx,bullettposy):
        self.bulletposx = bulletposx
        self.bulletposy = bullettposy
        self.velocity = 2

    def update(self):
        self.bulletposx = self.bulletposx + self.velocity
        if self.bulletposx > WIDTH + circlerad:
            objs.remove(self)

    def draw(self):
        screen.draw.filled_circle((self.bulletposx,self.bulletposy),circlerad,(255,255,255))

def on_mouse_down(pos):
    bulletposx = pos[0]
    bulletposy = pos[1]
    objs.append(bullett(bulletposx,bulletposy))

def draw():
    screen.clear()
    if len(objs) > 1:
        try:
            for x in range(len(objs)):
                objs[x].draw()
        except:
            pass

def update():
    if len(objs) > 1:
        try:
            for x in range(len(objs)):
                objs[x].update()
        except:
            pass
    draw()

pgzrun.go()