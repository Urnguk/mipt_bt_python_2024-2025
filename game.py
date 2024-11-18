import pygame
import numpy as np

WIDTH = 800
HEIGHT = 600
FPS = 120

BLACK = (0, 0, 0)
GREY = (128, 128, 128)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((10, 10))
        # self.image.fill(BLACK)

        self.image = pygame.image.load("7051535387.jpg")
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.prev_time = pygame.time.get_ticks()
        self.v = 0
        self.phi = 0
        self.w = 0
        self.a = 0

    def update(self):
        curr_time = pygame.time.get_ticks()
        dt = curr_time - self.prev_time
        self.v += self.a * dt
        self.v *= 0.99 ** (dt / 10)
        self.phi += self.w ** (dt / 10)
        if self.v > 1:
            self.v = 1
        elif self.v < 0:
            self.v = 0
        self.rect.x += self.v * np.cos(self.phi) * dt
        self.rect.y += self.v * np.sin(self.phi) * dt
        if self.rect.right > WIDTH:
            self.phi = np.pi - self.phi
            self.rect.right = WIDTH - (self.rect.right - WIDTH)
        if self.rect.left < 0:
            self.phi = np.pi - self.phi
            self.rect.left = abs(self.rect.left)
        if self.rect.top > HEIGHT:
            self.phi = -self.phi
            self.rect.top = HEIGHT - (self.rect.top - HEIGHT)
        if self.rect.bottom < 0:
            self.phi = -self.phi
            self.rect.bottom = abs(self.rect.bottom)
        self.prev_time = curr_time


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

arial_font = pygame.font.SysFont("Arial", 20)
text = arial_font.render("quit", True, WHITE)

running = True
while running:
    clock.tick(FPS)
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.w = 0
            if event.key == pygame.K_LEFT:
                player.w = 0
            if event.key == pygame.K_SPACE:
                all_sprites.remove(player)
            if event.key == pygame.K_UP:
                player.a = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.a = 0.001
            if event.key == pygame.K_RIGHT:
                player.w = 0.005
            if event.key == pygame.K_LEFT:
                player.w = -0.005



        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if WIDTH / 2 <= mouse_pos[0] <= WIDTH / 2 + 140 and HEIGHT / 2 <= mouse_pos[1] <= HEIGHT / 2 + 40:
        #         running = False
    #
    all_sprites.update()
    # collisions = pygame.sprite.spritecollide(player, group_of_entites, False)


    screen.fill(GREEN)
    # pygame.draw.rect(screen, GREY, [WIDTH / 2, HEIGHT / 2, 140, 40])
    # screen.blit(text, (WIDTH / 2 + 60, HEIGHT / 2 + 10))

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
