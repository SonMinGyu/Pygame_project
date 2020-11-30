import pygame
import os
########################################################################
# 기본 초기화 (반드시 해야하는 부분)
pygame.init()  # 초기화(반드시 해야함)

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("My Pang")  # 게임이름

# FPS
clock = pygame.time.Clock()
########################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
current_path = os.path.dirname(__file__)  # 현재 파일 위치 반환
image_path = os.path.join(current_path, "images")

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]  # 스테이지 높이 위에 캐릭터 두기위해 저장

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 이동 속도
character_speed = 1

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한 번에 여러 발 발사 가능
weapons = []
weapon_speed = 5

running = True  # 게임이 진행중인가
while running:
    dt = clock.tick(120)  # 게임화면의 초당 프레임 수 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():  # 어떤 이벤트 발생?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트 실행시
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + \
                    (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        character_to_x -= character_speed
        character_x_pos += character_to_x * dt
        if character_x_pos < 0:
            character_x_pos = 0
        character_to_x = 0
    if keys[pygame.K_RIGHT]:
        character_to_x += character_speed
        character_x_pos += character_to_x * dt
        if character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width
        character_to_x = 0

    # if keys[pygame.K_SPACE]:
    #     weapon_x_pos = character_x_pos + \
    #         (character_width / 2) - (weapon_width / 2)
    #     weapon_y_pos = character_y_pos
    #     weapons.append([weapon_x_pos, weapon_y_pos])

    # 3. 게임 캐릭터 위치 정의 (이벤트 처리와 함께 처리 가능)

    # 무기 위치 조정
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]  # 무기 위치 위로

    # 천장에 닿은 무기 없애기
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()  # 게임화면 다시 그리기

# pygame 종료
pygame.quit()
