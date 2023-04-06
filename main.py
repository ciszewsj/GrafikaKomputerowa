import pygame
from pygame import K_p, K_o, K_l, K_k, K_m, K_n, K_q, K_w, K_s, K_a, K_x, K_z, K_c, K_v

from camera import Camera
from shapes.cube import Cube

WHITE = (255, 255, 255)
BLUE = (0, 9, 255)
RED = (255, 1, 0)
PINK = (255, 0, 177)
YELLOW = (255, 227, 0)
GREEN = (0, 255, 13)
ORANGE = (255, 95, 31)
PURPLE = (171, 32, 253)

WINDOW_X_SIZE = 1280
WINDOW_Y_SIZE = 720

DISTANCE_FROM_CAMERA = 450
DISTANCE_BETWEEN_POINTS = 150
DISTANCE_FROM_CENTER = 100

window = pygame.display.set_mode((WINDOW_X_SIZE, WINDOW_Y_SIZE))

active = True
cubes = [
    Cube(DISTANCE_FROM_CENTER, DISTANCE_FROM_CENTER, DISTANCE_FROM_CENTER, WHITE, DISTANCE_FROM_CAMERA,
         DISTANCE_BETWEEN_POINTS),
    Cube(-DISTANCE_FROM_CENTER, DISTANCE_FROM_CENTER, DISTANCE_FROM_CENTER, BLUE, DISTANCE_FROM_CAMERA,
         DISTANCE_BETWEEN_POINTS),
    Cube(DISTANCE_FROM_CENTER, -DISTANCE_FROM_CENTER, DISTANCE_FROM_CENTER, RED, DISTANCE_FROM_CAMERA,
         DISTANCE_BETWEEN_POINTS),
    Cube(DISTANCE_FROM_CENTER, DISTANCE_FROM_CENTER, -DISTANCE_FROM_CENTER, PINK, DISTANCE_FROM_CAMERA,
         DISTANCE_BETWEEN_POINTS),
    Cube(-DISTANCE_FROM_CENTER, -DISTANCE_FROM_CENTER, DISTANCE_FROM_CENTER, YELLOW, DISTANCE_FROM_CAMERA,
         DISTANCE_BETWEEN_POINTS),
    Cube(-DISTANCE_FROM_CENTER, DISTANCE_FROM_CENTER, -DISTANCE_FROM_CENTER, GREEN, DISTANCE_FROM_CAMERA,
         DISTANCE_BETWEEN_POINTS),
    Cube(DISTANCE_FROM_CENTER, -DISTANCE_FROM_CENTER, -DISTANCE_FROM_CENTER, ORANGE, DISTANCE_FROM_CAMERA,
         DISTANCE_BETWEEN_POINTS),
    Cube(-DISTANCE_FROM_CENTER, -DISTANCE_FROM_CENTER, -DISTANCE_FROM_CENTER, PURPLE, DISTANCE_FROM_CAMERA,
         DISTANCE_BETWEEN_POINTS)
]
clock = pygame.time.Clock()

camera = Camera(cubes)
while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_p:
                camera.move_up()
            if event.key == K_o:
                camera.move_down()
            if event.key == K_k:
                camera.move_left()
            if event.key == K_l:
                camera.move_right()
            if event.key == K_n:
                camera.move_forward()
            if event.key == K_m:
                camera.move_back()

            if event.key == K_w:
                camera.rotate_x(1)
            if event.key == K_q:
                camera.rotate_x(-1)
            if event.key == K_a:
                camera.rotate_y(1)
            if event.key == K_s:
                camera.rotate_y(-1)
            if event.key == K_x:
                camera.rotate_z(1)
            if event.key == K_z:
                camera.rotate_z(-1)

            if event.key == K_c:
                camera.scale_down()
            if event.key == K_v:
                camera.scale_up()
    pygame.draw.rect(window, (0, 0, 0), (0, 0, WINDOW_X_SIZE, WINDOW_Y_SIZE))
    camera.draw(window, 450, WINDOW_X_SIZE, WINDOW_Y_SIZE)
    pygame.display.update()
    clock.tick(1000)
