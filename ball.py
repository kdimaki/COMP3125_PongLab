import pygame

class Ball:
    RADIUS = 15
    vx = 1
    vy = 1

    def __init__(self, x, y, vx, vy, screen, fgcolor, bgcolor, dimensions):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.screen = screen
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.dimensions = dimensions

    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)
    
    def update(self):
        self.show(self.bgcolor)
        self.x = self.x + self.vx
        self.y = self.y + self.vy

        #check for collisions
        px = self.x + self.vx
        py = self.y + self.vy

        #right
        if( ( px - self.RADIUS ) <= self.dimensions[2]):
            self.vx = -self.vx

        #top
        if( ( py - self.RADIUS ) <= self.dimensions[2]):
            self.vy = -self.vy

        #bottom
        if( ( py + self.RADIUS ) >= self.dimensions[1] - self.dimensions[2]):
            self.vy = -self.vy

        self.show(self.fgcolor)