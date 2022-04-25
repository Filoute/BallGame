import pygame
from mathFunction import mathFunction

class directionArrow:
    def __init__(self, screen):
        self.screen = screen
        # powerBar
        self.timeWhilePress = 0
        self.MousePress = False

        self.arrowLine = None
        self.arrowHead = None

    def update(self):

        if not self.MousePress: self.timeWhilePress = 0

        for i in range(0, 3):
            if pygame.mouse.get_pressed()[i]:
                self.MousePress = True
                break
            else:
                self.MousePress = False

    def draw(self, ball):
        if self.MousePress:
            sm = mathFunction.setVelocity(pygame.mouse.get_pos(), [ball[0], ball[1]])
            direction = mathFunction.setDirection(pygame.mouse.get_pos(), [ball[0], ball[1]])
            self.arrowHead = self.limitofArrow(sm[0] *-2)* direction[0] + ball[0] , self.limitofArrow(sm[1] *-2)* direction[1] + ball[1]

            self.arrowLine = pygame.draw.line(self.screen, (255,155,0), (self.arrowHead), (ball), 3)
            self.makeHead(ball)

    def makeHead(self,ball):

        pygame.draw.polygon(self.screen, (0,200,0), ((ball[0]*0.95, ball[1]*0.95), (ball[0]*1.05, ball[1]*1.05), (self.arrowHead[0]*1, self.arrowHead[1]*1)), 3)

    def limitofArrow(self, arrowCoordinate):
        if arrowCoordinate > 25:
            return 25
        elif arrowCoordinate < -25:
            return -25
        else: return arrowCoordinate
        
    def collision(self):
        pass
