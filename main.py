import pygame
from ball import ball

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
        # Images

        self.ball = ball([150,100], self.screen)
        #

    def OnLeave(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def OnClick(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            self.ball.addVector([2,2])


    def event(self):
        for event in pygame.event.get():
            self.OnClick(event)
            self.OnLeave(event)

        self.keys = pygame.key.get_pressed()

    def update(self):
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
screen = pygame.display.set_mode((500, 300))
game = Game(screen)
game.run()

pygame.quit()
