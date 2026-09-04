import asyncio
import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

PLAYER_SIZE = 50
SPEED = 10 # 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Pygame Game")

font = pygame.font.SysFont(None, 30)

x = 375
y = 275


def is_legal_move(x_pos, y_pos, direction, player_size=PLAYER_SIZE, player_speed=SPEED, screen_width=WIDTH, screen_height=HEIGHT) -> bool:
    match direction:
        case 'left':
            return x_pos - player_speed >= 0
        case 'right':
            return x_pos + player_speed <= screen_width - player_size
        case 'up':
            return y_pos - player_speed >= 0
        case 'down':
            return y_pos + player_speed <= screen_height - player_size
        case _:
            raise ValueError(f"Invalid direction: '{direction}'")


async def main():
    global x, y

    running = True

    while running:
    
        # EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # INPUT
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and is_legal_move(x, y, 'left'):
            x -= SPEED

        if keys[pygame.K_RIGHT] and is_legal_move(x, y, 'right'):
            x += SPEED

        if keys[pygame.K_UP] and is_legal_move(x, y, 'up'):
            y -= SPEED

        if keys[pygame.K_DOWN] and is_legal_move(x, y, 'down'):
            y += SPEED

        # DRAW
        screen.fill((30, 30, 60))

        pygame.draw.rect(
            screen,
            (255, 200, 50),
            (x, y, PLAYER_SIZE, PLAYER_SIZE)
        )

        ############ X, y
        position_text = font.render(f"X: {x}, Y: {y}", True, (255, 255, 255))
        screen.blit(position_text, (10, 10))


        pygame.display.flip()

        # Required for running Pygame in the browser
        await asyncio.sleep(0)

    pygame.quit()


asyncio.run(main())