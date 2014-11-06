import sys, pygame
import time
import random
pygame.init()

size = width, height = 1280, 960
gravity = 0.05
black = 0, 0, 0

screen = pygame.display.set_mode(size)

particles = []
for i in range(100):
    particle = pygame.image.load("casa_silicon_ions_40.jpg")
    particlerect = particle.get_rect()
    particlerect.x = width / 2
    particlerect.bottom = height
    speed = [random.uniform(-3, 3), random.uniform(-10, -5)]
    particles.append((particle, particlerect, speed))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(black)

    for particle, particlerect, speed in particles:
        particlerect.x += speed[0]
        particlerect.y += speed[1]
        speed[1] += gravity

        screen.blit(particle, particlerect)

    pygame.display.flip()
    time.sleep(0.01)
