import pygame
from ball import ball
import math

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.ScreeWidth = screen.get_width()
        self.ScreeHeight = screen.get_height()
        #
        self.running = True
        self.clock = pygame.time.Clock()
        self.tick = 0
        #

        self.keys = None
        # 

        self.ball = ball([100,100], self.screen)
        self.posOnClick = 0
        self.posOnRelease = 0
        self.MousePress = False
        #

    def OnLeave(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def OnMouseClick(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.posOnClick = pygame.mouse.get_pos()
            self.MousePress = True

    def OnMouseRelease(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.posOnRelease = pygame.mouse.get_pos()
            self.MousePress = False
            self.ball.addVector(self.setVelocity(self.posOnRelease, [self.ball.x, self.ball.y]), self.setDirection(self.posOnRelease, [self.ball.x, self.ball.y]))
            

    def setVelocity(self, pos1, pos2):
        return [math.sqrt(abs(pos1[0] - pos2[0])), math.sqrt(abs(pos1[1] - pos2[1]))]

    def setDirection(self, pos1, pos2):
        direction = [0,0]
        if (pos1[0] - pos2[0]) > 0: direction[0] = 1
        else: direction[0] = -1
        if (pos1[1] - pos2[1]) > 0: direction[1] = 1
        else: direction[1] = -1
        return direction
    
    def getDistance(self, pos1, pos2):
        return math.sqrt(math.pow(abs(pos1[0] - pos2[0]), 2) + math.pow(abs(pos1[1] - pos2[1]), 2))

    def drawLine(self):
        if self.MousePress:
            direction = self.setDirection(pygame.mouse.get_pos(), self.posOnClick)
            linePosX = self.ball.x + (pygame.mouse.get_pos()[0] - self.ball.x)
            linePosY = self.ball.y + (pygame.mouse.get_pos()[1] - self.ball.y)

            pygame.draw.line(self.screen, (0,200,200), (self.ball.x, self.ball.y), (linePosX, linePosY), 2)
            pygame.draw.line(self.screen, (0,255,255), (self.ball.x, self.ball.y), (linePosX*-1, linePosY*-1), 2)

    def event(self):
        for event in pygame.event.get():
            self.OnLeave(event)

            self.OnMouseClick(event)
            self.OnMouseRelease(event)

        self.keys = pygame.key.get_pressed()

    def update(self):
        self.drawLine()
        self.ball.move()
        self.ball.reduceVector(0.1)
        self.ball.draw()

    def DisplayScreen(self):
        self.screen.fill((255, 255, 255))

    def display(self):
        self.DisplayScreen()
        self.update()
        pygame.display.flip()

    def run(self):
        while self.running:
            self.display()
            self.event()
            self.clock.tick(60)
            if self.tick == 60:
                self.tick = 0
            else:
                self.tick += 1


pygame.init()
screen = pygame.display.set_mode((700, 500))
game = Game(screen)
game.run()

pygame.quit()