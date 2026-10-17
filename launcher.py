import random
targets = []
class Target:
    def __init__(self):
        self.x = random.randint(50, WIDTH-50)
        self.y = random.randint(50, HEIGHT-150)
    def draw(self):
            screen.draw.filled_circle((self.x, self.y),20, "red")
     
     
def add_Target():
 targets.append(Target())

        

