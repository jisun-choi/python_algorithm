# 한 클래스에 두 개의 객체(공격,방어)를 만들어 '캐릭터 싸움'을 구현해주세요.
# 나와 상대방(적)의 이름 및 직업을 생성 & 초기 hp 값은 100 & 공격 시, hp에서 -10 / 방어 시, hp에서 -5
# ==========print 내용=====================
# 내 이름.공격(적 이름)  #메소드 호출
# 상대 (직업) 에게 10 피해를 입혔습니다.
# 내 이름.방어()  #메소드 호출
# (내 직업) 은 5 피해를 입었습니다.

class Fight:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.hp = 100

    def attack(self, enemy):
        self.hp -= 10
        print(f'상대 {enemy.role}에게 10 피해를 입혔습니다.')
        print(f'{self.name} remaining hp: {self.hp}')

    def defend(self):
        self.hp -= 5
        print(f'{self.name}은 5 피해를 입었습니다.')
        print(f'{self.name} remaining hp: {self.hp}')

  
    def __str__(self):
        return'{}\t{}\t{}'.format(self.name, self.role, self.hp)


Jisun = Fight('지선','마법사')
Suyoung = Fight('수영','농부')


print(Jisun.attack(Suyoung))
print(Jisun.defend())
