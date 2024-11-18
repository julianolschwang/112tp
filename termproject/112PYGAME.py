import pygame
import random
pygame.init()

#onAppStart
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Geometry Dash (Julian Edition)")
clock = pygame.time.Clock()
gravity = 0.7
jump_speed = -15
fall_speed = 0
ground_height = 50
game_speed = 5 + 0.001 * pygame.time.get_ticks()
score = 0
font = pygame.font.SysFont("Arial", 30)

# class for player and obstacles
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((173, 216, 230))
        self.rect = self.image.get_rect()
        self.rect.center = (100, height - ground_height - 50)
        self.y_velocity = 0

    def update(self):
        global fall_speed
        self.y_velocity += gravity
        self.rect.y += self.y_velocity
        
        if self.rect.bottom >= height - ground_height:
            self.rect.bottom = height - ground_height
            self.y_velocity = 0

    def jump(self):
        if self.rect.bottom == height - ground_height:
            self.y_velocity = jump_speed

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 20
        self.height = random.randint(50, 100)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((238, 75, 43))
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = height - self.height - ground_height    

    def update(self):
        self.rect.x -= game_speed
        if self.rect.right < 0:
            self.kill()

class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = width
        self.height = ground_height
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((57, 255, 100))
        self.rect = self.image.get_rect()
        self.rect.x = width - self.width
        self.rect.y = height - self.height
        

def display_score():
    score_text = font.render(f"Score: {score}", True, (128, 128, 128))
    screen.blit(score_text, (10, 10))

def main():
    global score, game_speed
    running = True
    player = Player()
    ground = Floor()
    all_sprites = pygame.sprite.Group(player, ground)
    obstacles = pygame.sprite.Group()
    last_obstacle_time = pygame.time.get_ticks()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()

        all_sprites.update()
        
        if pygame.time.get_ticks() - last_obstacle_time > 1500:
            last_obstacle_time = pygame.time.get_ticks()
            new_obstacle = Obstacle()
            obstacles.add(new_obstacle)
            all_sprites.add(new_obstacle)

        if pygame.sprite.spritecollide(player, obstacles, False):
            running = False
            
        score += 1

        screen.fill((0, 0, 128))
        all_sprites.draw(screen)
        display_score()

        pygame.display.flip()

        clock.tick(60)

if __name__ == "__main__":
    main()