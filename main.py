import pygame
from ball import ball
import math
from random import randint

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

        self.ball = ball([randint(5, self.ScreeWidth - 5),randint(5, self.ScreeHeight - 5)], self.screen)
        self.posOnClick = 0
        self.posOnRelease = 0
        self.MousePress = False
        self.powerBarUp = True
        self.timeWhilePress = 0
        self.powerBarColor = (0,0,0)
        #
        self.Texture = pygame.font.SysFont('Arial', 30)

    def OnLeave(self, event):
        if event.type == pygame.QUIT:
            self.running = False
    
    def powerBarColision(self):
        pass

    def OnMouseClick(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.posOnClick = pygame.mouse.get_pos()
            self.MousePress = True

    def OnMouseRelease(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.posOnRelease = pygame.mouse.get_pos()
            self.MousePress = False
            self.ball.addVector(self.setVelocity(self.posOnRelease, [self.ball.x, self.ball.y]), self.setDirection(self.posOnRelease, [self.ball.x, self.ball.y]))
            self.timeWhilePress = 0

    def shootPower(self):
        if self.timeWhilePress / 60 >= 5:
            return 2
        else: return self.timeWhilePress/60/5+1

    def setVelocity(self, pos1, pos2):
        return [math.sqrt(abs(pos1[0] - pos2[0])) * self.shootPower(), math.sqrt(abs(pos1[1] - pos2[1])) * self.shootPower()]

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
            Vector = self.setVelocity(pygame.mouse.get_pos(), [self.ball.x, self.ball.y])

            pygame.draw.line(self.screen, (0,200,200), (self.ball.x, self.ball.y), (linePosX, linePosY), 2)
            pygame.draw.line(self.screen, (0,255,255), (self.ball.x, self.ball.y), (linePosX, linePosY), 2)

    def event(self):
        for event in pygame.event.get():
            self.OnLeave(event)
            self.OnMouseClick(event)
            self.OnMouseRelease(event)

        self.keys = pygame.key.get_pressed()
        self.powerStatus()

    def powerStatus(self):
        if self.MousePress: 
            if self.shootPower() == 2:
                self.powerBarUp = False
            if self.timeWhilePress == 0:
                self.powerBarUp = True
            if self.powerBarUp: self.timeWhilePress += 5
            else: self.timeWhilePress -= 5

    def displayText(self):
        pass
        # Price = self.Texture.render(f'time: {self.timeWhilePress/ 60} / {self.timeWhilePress} \ : / {self.shootPower()}', True, (0, 0, 0))
        # screen.blit(Price, (10, 10))
    
    def displayPowerBar(self):
        if self.MousePress:
            if self.shootPower()-1 < 0.2: self.powerBarColor = (255, 0, 0)
            elif self.shootPower()-1 < 0.4: self.powerBarColor = (255, 215, 0)
            elif self.shootPower()-1 < 0.6: self.powerBarColor = (255, 255, 0)
            elif self.shootPower()-1 < 0.8: self.powerBarColor = (215, 255, 0)
            else: self.powerBarColor = (0, 255, 0)
            font = pygame.draw.rect(self.screen, (0,0,0), ((pygame.mouse.get_pos()[0] + 10 , pygame.mouse.get_pos()[1] - 40), (30,60)), 0, 7)
            power = pygame.draw.rect(self.screen, self.powerBarColor, ((pygame.mouse.get_pos()[0] + 15 , pygame.mouse.get_pos()[1]+ 15), (20,50*((self.shootPower()-1)*-1))), 0, 7)
            
    def update(self):
        self.drawLine()
        self.displayPowerBar()
        self.ball.move()
        self.ball.reduceVector(0.1)
        self.ball.draw()

    def DisplayScreen(self):
        self.screen.fill((255, 255, 255))

    def display(self):
        self.DisplayScreen()
        self.displayText()
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