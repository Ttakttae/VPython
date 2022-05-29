"""
<프로그램 전체 구조도>
Main -> Ball(공 관련) -> 공 생성
     -> Ball_Bar(볼 튕기는 바 관련) -> 바 생성
     -> Heart(목숨 관련) -> 목숨 설정, 남은 목숨 개수 출력
     -> Blocks(부숴야 되는 블록들 관련) -> 블록들 생성
     -> Walls(벽 관련) -> 벽들 생성

while True -> Ball.ball_movement(공 움직임 계속 되야함) -> Heart.change_text(목숨 개수 출력 변경, 게임 오버/승리 관리), Heart._heart.setter(목숨 개수 변경)
           -> Ball_Bar.bar_movement(바 움직임도 계속 활성화 상태여야 함)
    ->스페이스 바가 눌린다면 -> 화면 지우고 새로 Main 생성
"""


AI_play = False #자동 플레이 여부


from vpython import * #vpython 패키지(3d 모델링)
from random import uniform #random 함수
from time import time #시간 재기 위한 time



class Ball:
    """
    공의 이동 관련된 클래스
    """
    def __init__(self, main):
        """
        클래스 Ball 세팅
        :param main:
        """
        self.main = main
        self.make_ball() #공 생성

    def make_ball(self):
        """
        공을 생성하는 함수
        :return:
        """
        self._speed = 0.0002 #공의 속도
        self._ball = sphere(color=color.magenta, pos=vector(0, -7, 0), size=vector(0.7, 0.7, 0.7), make_trail=False)
        self._ball.v = vec(1, 1, 0) #공의 이동 방향

    @property
    def ball(self):
        """
        공 자체를 반환
        :return:
        """
        return self._ball #공 반환

    def ball_movement(self):
        """
        공의 움직임을 관리하는 함수(다른 물체와 충돌도 관리)
        :return:
        """
        self._ball.pos += self._ball.v * self._speed #기본 움직임 제어
        if self._ball.pos.x + 0.4 >= main.wall.right_wall.pos.x: #오른 벽 부딪힐 시
            self._ball.v.x = -self._ball.v.x + uniform(-0.1, 0.1) #x방향 반대로 + 약간의 무작위 방향성
        if self._ball.pos.x - 0.4 <= main.wall.left_wall.pos.x: #왼 벽 부딪힐 시
            self._ball.v.x = -self._ball.v.x + uniform(-0.1, 0.1) #x방향 반대로 + 약간의 무작위 방향성
        if self._ball.pos.y + 0.4 >= main.wall.upper_wall.pos.y: #윗 벽 부딪힐 시
            self._ball.v.y = -self._ball.v.y + uniform(-0.1, 0.1) #y방향 반대로 + 약간의 무작위 방향성
        if self._ball.pos.y - 0.5 <= main.ball_bar.ball_bar.pos.y and (self._ball.pos.x <= main.ball_bar.ball_bar.pos.x + 2.5 and self._ball.pos.x >= main.ball_bar.ball_bar.pos.x - 2.5): #바와 부딪힐 시
            self._ball.v.y = -self._ball.v.y + uniform(-0.1, 0.1) #y방향 반대로 + 약간의 무작위 방향성
            if self._ball.v.x < 0 and self._ball.pos.x > main.ball_bar.ball_bar.pos.x:
                self._ball.v.x = -self._ball.v.x + uniform(-0.1, 0.1) #왼쪽으로 이동하는 공이 바의 오른쪽 부분(중심 기준)에 맞았을 때는 오른쪽으로 튕겨나가기(원래 게임 환경 적용)
            elif self._ball.v.x > 0 and self._ball.pos.x < main.ball_bar.ball_bar.pos.x:
                self._ball.v.x = -self._ball.v.x + uniform(-0.1, 0.1) #오른쪽으로 이동하는 공이 바의 왼쪽 부분(중심 기준)에 맞았을 때는 오른쪽으로 튕겨나가기(원래 게임 환경 적용)
            else:
                pass
        if self._ball.pos.y <= main.ball_bar.ball_bar.pos.y: #구멍으로 빠질 시
            self._ball.visible = False #공을 안보이게 하고
            self._ball.__del__() #공을 전산에서 삭제(실제로는 남아 있지만 호출 불가능)
            if main.heart.heart == 0: #목숨이 안남았다면
                main.heart.heart = -1 #목숨을 -1로 만들어서 게임오버 상태 만들기 -> 게임 오버 출력(화면)
                print("Game Over!") #게임 오버 출력(콘솔창)
                main.end = True #게임 종료 변수 활성화
            else: #목숨이 남아있다면
                self.make_ball() #새로운 공 생성
                main.heart.heart = -1 #목숨 감소
        for block in main.blocks.blocks: #블록과 부딪힐 시
            if self._ball.pos.x > block.pos.x + 1.21 or self._ball.pos.x < block.pos.x - 1.21: #블록의 x좌표 범위내에 없을 경우
                pass
            elif self._ball.pos.y > block.pos.y + 0.71 or self._ball.pos.y < block.pos.y - 0.71: #블록의 y좌표 범위내에 없을 경우
                pass
            else: #블록의 x좌표 범위내에 없을 경우도 아니고 블록의 y좌표 범위내에 없을 경우도 아닌 경우 -> 블록과 닿았을 경우
                if block.color == vector(0, 1, 0): #색깔이 초록색(1단계)이면 제일 낮은 속도(기본 속도) 유지
                    pass
                elif block.color == vector(1, 1, 0): #색깔이 노란색(2단계)이면 두번째로 낮은 속도로 변경(처음 닿은 이후 계속 유지)
                    if self._speed < 0.00024: #이미 노란색에 닿은적이 있는지 확인
                        self._speed = 0.00024
                    else:
                        pass
                elif block.color == vector(1, 0.6, 0): #색깔이 주황색(3단계)이면 두번째로 높은 속도로 변경(처음 닿은 이후 계속 유지)
                    if self._speed < 0.00026: #이미 주황색에 닿은적이 있는지 확인
                        self._speed = 0.00026
                    else:
                        pass
                elif block.color == vector(1, 0, 0): #색깔이 빨간색(4단계)이면 제일 높은 속도로 변경(처음 닿은 이후 계속 유지)
                    if self._speed < 0.00028: #이미 빨간색에 닿은적이 있는지 확인
                        self._speed = 0.00028
                    else:
                        pass
                else:
                    pass
                if self._ball.pos.x <= block.pos.x + 1.21 or self._ball.pos.x >= block.pos.x - 1.21: #블록의 윗면이나 아랫면과 닿은 경우(이미 닿은 경우로 위에서 분류했으므로 x범위 안 인지만 확인만 하면 됨)
                    self._ball.v.y = -self._ball.v.y + uniform(-0.1, 0.1) #y방향 반대로 + 약간의 무작위 방향성
                    main.blocks.change_block_size(block, vector(0, 0, 0)) #블록 삭제(크기 0으로 하는 것으로 대체)
                    main.blocks.remove_block(block) #리스트에서 블록 삭제함으로써 다음번 for문에서 확인 안되도록 처리
                else:
                    try: #이미 위에서 삭제 되었을 경우 처리하기 위한 try문
                        if self._ball.pos.y <= block.pos.y + 0.71 or self._ball.pos.y >= block.pos.y - 0.71: #블록의 왼쪽면이나 오른쪽 면과 닿은 경우(이미 닿은 경우로 위에서 분류했으므로 y범위 안 인지만 확인만 하면 됨)
                            self._ball.v.x = -self._ball.v.x + uniform(-0.1, 0.1) #x방향 반대로 + 약간의 무작위 방향성
                            main.blocks.change_block_size(block, vector(0, 0, 0)) #블록 삭제(크기 0으로 하는 것으로 대체)
                            main.blocks.remove_block(block) #리스트에서 블록 삭제함으로써 다음번 for문에서 확인 안되도록 처리
                    except:
                        pass
        if len(main.blocks.blocks) == 0: #블록이 모두 없어졌을 시
            main.heart.change_text(True) #승리의 텍스트 출력(화면에) + 시간 계산됨(아래 함수 참조)
            print("You Win!") #승리의 텍스트 출력(콘솔창)
            main.end = True #게임 종료 변수 활성화


