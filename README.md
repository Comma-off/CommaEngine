# CommaEngine
CommaEngine is an "engine" made as a wrapper for pygame and pymunk.

# Usage
Very limited at the moment. It is still in development.

# Requirements
pip install pygame pymunk

# How to use
1. Download CommaEngine.py from the repo
2. Place it near your game's .py file
3. Add import CommaEngine into the game's code
4. Start building something with it!

# Example of usage
```
# Made using CommaEngine

import CommaEngine
import pygame
import time

mainWindow = CommaEngine.initWindow(1000, 1000)

running = True

CommaEngine.initSpace(0, -1000)
sample = CommaEngine.newSprite("sample", 50, 50, 50, 100, 100)

while running:
    running = CommaEngine.updateWndw()

    CommaEngine.spritePos(1/60)

    CommaEngine.drawOnWndw(mainWindow, (100, 100, 100))
    CommaEngine.drawText(mainWindow, "Running using CommaEngine v0.0.1!", 5, 5, 15, (255, 255, 255))
    pygame.display.flip()

CommaEngine.killWindow()
```

# Roadmap
2026 - v0.0.1: The Beginning
- Basic tasks can be done using CommaEngine
- Window creation, physics space, sprites, text, and simple drawing
- Functional API foundation (no classes, pure functions)
     
     
2026–2027 - v0.0.2 to v1.0.0: Becoming a Real Engine
- More features without directly touching PyGame
- Sprite rendering
- Keyboard & mouse input
- Sound support
- Delta‑time system
- Basic utilities (timers, colors, shapes)
      
     
2028–20XX - v1.0.1 to v?.?.?: The Dream Era
- More advanced features
- Maybe super basic 3D (no promises, just vibes)
- Experimental modules
**Remember, everything in the roadmap is in plans. No promises, just vibes.**

# License
This project is licensed under the MIT License.     
     
See the LICENSE file for details.     
Pull requests and issues are welcome.
