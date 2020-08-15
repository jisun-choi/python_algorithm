class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp 

class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp)
        self.damage = damage
    
    def attack(self, location):
        print(f'{self.name} : {location} 방향으로 적군 공격 [공격력 {self.damage}]')
    
    def damaged(self, damage):
        print(f'{self.name} : {damage} 데미지를 입음')
        self.hp -= damage
        print(f'{self.name}  : 현재 체력 {self.hp}')
        if self.hp <= 0:
            print(f'{self.name} 파괴됨')

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print(f'{name} : {location} 방향으로 날아감 [속도 {self.flying_speed}]')

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# firebat1 = AttackUnit('파이어뱃', 50, 16)
# firebat1.attack('5시')
# firebat1.damaged(25)
# firebat1.damaged(25)

valkyrie = FlyableAttackUnit('발키리', 200, 6, 5)
valkyrie.fly(valkyrie.name, '3시')