class Heart:
    """
    목숨을 관리하는 클래스(남은 목숨 개수 알려주는 글자도 관리)
    """
    def __init__(self, main):
        """
        클래스 Heart 세팅
        :param main:
        """
        self.main = main
        self._heart = 3 #기본 목숨 개수: 3
        self.make_text() #화면에 남은 목숨 개수 알려주는 글자 생성

    @property
    def heart(self):
        """
        목숨 개수 알려줌
        :return:
        """
        return self._heart
    @heart.setter
    def heart(self, amount):
        """
        목숨 개수 설정함
        :param amount:
        :return:
        """
        self._heart += amount
        self.change_text()

    def make_text(self):
        """
        화면에 남은 목숨 개수 출력해주는 함수
        :return:
        """
        self._heart_text = text(text=f"Left Hearts: {self._heart}", pos=vector(10.2, -7.5, 0), height=0.5) #글자 생성

    def change_text(self, win=False):
        """
        화면에 남은 목숨 개수 출력을 변경하거나 걸린 시간을 출력해주는 함수
        :param win: -> 이겼으면 승리의 텍스트와 걸린 시간 출력
        :return:
        """
        self._heart_text.visible = False #기존 목숨개수 텍스트 안보이게 숨기기
        self._heart_text.__del__() #기존 목숨개수 텍스트 전산상에서 삭제(실제로는 남아있으나 호출 불가)
        if win: #이겨서 호출된거라면
            text(text=f"Time: {int((time() - main.start_time)*10)/10}", pos=vector(10.2, -6.5, 0), height=0.5) #걸린 시간 계산
            text(text="You Win!", pos=vector(10.2, -7.5, 0), height=0.5) #승리의 텍스트 출력
        elif self._heart == -1: #게임오버여서 호출된거라면
            text(text="Game Over!", pos=vector(10.2, -7.5, 0), height=0.5) #게임오버 텍스트 출력
        else: #그냥 죽어서 호출된거라면
            self.make_text() #남은 목숨 개수 다시 출력


