import sys, pygame
import time
import random
pygame.init()

size = width, height = 1280, 960
gravity = 0.01
black = 0, 0, 0

screen = pygame.display.set_mode(size)

balls = []
for i in range(10):
    ball = pygame.image.load("ball.gif")
    ballrect = ball.get_rect()
    ballrect.x = width / 2
    ballrect.bottom = height
    speed = [random.uniform(0, 3), random.uniform(-1, -5)]
    balls.append((ball, ballrect, speed))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(black)

    for ball, ballrect, speed in balls:
        ballrect = ballrect.move(speed)
        speed[1] += gravity

        screen.blit(ball, ballrect)

    pygame.display.flip()
    time.sleep(0.01)
