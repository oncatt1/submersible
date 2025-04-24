import pygame
# all measurements are in SI units
pygame.init()
WIDTH, HEIGHT = 1280, 720
GRAVITY = 9.81
DT = 0.1
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
water = pygame.Rect(0, HEIGHT/2, WIDTH, HEIGHT/2)
class Block:
    def __init__(self, x, y, width, height, color, density):
        self.rect = pygame.Rect(x, y, width, height)
        self.area = width * height
        self.mass = density * self.area
        self.color = color
        self.speed = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)

    def update(self, dt):
        self.acceleration = pygame.Vector2(0, self.Forces() / self.mass)

        if self.inWater():
            self.acceleration = pygame.Vector2(0,0)
            return
        self.speed += self.acceleration * dt
        self.rect.x += self.speed.x
        self.rect.y += self.speed.y

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def inWater(self):
        if self.rect.y >= water.y:
            return True
        else:
            return False
        
    def Forces(self):
        Fbuoyant = Densities[0] * self.area * GRAVITY
        Fgravity = self.mass * GRAVITY

        return Fbuoyant - Fgravity
        
Rects = []
Densities = [1000, 750] # water, some wood avarage

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  
            mouse_x, mouse_y = pygame.mouse.get_pos()
            Rects.append(Block(mouse_x, mouse_y, 10, 10, "brown", Densities[1]))

    screen.fill("gray")
    pygame.draw.rect(screen, blue", water)

    for x in Rects:
        x.update(DT)
        x.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()