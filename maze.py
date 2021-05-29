from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,image_player,x_player, y_player,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(image_player),(65,65))
        self.speed = player_speed
        self.rect  = self.image.get_rect()
        self.rect.x= x_player 
        self.rect.y= y_player

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))



class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += self.speed

class Enemy(GameSprite):
    direction = "left"
    def update(self):
       
        if self.rect.x < 470:
            self.direction = "right"
        elif self.rect.x > 650:
            self.direction = "left"
        
        if self.direction == "left":
            self.rect.x -= self.speed
        else: 
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self,colour1,colour2,colour3,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.colour1= colour1
        self.colour2= colour2
        self.colour3= colour3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((colour1,colour2,colour3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
            
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze Game")

background = transform.scale(image.load("background.jpg"), (700,500))

player = Player("hero.png", 40, 420, 2 )
enemy  = Enemy("cyborg.png", 585, 250, 1)
finish = GameSprite("treasure.png", 610, 400, 0 )

Wall1 = Wall(0, 179, 0, 120, 10 , 10 , 400)
Wall2 = Wall(0, 179, 0, 320, 450, 140, 10)
Wall3 = Wall(0, 179, 0, 1  , 400, 130, 10)
Wall4 = Wall(0, 179, 0, 450, 10 , 500, 10)
Wall5 = Wall(0, 179, 0, 240, 120, 250, 10)
Wall6 = Wall(0, 179, 0, 240, 250, 250, 10)
Wall7 = Wall(0, 179, 0, 400, 360, 10 , 100)

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

money = mixer.Sound ("money.ogg")
kick = mixer.Sound ("kick.ogg")

clock = time.Clock()
FPS = 55
clock.tick(FPS)

font.init()
font = font.SysFont("Arial" , 70)

win = font.render("YOU WIN!", True, (204, 163, 0))
lose = font.render("YOU LOSE!", True, (179, 0, 0))

game = True
finished = False

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finished != True:
        window.blit(background, (0,0))

        player.update()
        enemy.update()
        
        player.reset()
        enemy.reset()
        finish.reset()
        
        Wall1.draw_wall()
        Wall2.draw_wall()
        Wall3.draw_wall()
        Wall4.draw_wall()
        Wall5.draw_wall()
        Wall6.draw_wall()
        Wall7.draw_wall()

        if sprite.collide_rect(player,enemy) or sprite.collide_rect(player, Wall1) or sprite.collide_rect(player, Wall2) or sprite.collide_rect(player, Wall3) or sprite.collide_rect(player, Wall4) or sprite.collide_rect(player, Wall5) or sprite.collide_rect(player, Wall6) or sprite.collide_rect(player, Wall7):
            window.blit(lose, (200,200))
            finished = True
            kick.play()

        if sprite.collide_rect(player, finish):
            window.blit(win, (200,200))
            finished = True
            money.play()

    display.update()