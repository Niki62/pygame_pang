#ptt_01_board.py
#파이게임 틱택토

import pygame

#파이게임 초기화
pygame.init()

#변수 초기화
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 450
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

#파이게임 화면 초기화
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("TIC TACK TOE")

#게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False