def price(people):
    print(f'{people} 명 가격은 {people*10000}입니다.')

def price_morning(people):
    print(f'{people} 명 조조할인 가격은 {people*6000}입니다.')

def price_soldier(people):
    print(f'{people} 명 군인할인 가격은 {people*5000}입니다.')


#모듈 실행 
import theater_module

theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_soldier(2)

import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(2)

from theater_module import *
price(3)
price_morning(4)
price_soldier(2)