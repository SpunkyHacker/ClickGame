import pygame
import time

WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("click game")

clock = pygame.time.Clock()
FPS = 60

class Button():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.button = pygame.Rect(self.x, self.y, self.width, self.height)
        self.clicked = False

    def draw(self):
        
        pos = pygame.mouse.get_pos()

        if self.button.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            
        
        pygame.draw.rect(screen, (255, 255, 255), self.button)
        pygame.display.flip()


def main():
    clock.tick(FPS)

    button = Button(10, 10, 50, 50)

    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        screen.fill((0, 0, 0))
        time.sleep(1)
        button.draw()
        pygame.display.update()




if __name__ == "__main__":
    main()