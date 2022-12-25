import sys
import pygame
from settings import *

pygame.init()

# create the screen
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Cuck simulator")
clock = pygame.time.Clock()

# player
playerImg = pygame.image.load("paddle.png")
playerCoor = [width / 2, height * 0.70]
xChange = 0

def player():
    screen.blit(playerImg, (playerCoor))
    playerCoor[0] += xChange
# ball
ballImg = pygame.image.load("ball.png")
ballCoor = [(width / 2)+60, 250]
ball_xy_mov = [5,-5]

# enemy
enemyImg = pygame.image.load("esamc.png")
enemyCoor = [0,0]
def enemy():
    screen.blit(enemyImg, ((0 + 150),0) )

    

def ball():
    ball = screen.blit(ballImg, (ballCoor))
    ballCoor [0] += ball_xy_mov[0]
    ballCoor [1] += ball_xy_mov[1]
    
def map_collision():
    #ball bounce
    if ballCoor[0] == 0:
        ball_xy_mov[0] *= -1
    elif ballCoor[0] == 775:
        ball_xy_mov[0] *= -1
    if ballCoor[1] == 0:
        ball_xy_mov[1] *= -1
    elif ballCoor[1] == 605:
        ballCoor [0] = (width / 2)+60; ballCoor[1] = 250

    #ball touches the brick
    if ballCoor[1] == (enemyCoor[1] + 15):
        if ballCoor[0] >= (enemyCoor[0] - 15) and ballCoor[0] <= (enemyCoor[0] + 50):
            ball_xy_mov[1] *= -1

    #ball touches the player
    if ballCoor[1] == (playerCoor[1] - 25):
        if ballCoor[0] >= playerCoor[0] and ballCoor[0] <= (playerCoor[0] + 150):
            ball_xy_mov[1] *= -1

    #player limit
    if playerCoor[0] <= 0:
        playerCoor[0] = 0
    elif playerCoor[0] >= 650:
        playerCoor[0] = 650

# game loop
running = True
while running:
    screen.fill(bg_color)
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xChange = -5
            if event.key == pygame.K_RIGHT:
                xChange = 5  
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xChange = 0
    map_collision()
    player()
    ball()
    enemy()
    pygame.display.update()