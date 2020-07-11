import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

car = pygame.image.load('car.png').convert_alpha()

x, y = 50, 50
speed = 4

screen.fill((255, 255, 255))
screen.blit(car, (x, y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                flip = pygame.transform.rotate(car, -90)
                x += speed
                screen.fill((255, 255, 255))
                screen.blit(flip, (x, y + 25))

            if event.key == pygame.K_LEFT:
                flip = pygame.transform.rotate(car, 90)
                x -= speed
                screen.fill((255, 255, 255))
                screen.blit(flip, (x, y + 25))

            if event.key == pygame.K_UP:
                flip = pygame.transform.rotate(car, 0)
                y -= speed
                screen.fill((255, 255, 255))
                screen.blit(flip, (x, y))

            if event.key == pygame.K_DOWN:
                flip = pygame.transform.rotate(car, -180)
                y += speed
                screen.fill((255, 255, 255))
                screen.blit(flip, (x, y))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        flip = pygame.transform.rotate(car, -90)
        x += speed
        screen.fill((255, 255, 255))
        screen.blit(flip, (x, y + 25))

    if keys[pygame.K_LEFT]:
        flip = pygame.transform.rotate(car, 90)
        x -= speed
        screen.fill((255, 255, 255))
        screen.blit(flip, (x, y + 25))

    if keys[pygame.K_UP]:
        flip = pygame.transform.rotate(car, 0)
        y -= speed
        screen.fill((255, 255, 255))
        screen.blit(flip, (x, y))

    if keys[pygame.K_DOWN]:
        flip = pygame.transform.rotate(car, -180)
        y += speed
        screen.fill((255, 255, 255))
        screen.blit(flip, (x, y))

    pygame.display.update()
