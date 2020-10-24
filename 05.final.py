#pypang_final
#파이팡 게임 만들기

import pygame
import os
#1. 파이게임 초기화
#2. 게임환경 초기화
#3. 캐릭터 이동
#4. 무기 발사
#5. 공 추가
#6. 공 나누기
#7. 메세지 출력

#파이게임 초기화
pygame.init()

screen_width = 640
screen_height = 480
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('PYPANG!!')

#이미지 불러오기
cur_path = os.path.dirname(__file__)
img_path = os.path.join(cur_path, 'images')

background_img = pygame.image.load(os.path.join(img_path, 'background.png'))
stage_img = pygame.image.load(os.path.join(img_path, 'stage.png'))
stage_height = stage_img.get_rect().size[1]

character_img = pygame.image.load(os.path.join(img_path,'character.png'))
character_rect = character_img.get_rect().size
character_width = character_rect[0]
character_height = character_rect[1]
character_x_pos = screen_width // 2 - character_width // 2
character_y_pos = screen_height - stage_height - character_height

#게임루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #화면 출력
    screen.blit(background_img, (0,0))
    screen.blit(stage_img, (0, screen_height - stage_height))
    screen.blit(character_img, (character_x_pos, character_y_pos))

    #화면 업데이트
    pygame.display.update()

#파이게임 종료
pygame.quit()