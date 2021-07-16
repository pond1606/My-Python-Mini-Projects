"""Shooting Covid game by Phan Huynh Thien Phuc
This game is originally in a Udemy course (An introduction to game development in Python).
I made some changes so now it's a Covid shooting game. You have masks as your HP and you
have to dodge (or shoot) the Covid virus flying everywhere. Pretty cool, right?"""

import pygame, sys, random


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos):
        super().__init__()
        self.uncharged = pygame.image.load(path)
        self.charged = pygame.image.load('spaceship_charged.png')
        self.image = self.uncharged
        self.rect = self.image.get_rect(center=(x_pos, y_pos))
        self.mask_surface = pygame.image.load('mask.png')
        self.health = 5

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        self.screen_constrain()
        self.display_heath()

    def screen_constrain(self):
        if self.rect.right >= 1280:
            self.rect.right = 1280
        if self.rect.left <= 0:
            self.rect.left = 0

    def display_heath(self):
        mask_x_pos = 10
        for mask in range(self.health):
            screen.blit(self.mask_surface, (mask_x_pos, 10))
            mask_x_pos += 40

    def get_damage(self, damage_amount):
        self.health -= damage_amount

    def charge(self):
        self.image = self.charged

    def discharge(self):
        self.image = self.uncharged


class Meteor(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, x_speed, y_speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=(x_pos, y_pos))
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self):
        self.rect.centerx += self.x_speed
        self.rect.centery += self.y_speed

        if self.rect.centery >= 800:
            self.kill()


class Laser(pygame.sprite.Sprite):
    def __init__(self, path, pos, speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed

    def update(self):
        self.rect.centery -= self.speed
        if self.rect.centery <= -100:
            self.kill()


def main_game():
    global laser_active
    laser_group.draw(screen)
    spaceship_group.draw(screen)
    meteor_group.draw(screen)

    laser_group.update()
    spaceship_group.update()
    meteor_group.update()

    # Collision
    if pygame.sprite.spritecollide(spaceship_group.sprite, meteor_group, True):
        spaceship_group.sprite.get_damage(1)

    for laser in laser_group:
        pygame.sprite.spritecollide(laser, meteor_group, True)

    if pygame.time.get_ticks() - laser_timer >= 500:
        laser_active = True
        spaceship_group.sprite.charge()
    return 1


def end_game():
    text_surface = game_font.render('Game Over', True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(640, 340))
    screen.blit(text_surface, text_rect)

    score_surface = game_font.render(f'Score: {score}', True, (0, 0, 0))
    score_rect = score_surface.get_rect(center=(640, 380))
    screen.blit(score_surface, score_rect)


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 40)
score = 0
laser_timer = 0
laser_active = False

# Spaceship
spaceship = SpaceShip('spaceship.png', 640, 500)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

# Meteor
meteor_group = pygame.sprite.Group()
METEOR_EVENT = pygame.USEREVENT
pygame.time.set_timer(METEOR_EVENT, 250)

# Laser
laser_group = pygame.sprite.Group()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == METEOR_EVENT:
            meteor_path = random.choice(['covid1.png', 'covid2.png', 'covid3.png'])
            random_x_pos = random.randrange(0, 1280)
            random_y_pos = random.randrange(-500, -50)
            random_x_speed = random.randrange(-1, 1)
            random_y_speed = random.randrange(4, 10)
            meteor = Meteor(meteor_path, random_x_pos, random_y_pos, random_x_speed, random_y_speed)
            meteor_group.add(meteor)
        if event.type == pygame.MOUSEBUTTONDOWN and laser_active:
            laser = Laser('Laser.png', pygame.mouse.get_pos(), 10)
            laser_group.add(laser)
            laser_active = False
            laser_timer = pygame.time.get_ticks()
            spaceship_group.sprite.discharge()
        if event.type == pygame.MOUSEBUTTONDOWN and spaceship_group.sprite.health <= 0:
            spaceship_group.sprite.health = 5
            meteor_group.empty()
            score = 0

    screen.fill((255, 255, 255))
    if spaceship_group.sprite.health > 0:
        score += main_game()
    else:
        end_game()
    pygame.display.update()
    clock.tick(120)