class Ball_Bar:
    """
    볼을 튕겨내는 바를 관리하는 클래스
    """
    def __init__(self, main, ai_play=False):
        """
        클래스 Ball_Bar 세팅
        :param main:
        :param ai_play: -> 자동으로 플레이 할지 결정
        """
        self.main = main
        self.AI_PLAY = ai_play #자동 플레이 관련 세팅
        self._bar_speed = 0.0008 #기본 속도
        self.make_ball_bar() #바 생성

    def make_ball_bar(self):
        """
        바를 생성하는 함수
        :return: 
        """
        self._ball_bar = box(color=color.blue, size=vector(5, 0.3, 0.1), pos=vector(0, -7.5, 0)) #바 생성
        self._ball_bar.v = vector(0, 0, 0) #이동방향 설정

    @property
    def ball_bar(self):
        """
        공 튀기는 바 자체를 반환
        :return:
        """
        return self._ball_bar #공 튀기는 바 반환

    def bar_movement(self):
        """
        바의 움직임을 관리(자동 플레이도 관리)
        :return: 
        """
        if self.AI_PLAY: #자동 플레이 할때
            if main.ball.ball.pos.x + 2.5 > main.wall.right_wall.pos.x: #오른 벽과 닿았다면(공 기준으로 관리함, 왜냐하면 바는 한번 닿으면 움직이지가 않게 되서)
                pass
            elif main.ball.ball.pos.x - 2.5 < main.wall.left_wall.pos.x: #왼 벽과 닿았다면(공 기준으로 관리함, 왜냐하면 바는 한번 닿으면 움직이지가 않게 되서)
                pass
            else: #벽에 안 닿았다면 x좌표를 공과 일치시킴
                self._ball_bar.pos.x = main.ball.ball.pos.x
        else: #자동 플레이가 아니라면
            self._ball_bar.pos.x += self._ball_bar.v.x * self._bar_speed #기본 움직임 제어
            self._keys = keysdown() #키보드 인식
            if 'left' in self._keys: #왼쪽 화살표키가 눌렸다면
                if self._ball_bar.pos.x - 2.6 <= self.main.wall.left_wall.pos.x: #왼벽에 닿아다면
                    self._ball_bar.v = vector(0, 0, 0) #안 움직이기
                else:
                    self._ball_bar.v = vector(-1, 0, 0) #왼쪽으로 방향 설정
            elif 'right' in self._keys: #오른쪽 화살표키가 눌렸다면
                if self._ball_bar.pos.x + 2.6 >= self.main.wall.right_wall.pos.x: #오른벽에 닿아다면
                    self._ball_bar.v = vector(0, 0, 0) #안 움직이기
                else:
                    self._ball_bar.v = vector(1, 0, 0) #오른쪽으로 방향 설정
            else:
                self._ball_bar.v = vector(0, 0, 0) #아무것도 안눌렸다면 안 움직이기


