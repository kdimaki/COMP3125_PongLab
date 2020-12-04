#from paddle import Paddle
from ball import Ball
import pygame
import random


def main():
    pygame.init()

    pygame.display.set_caption("PyGame")
    WIDTH = 1000
    HEIGHT = 500
    BORDER = 25
    FPS = 360 #if errors occur try it with 220, 144, or your machine's equivelant

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    screen.fill((0, 0, 0))
    pygame.display.update()

    wcolor = pygame.Color("red")
    bgcolor = pygame.Color("black")

    #top
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (WIDTH, BORDER)))

    #left
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (BORDER, HEIGHT)))

    #bottom
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, HEIGHT - BORDER), (WIDTH, HEIGHT)))


    x0 = WIDTH - Ball.RADIUS
    y0 = HEIGHT // 2

    vx = -random.randint(1, 5)
    vy = -random.randint(1, 5)
    b0 = Ball(x0, y0, vx, vy, screen, wcolor, bgcolor, [WIDTH, HEIGHT, BORDER])
    b0.show(wcolor)
    
    clock = pygame.time.Clock()

    running = True
    print(screen)

    pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        clock.tick(FPS)
        b0.update()




if __name__ == "__main__":
    main()