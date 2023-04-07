import pygame

from fong.fong_ball import FongBall

WINDOW_X_SIZE = 400
WINDOW_Y_SIZE = 400

window = pygame.display.set_mode((WINDOW_X_SIZE, WINDOW_Y_SIZE))
active = True
ball = FongBall()

refresh = True

while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    if refresh:
        pygame.draw.rect(window, (0, 0, 0), (0, 0, WINDOW_X_SIZE, WINDOW_Y_SIZE))
        ball.create_image(window)
        pygame.display.update()
        refresh = False
