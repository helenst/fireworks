import sys, pygame
import time
import random
pygame.init()

size = width, height = 1280, 960
gravity = 0.01
black = 0, 0, 0

screen = pygame.display.set_mode(size)

particles = []
for i in range(10):
    particle = pygame.image.load("casa_silicon_ions_40.jpg")
    particlerect = particle.get_rect()
    particlerect.x = width / 2
    particlerect.bottom = height
    speed = [random.randint(-3, 3), random.randint(-10, -5)]
    particles.append((particle, particlerect, speed))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(black)

    for particle, particlerect, speed in particles:
        particlerect.x += speed[0]
        particlerect.y += speed[1]
#       particlerect = particlerect.move(speed)
        speed[1] += gravity
        print(speed)
        print(particlerect.x, particlerect.y)

        screen.blit(particle, particlerect)

    pygame.display.flip()
    time.sleep(0.01)
