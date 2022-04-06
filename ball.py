import pygame

class ball:
    def __init__(self, pos, screen):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.Vector = [0,0]
        self.screen = screen
        self.direction = [1,1]
        self.VectorLimit = [100,100]
        # ball
        self.ball = pygame.draw.circle(self.screen, (255,0,0),(self.x, self.y), 5)
        

    def draw(self):
        self.ball = pygame.draw.circle(self.screen, (255,0,0),(self.x, self.y), 5)
        
    def move(self):
        self.x += self.Vector[0]
        self.y += self.Vector[1]
        self.collision()

    def reduceVector(self, reduceSpeed):
        if reduceSpeed < 0.1: print(f"Error reduceSpeed too slow {reduceSpeed}")


        if self.Vector[0] < 0:
            self.Vector[0] += reduceSpeed
        elif self.Vector[0] > 0:
            self.Vector[0] -= reduceSpeed
        
        self.Vector[0] = int(self.Vector[0] * 10) / 10

        if self.Vector[1] < 0:
            self.Vector[1] += reduceSpeed
        elif self.Vector[1] > 0:
            self.Vector[1] -= reduceSpeed

        self.Vector[1] = int(self.Vector[1] * 10) / 10

    def collision(self):
        if self.y >= self.screen.get_height() or self.y <= 0:
            self.Vector[1] *= -1
            self.direction[1] *= -1
            self.y += self.Vector[1]

        if self.x >= self.screen.get_width() or self.x <= 0:
            self.Vector[0] *= -1
            self.direction[0] *= -1
            self.x += self.Vector[0]
    
    def setVector(self, Vector, direction):
        self.Vector[0] = Vector[0] * direction[0]*-1
        self.Vector[1] = Vector[1] * direction[1]*-1
        self.SpeedLimit()

    def addVector(self, Vector, direction):
        self.Vector[0] += Vector[0] * direction[0]*-1
        self.Vector[1] += Vector[1] * direction[1]*-1
        self.SpeedLimit()

    def SpeedLimit(self):
        if self.Vector[0] > self.VectorLimit[0]: self.Vector[0] = self.VectorLimit[0] - 1
        elif self.Vector[0] < self.VectorLimit[0]*-1:  self.Vector[0] = self.VectorLimit[0]*-1 + 1

        if self.Vector[1] > self.VectorLimit[1]: self.Vector[1] = self.VectorLimit[1] - 1
        elif self.Vector[1] < self.VectorLimit[1]*-1:  self.Vector[1] = self.VectorLimit[1]*-1 + 1