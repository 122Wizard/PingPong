from pygame import *

img_back = "background.jpg"

win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption("Ping_Pong")
background = transform.scale(image.load(img_back), (win_width, win_height))


class GameSprite(sprite.Sprite):
    #constructer
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # call constructor of Sprite:
        sprite.Sprite.__init__(self)

        #evry sprites should has his property
        if not player_image is None:
            self.image = transform.scale(image.load(player_image), (size_x, size_y))
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y

        self.speed = 0 if player_speed is None else player_speed

    # method to draw
    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    # method to drive
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 85:
            self.rect.x += self.speed