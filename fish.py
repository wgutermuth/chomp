import pygame

class Fish(pygame.sprite.Sprite):
    def __int__(self,x=200,y=200):
        self.image = pygame.image.load("assets/images/fish.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.x = x
        self.y = y

        print("I am a brand new fish :D")
        pass
    def draw(self,screen):
        screen.blit(self.image, (self.x, self.y))
    def move_left(self):
        # Swim left.
        self.x -= 10
    def move_right(self):
        # Swim right.
        self.x += 10
    def move_up(self):
        # Swim up.
        self.y -= 10
    def move_down(self):
        # Move down.
        self.y += 10