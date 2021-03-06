#ptt_03_mouse.py
#3. 마우스 입력 처리

import pygame

#파이게임 초기화
pygame.init()

#변수 초기화
SCREEN_WIDTH = SCREEN_HEIGHT = 450
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

#화면 초기화
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("TIC TAC TOE")

#게임 변수 초기화
WHITE = (255, 255, 255)
CELL_SIZE = 150
ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE
COL_COUNT = SCREEN_WIDTH // CELL_SIZE

#격자 그리기 함수 draw_grid
def draw_grid():
    for gy in range(ROW_COUNT):
        for gx in range(ROW_COUNT):
            one_rect = pygame.Rect(gx * CELL_SIZE, gy * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, one_rect, 3)


#클릭한 셀의 좌표를 보드의 좌표로 변경
def cell_to_board(tm_pos):
    row = col = -1
    for y in range(3):
        if y* CELL_SIZE <= tm_pos[1] < y * CELL_SIZE + CELL_SIZE:
            row = y
    for x in range(3):
        if x * CELL_SIZE <= tm_pos[0] < x * CELL_SIZE + CELL_SIZE:
            col = x

    return row, col



#게임루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_pos = pygame.mouse.get_pos()
            print("클릭 좌표:", m_pos[0], m_pos[1])
            print("버튼:", event.button)

            r,c = cell_to_board(m_pos)
            print("행: {}, 열: {}".format(r, c))

            #마우스 오른쪽 버튼 클릭하면 게임 종료
            if event.button == 3:
                running = False

    #격자그리기
    draw_grid()



    #화면 업데이트
    pygame.display.update()

#파이게임 종료
pygame.quit()