import pygame
import pymunk

# PyEngine. V0.0.1.

space = None

def initWindow(width2, height2):
    pygame.init()
    screen = pygame.display.set_mode((width2, height2))
    return screen

def killWindow():
    pygame.quit()

def drawOnWndw(screen, color):
    screen.fill(color)

def drawText(screen, text, x, y, size, color):
    font = pygame.font.SysFont("Arial", size)
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))

def updateWndw():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def initSpace(gravX, gravY):
    global space
    space = pymunk.Space()
    space.gravity = gravX, gravY
    return space

def newSprite(name, width, height, posX, posY, mass):
    size = (width, height)

    moment = pymunk.moment_for_box(mass, size)

    body = pymunk.Body(mass, moment)
    shape = pymunk.Poly.create_box(body, size)

    body.position = posX, posY
    space.add(body, shape)

    return body

def spritePos(dt):
    space.step(dt)

def getPos(body):
    return body.position
