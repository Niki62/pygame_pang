#공만들기
import pygame
import os

#초기화
pygame.init()

#프레임 설정
clock = pygame.time.Clock()

#생성
screen_width=640
screen_height=480
screen_size=(screen_width,screen_height)
screen=pygame.display.set_mode(screen_size)
pygame.display.set_caption("PYPANG!")

#배경이미지
cu_path = os.path.dirname(__file__)
img_path = os.path.join(cu_path, "images")
bg = pygame.image.load(os.path.join(img_path, "background.png"))

#바닥이미지
stage = pygame.image.load(os.path.join(img_path, "stage.png"))
stage_size=stage.get_rect().size
stage_height=stage_size[1]

#캐릭터이미지
character = pygame.image.load(os.path.join(img_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width // 2 - character_width // 2
character_y_pos = screen_height - stage_height - character_height
character_speed = 0

#무기이미지
weapon = pygame.image.load(os.path.join(img_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_speed = 10

#무기저장소
weapons = []

#공 만들기
ball_images = [
    pygame.image.load(os.path.join(img_path, "balloon1.png")),
    pygame.image.load(os.path.join(img_path, "balloon2.png")),
    pygame.image.load(os.path.join(img_path, "balloon3.png")),
    pygame.image.load(os.path.join(img_path, "balloon4.png"))
]

ball_speed_y = [-18, -15, -12, -9]

#초기 공 추가
balls=[]
balls.append(
    {
        "pos_x" : 50,
        "pos_y" : 50,
        "img_idx" : 0,
        "to_x" : 3,
        "to_y" : -6,
        "init_spd_y" : ball_speed_y[0]
    }
)

#게임루프
running=True
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_speed -= 5
            elif event.key == pygame.K_RIGHT:
                character_speed += 5
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width//2)-(weapon_width//2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT == pygame.K_RIGHT:
                    character_speed = 0

    #게임 캐릭터 위치 업데이트
    character_x_pos += character_speed

    if character_x_pos < 0:
        character_x_pos = 0
    if character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #무기 위치 조정
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]

    #천장에 닿은 무기 제거
    weapons = [[w[0],w[1]] for w in weapons if w[1] > 0]
    #print(weapons)

    #공 위치 변경
    for ball_idx, ball_one in enumerate(balls):
        #print(ball_idx, ball_one)
        ball_pos_x = ball_one["pos_x"]
        ball_pos_y = ball_one["pos_y"]
        ball_img_idx = ball_one["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        if ball_pos_y > screen_height - stage_height - ball_height:
            ball_one["to_y"] = ball_one["init_spd_y"]
        else:
            ball_one["to_y"] += 0.5
        ball_one["pos_x"] += ball_one["to_x"]
        ball_one["pos_y"] += ball_one["to_y"]

    screen.blit(bg, (0,0))
    screen.blit(stage,(0,screen_height-stage_height))
    screen.blit(character,(character_x_pos,character_y_pos))
    for one in weapons:
        screen.blit(weapon, (one[0], one[1]))

    for idx, one in enumerate(balls):
        ball_pos_x = one["pos_x"]
        ball_pos_y = one["pos_y"]
        ball_img_idx = one["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))
    pygame.display.update()



#종료
pygame.quit()