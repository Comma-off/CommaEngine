import CommaEngine
import pygame
import time

mainWindow = CommaEngine.initWindow(1000, 1000)

running = True

CommaEngine.initSpace(0, -1000)
sample = CommaEngine.newSprite("sample", 50, 50, 50, 100, 100)

while running:
    running = CommaEngine.updateWndw()

    CommaEngine.spritePos(1)

    CommaEngine.drawOnWndw(mainWindow, (100, 100, 100))
    CommaEngine.drawText(mainWindow, "Running using CommaEngine v0.0.1!", 5, 5, 15, (255, 255, 255))
    CommaEngine.drawText(mainWindow, "Running using CommaEngine v0.0.1!", 0, 0, 15, (0, 0, 0))
    pygame.display.flip()

CommaEngine.killWindow()