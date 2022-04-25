import pygame
from ball import ball
from powerBar import powerBar
from directionArrow import directionArrow
from mathFunction import mathFunction
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
        self.directionArrow = directionArrow(self.screen)
        self.powerBar = powerBar(self.screen)
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
            if pygame.mouse.get_pressed() == (0,0,0):
                self.posOnRelease = pygame.mouse.get_pos()
                self.MousePress = False
                self.ball.addVector(mathFunction.setVelocity(self.posOnRelease, [self.ball.x, self.ball.y], self.powerBar.shootPower()), mathFunction.setDirection(self.posOnRelease, [self.ball.x, self.ball.y]))

    def event(self):
        for event in pygame.event.get():
            self.OnLeave(event)
            self.OnMouseClick(event)
            self.OnMouseRelease(event)

        self.keys = pygame.key.get_pressed()

    def displayText(self):
        pass
        # Price = self.Texture.render(f'time: {self.timeWhilePress/ 60} / {self.timeWhilePress} \ : / {self.shootPower()}', True, (0, 0, 0))
        # screen.blit(Price, (10, 10))

    def arrowDirectionUpdate(self):
        self.directionArrow.update()
        self.directionArrow.draw(self.ball.pos)

    def ballUpdate(self):
        self.ball.update()
        self.ball.drawLine()
        self.ball.move()
        self.ball.reduceVector(0.1)
        self.ball.draw()

    def powerBarUpdate(self):
        self.powerBar.draw()
        self.powerBar.update()

    def update(self):
        self.powerBarUpdate()
        self.arrowDirectionUpdate()
        self.ballUpdate()

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