import asyncio
import pygame
import sys
import time

# 초기화
pygame.init()

# 화면 크기 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 색상 정의
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# 폰트 설정
font_path = "Paperlogy-4Regular.ttf"  # 일반 폰트 경로
bold_font_path = "Paperlogy-8ExtraBold.ttf"  # 굵은 폰트 경로

font = pygame.font.Font(bold_font_path, 40)
small_font = pygame.font.Font(font_path, 28)

# 게임 설명서
def show_instructions():
    screen.fill(white)
    
    title = font.render("Non zero-centered problem", True, black)
    instructions = small_font.render("목표: 빨간 공에 도달하세요.", True, black)
    controls1 = small_font.render("입력키의 부호가 같은 방향으로만 움직일 수 있습니다", True, black)
    controls2 = small_font.render("오른쪽 위로 이동, 왼쪽 아래로 이동", True, black)
    start_message = small_font.render("시작하려면 아무 키나 누르세요.", True, red)
    
    screen.blit(title, (screen_width // 2 - title.get_width() // 2, screen_height // 4))
    screen.blit(instructions, (screen_width // 2 - instructions.get_width() // 2, screen_height // 4 + 60))
    screen.blit(controls1, (screen_width // 2 - controls1.get_width() // 2, screen_height // 4 + 120))
    screen.blit(controls2, (screen_width // 2 - controls2.get_width() // 2, screen_height // 4 + 180))
    screen.blit(start_message, (screen_width // 2 - start_message.get_width() // 2, screen_height // 2 + 100))
    
    pygame.display.flip()
    
    # 대기 상태, 키 입력 대기
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

async def main():
    global current_pos, path, goal_reached, start_time, elapsed_time
    reset_game()

    clock = pygame.time.Clock()  # 프레임 레이트 제어를 위해 시계 객체 생성

    while True:
        screen.fill(white)
        
        # 목표 지점 그리기
        pygame.draw.circle(screen, red, target_pos, 10)
        
        # 경로 그리기
        for i in range(len(path) - 1):
            pygame.draw.line(screen, blue, path[i], path[i + 1], 5)
        
        # 현재 위치 그리기
        pygame.draw.circle(screen, black, current_pos, 10)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and goal_reached:
                if event.key == pygame.K_RETURN:
                    reset_game()  # 게임 리셋
        
        keys = pygame.key.get_pressed()
        
        if not goal_reached:
            if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
                # 오른쪽 위 대각선으로 이동 (기울기 조정)
                current_pos[0] += move_x_right_up
                current_pos[1] -= move_y_right_up
            elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
                # 왼쪽 아래 대각선으로 이동 (기울기 조정)
                current_pos[0] -= move_x_left_down
                current_pos[1] += move_y_left_down
        
            # 실시간 경과 시간 계산 및 표시
            elapsed_time = time.time() - start_time
            time_display = small_font.render(f"시간: {elapsed_time:.2f}초", True, black)
            screen.blit(time_display, (10, 10))  # 화면 좌측 상단에 경과 시간 표시
        
        # 화면 경계 체크 (화면 밖으로 나가지 않도록)
        current_pos[0] = max(0, min(current_pos[0], screen_width))
        current_pos[1] = max(0, min(current_pos[1], screen_height))
        
        # 이동 후 경로에 추가
        if path[-1] != current_pos:  # 이전 위치와 다를 때만 경로에 추가
            path.append(current_pos.copy())
        
        # 목표 지점에 도달했는지 확인
        if not goal_reached and (abs(current_pos[0] - target_pos[0]) < 10 and abs(current_pos[1] - target_pos[1]) < 10):
            goal_reached = True
            elapsed_time = time.time() - start_time  # 경과 시간을 목표 지점 도달 시점에서 멈춤
        
        # 목표 지점 도달 알림
        if goal_reached:
            message = font.render("목표 지점에 도달했습니다!", True, red)
            time_message = small_font.render(f"소요 시간: {elapsed_time:.2f}초", True, red)
            restart_message = small_font.render("다시 시작하려면 엔터키를 누르세요.", True, red)
            screen.blit(message, (screen_width // 2 - message.get_width() // 2, screen_height // 2 - message.get_height() // 2))
            screen.blit(time_message, (screen_width // 2 - time_message.get_width() // 2, screen_height // 2 + 50))
            screen.blit(restart_message, (screen_width // 2 - restart_message.get_width() // 2, screen_height // 2 + 100))
            pygame.display.flip()

        # 화면 업데이트
        pygame.display.flip()
        clock.tick(60)  # 프레임 레이트를 60 FPS로 설정하여 부드러운 움직임 제공
        await asyncio.sleep(0)  # 메인 스레드로 제어를 넘김

def reset_game():
    global current_pos, path, goal_reached, start_time, elapsed_time
    current_pos = start_pos.copy()
    path = [current_pos.copy()]
    goal_reached = False
    start_time = time.time()  # 게임 시작 시간 기록
    elapsed_time = 0  # 경과 시간 초기화

# 초기 위치와 목표 지점 설정
start_pos = [50, 50]  # 좌측 상단 시작
target_pos = [screen_width - 50, screen_height - 50]  # 우측 하단 목표
current_pos = start_pos.copy()

# 경로를 추적하기 위한 리스트
path = [current_pos.copy()]

# 이동 속도 설정 (더 부드러운 이동을 위해 속도를 낮춤)
move_x_right_up = 5
move_y_right_up = 3

move_x_left_down = 3
move_y_left_down = 5

goal_reached = False
start_time = None
elapsed_time = 0

# 게임 시작 전 설명서 표시
show_instructions()

asyncio.run(main())