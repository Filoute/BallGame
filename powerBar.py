import pygame

class powerBar:
    def __init__(self, screen):
        self.screen = screen
        self.direction = [1,1]
        # powerBar
        self.powerBarColor = (0,0,0)
        self.timeWhilePress = 0
        self.MousePress = False
        self.powerBarUp = False

        self.fontDisplay = pygame.draw.rect(self.screen, (0,0,0), (0,0,0,0))
        self.powerDispaly = pygame.draw.rect(self.screen, (0,0,0), (0,0,0,0))

    def update(self):
        self.powerStatus()

        if not self.MousePress: self.timeWhilePress = 0

        for i in range(0, 3):
            if pygame.mouse.get_pressed()[i]:
                self.MousePress = True
                break
            else:
                self.MousePress = False

    def draw(self):
        if self.MousePress:
            if self.shootPower()-1 < 0.2: self.powerBarColor = (255, 0, 0)
            elif self.shootPower()-1 < 0.4: self.powerBarColor = (255, 215, 0)
            elif self.shootPower()-1 < 0.6: self.powerBarColor = (255, 255, 0)
            elif self.shootPower()-1 < 0.8: self.powerBarColor = (215, 255, 0)
            else: self.powerBarColor = (0, 255, 0)
            self.fontDisplay = pygame.draw.rect(self.screen, (0,0,0), ((pygame.mouse.get_pos()[0] + 10 , pygame.mouse.get_pos()[1] - 40), (30,60)), 0, 7)
            self.powerDispaly = pygame.draw.rect(self.screen, self.powerBarColor, ((pygame.mouse.get_pos()[0] + 15 , pygame.mouse.get_pos()[1]+ 15), (20,50*((self.shootPower()-1)*-1))), 0, 7)

    def powerStatus(self):
        if self.MousePress: 
            if self.shootPower() == 2:
                self.powerBarUp = False
            if self.timeWhilePress <= 0:
                self.powerBarUp = True

            if self.powerBarUp: self.timeWhilePress += self.shootPower()**3.5
            else: self.timeWhilePress -= self.shootPower()**3.5

    def shootPower(self):
        if self.timeWhilePress / 60 >= 5:
            return 2
        else: return self.timeWhilePress/60/5+1