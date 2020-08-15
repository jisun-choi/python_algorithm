from random import *

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f'{name} 유닛 생성')
    
    def move(self, location):
        print(f'{self.name} : {location} 방향으로 이동 [속도 {self.speed}]')

    def damaged(self, damage):
        print(f'{self.name} : {damage} 데미지를 입음')
        self.hp -= damage
        print(f'{self.name}  : 현재 체력 {self.hp}')
        if self.hp <= 0:
            print(f'{self.name} 파괴됨')

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        super().__init__(name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print(f'{self.name} : {location} 방향으로 적군 공격 [공격력 {self.damage}]')
    
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, '마린', 40, 1, 5)
    
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print(f'{self.name} : 스팀팩 사용 (HP 10 감소)')
        else:
            print(f'{self.name} : 체력 부족, 스팀팩 사용 x')

class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, '탱크', 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        if self.seize_mode == False:
            print(f'{self.name} : 시즈모드 전환')
            self.damage *= 2
            self.seize_mode = True
        else: 
            print(f'{self.name} : 시즈모드 해제')  
            self.damage /= 2
            self.seize_mode = False


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print(f'{name} : {location} 방향으로 날아감 [속도 {self.flying_speed}]')

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, '레이스', 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print(f'{self.name} : 클로킹 모드 해제')
            self.clocked = False
        else:
            print(f'{self.name} : 클로킹 모드 설정')
            self.clocked = True

def game_start():
    print('[알림] 새로운 게임을 시작합니다.')

def game_over():
    print('[player] 님이 게임에서 퇴장')

#게임 시작
game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

#유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

#전군 이동 
for unit in attack_units:
    unit.move('1시')

#탱크 시즈모드 개발 
Tank.seize_developed == True
print('[알림] 탱크 시즈모드 개발 완료')

#공격 모드 준비
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

#전군 공격
for unit in attack_units:
    unit.attack('1시')

#전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21))

#게임 종료
game_over()
