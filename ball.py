import pygame

class ball:
    def __init__(self, pos, screen):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.Vector = [0,0]
        self.screen = screen
        

    def draw(self):
        pygame.draw.circle(self.screen, (255,0,0),(self.x, self.y), 5)

    def move(self):
        self.x += self.Vector[0]
        self.y += self.Vector[1]
        self.collision()

    def reduceVector(self, reduceSpeed):
        if self.Vector[0] < 0:
            self.Vector[0] += reduceSpeed
        elif self.Vector[0] > 0:
            self.Vector[0] -= reduceSpeed

        if self.Vector[1] < 0:
            self.Vector[1] += reduceSpeed
        elif self.Vector[1] > 0:
            self.Vector[1] -= reduceSpeed

    def collision(self):
        if (self.y == self.screen.get_height() or self.y == 0):
            self.Vector[1] *= -1
        
        if (self.x == self.screen.get_width() or self.x == 0):
            self.Vector[0] *= -1
    
    def setVector(self, Vector):
        self.Vector = Vector

    def addVector(self, Vector):
        print("UwU")
        self.Vector[0] += Vector[0]
        self.Vector[1] += Vector[1]