from pygame import *
class GameSprite(sprite.Sprite):
#class constructor
  def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
      #call for the class (Sprite) constructor:
      sprite.Sprite.__init__(self)
      #every sprite must store the image property
      self.image = transform.scale(image.load(player_image), (size_x, size_y))
      self.speed = player_speed
      #every sprite must have the rect property that represents the rectangle it is fitted in
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
#method drawing the character on the window
  def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))
#main player class
class Player(GameSprite):
  #method to control the sprite with arrow keys
    def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
    def update_r(self):
           keys = key.get_pressed()
           if keys[K_UP] and self.rect.y > 5:
               self.rect.y -= self.speed
           if keys[K_DOWN] and self.rect.y < win_height - 80:
               self.rect.y += self.speed


background_color = (88, 169, 225)
win_width = 600
win_height = 500
window = display.set_mode((win_width,win_height))
window.fill(background_color)
raquette_1 = Player("racket.png", 30, 300, 50, 150, 4)
raquette_2 = Player("racket.png", 510, 300, 50, 150, 4)
ballon = GameSprite("tenis_ball.png", 200, 200, 50, 50, 4)
font.init()
font = font.Font(None, 35)
clock = time.Clock()


gameee = True
finish = False

perte1 = font.render("Player 1 lost", True, (145, 0, 0))
perte2 = font.render("Player 2 lost", True, (145, 0, 0))

speedx = 3
speedy = 3


while gameee:
    for e in event.get():
       if e.type == QUIT:
           gameee = False
    if finish == False:
        window.fill(background_color)
        raquette_1.update_l()
        raquette_2.update_r()
        ballon.rect.x += speedx
        ballon.rect.y += speedy
        if sprite.collide_rect(raquette_1, ballon) or sprite.collide_rect(raquette_2, ballon):
            speedx *= -1
            speedy *= 1
        if ballon.rect.y >= win_height-50 or ballon.rect.y < 0:
            speedy *= -1
        if ballon.rect.x < 0:
            finish = True
            window.blit(perte1, (200,200))
        if ballon.rect.x > win_height:
            finish = True
            window.blit(perte2, (200,200))
        raquette_1.reset()
        raquette_2.reset()
        ballon.reset()
    display.update()
    clock.tick(60)