class Blocks:
    """
    블록들을 생성하는 클래스
    """
    def __init__(self, main):
        """
        클래스 Blocks 세팅
        :param main: 
        """
        self.main = main
        self._blocks = [] #블록들이 담겨질 리스트
        self.set_blocks() #블록 생성

    def set_blocks(self):
        """
        블록을 생성하는 함수
        :return: 
        """
        for x in range(-10, 10, 2): #블록들의 x좌표 위치(2 간격)
            for y in range(2, 6): #블록들의 y좌표 위치(1 간격)
                if y == 2: #y가 2라면(1단계) 초록색 블록 생성
                    self.blocks.append(box(size=vector(1.9, 0.9, 0.1), pos=vector(x+1, y, 0), color=color.green)) #x를 1.9, y를 0.9로 해서 약간씩 간격 벌리기
                elif y == 3: #y가 3라면(2단계) 노란색 블록 생성
                    self.blocks.append(box(size=vector(1.9, 0.9, 0.1), pos=vector(x+1, y, 0), color=color.yellow)) #x를 1.9, y를 0.9로 해서 약간씩 간격 벌리기
                elif y == 4: #y가 4라면(3단계) 주황색 블록 생성
                    self.blocks.append(box(size=vector(1.9, 0.9, 0.1), pos=vector(x+1, y, 0), color=color.orange)) #x를 1.9, y를 0.9로 해서 약간씩 간격 벌리기
                elif y == 5: #y가 5라면(4단계) 빨간색 블록 생성
                    self.blocks.append(box(size=vector(1.9, 0.9, 0.1), pos=vector(x+1, y, 0), color=color.red)) #x를 1.9, y를 0.9로 해서 약간씩 간격 벌리기

    @property
    def blocks(self):
        """
        블록 리스트 반환
        :return:
        """
        return self._blocks #블록 리스트를 반환

    def change_block_size(self, block, size):
        """
        요청하는 블록의 사이즈를 변경합니다
        :param block:
        :param size:
        :return:
        """
        block.size = size #블록의 사이즈 변경

    def remove_block(self, block):
        """
        리스트에서 블록을 제거합니다
        :param block:
        :return:
        """
        self._blocks.remove(block) #해당하는 블록을 제거


class Wall:
    """
    벽들을 생성하는 클래스
    """
    def __init__(self, main):
        """
        클래스 Wall 세팅
        :param main:
        """
        self.main = main
        self.make_wall() #벽 생성 함수 실행

    def make_wall(self):
        """
        벽 생성 함수
        :return:
        """
        self._left_wall = box(size=vector(0.1, 15, 0.1), pos=vector(-10.1, 0, 0)) #왼 벽
        self._right_wall = box(size=vector(0.1, 15, 0.1), pos=vector(10.1, 0, 0)) #오른 벽
        self._upper_wall = box(size=vector(20.2, 0.1, 0.1), pos=vector(0, 7.5, 0)) #윗 벽

    @property
    def left_wall(self):
        """
        왼 벽 자체를 반환
        :return:
        """
        return self._left_wall #왼 벽 자체를 반환

    @property
    def right_wall(self):
        """
        오른 벽 자체를 반환
        :return:
        """
        return self._right_wall #오른 벽 자체를 반환

    @property
    def upper_wall(self):
        """
        윗 벽 자체를 반환
        :return:
        """
        return self._upper_wall #윗 벽 자체를 반환


class Main:
    """
    중심 클래스
    """
    def __init__(self):
        """
        클래스 Main 세팅
        :param ai_play: -> 자동플레이 여부를 클래스 Ball_Bar에 전달하기 위한 매개변수
        """
        self._start_time = time() #시작하는 시간 기록
        self._end = False #게임이 종료됬는지 여부(이기거나 져서)
        self._monitor = canvas(width=1300, height=800) #화면 설정(사이즈도 설정)
        self.heart = Heart(self) #목숨 클래스
        self.ball_bar = Ball_Bar(self, AI_play) #바 클래스
        self.ball = Ball(self) #공 클래스
        self.blocks = Blocks(self) #블록 클래스
        self.wall = Wall(self) #벽 클래스

    def restart_game(self):
        """
        게임을 재시작 하는 함수
        :return:
        """
        self._monitor.delete() #모니터(캔버스)를 삭제
        self._monitor = canvas(width=1300, height=800) #모니터(캔버스)를 재생성
        self._end = False #게임을 다시 안 끝난 상태로 변경
        self.__init__()

    @property
    def end(self):
        """
        게임의 종료 여부를 알려주는 end변수 반환
        :return:
        """
        return self._end #end변수 반환
    @end.setter
    def end(self, bool):
        """
        게임이 종료됬는지의 여부를 알려주는 end변수 변경
        :param bool:
        :return:
        """
        self._end = bool #end 변수 설정

    @property
    def start_time(self):
        """
        시작시간을 기록해놓은 start_time 변수를 반환
        :return:
        """
        return self._start_time #start_time변수를 반환


if __name__ == "__main__": #이 파일을 직접 실행한다면
    main = Main() #클래스 Main 생성, 이름은 main으로
    while True: #무한 반복
        keys = keysdown() #키보드 인식
        if ' ' in keys: #스페이스 바가 눌렸다면
            sleep(1) #한번만 하기 위한 약간의 지연(오래 누르면 여러번 눌린거로 인식해서)
            main.restart_game()
        else: #아니면 그냥 아무것도 안함
            pass
        if main.end == False: #게임이 종료된게 아니라면
            main.ball_bar.bar_movement() #바 움직이기
            main.ball.ball_movement() #공 움직이기
        else: #게임 종료 됬으면 아무것도 안정
            pass