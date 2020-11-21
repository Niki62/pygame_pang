#ptt_01_board.py
#파이게임 틱택토

import pygame

#파이게임 초기화
pygame.init()

#변수 초기화
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 450
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

#화면설정
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("TIC TAC TOE")

#게임 변수 설정
WHITE = (255, 255, 255)
CELL_SIZE = 150
ROW_COUNT = SCREEN_HEIGHT // 3
COL_COUNT = SCREEN_WIDTH // 3

#게임루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #사각형 그리기
    # pygame.draw.rect(screen, (255, 255, 255), (0, 0, 150, 150), 1)
    # pygame.draw.rect(screen, (255, 255, 255), (150, 0, 150, 150), 1)
    # pygame.draw.rect(screen, (255, 255, 255), (300, 0, 150, 150), 1)
    # pygame.draw.rect(screen, (255, 255, 255), (0, 150, 150, 150), 1)
    # pygame.draw.rect(screen, (255, 255, 255), (150, 150, 150, 150), 1)
    # pygame.draw.rect(screen, (255, 255, 255), (300, 150, 150, 150), 1)
    # pygame.draw.rect(screen, (255, 255, 255), (0, 300, 150, 150), 1)
    # pygame.draw.rect(screen, (255, 255, 255), (150, 300, 150, 150), 1)
    # pygame.draw.rect(screen, (255, 255, 255), (300, 300, 150, 150), 1)

    for y in range(3):
        for x in range(3):
            one_rect = (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, one_rect, 1)

    #화면 업데이트
    pygame.display.update()

#파이게임 종료
pygame.quit()