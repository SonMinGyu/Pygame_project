import pygame
########################################################################
# 기본 초기화 (반드시 해야하는 부분)
pygame.init()  # 초기화(반드시 해야함)

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("make_my_game")  # 게임이름

# FPS
clock = pygame.time.Clock()
########################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

running = True  # 게임이 진행중인가
while running:
    dt = clock.tick(120)  # 게임화면의 초당 프레임 수 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():  # 어떤 이벤트 발생?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트 실행시
            running = False

    # 3. 게임 캐릭터 위치 정의 (이벤트 처리와 함께 처리 가능)

    # 4. 충돌 처리

    # 5. 화면에 그리기

    pygame.display.update()  # 게임화면 다시 그리기

# pygame 종료
pygame.quit()
