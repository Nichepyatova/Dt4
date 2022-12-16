# # 4 1-балл
# Dollar
# Создайте функцию dollarize (), которая принимает Float и возвращает долларовый формат:
#
# Copy
# dollarize(123456.78901) -> "$123,456.80"
# dollarize(-123456.7801) -> "-$123,456.78"
# dollarize(1000000) -> "$1,000,000"
#
# Преобразуйте эту функцию в полезный класс MoneyFmt. MoneyFmt содержит одно значение данных (количество) и 4 метода.
# Copy
#     "init" //конструктор инициализирует значение данных
#     "update" //метод заменяет значение данных новым
#     "repr" //методы возвращают значение с плавающей запятой
#     "str" //метод, реализующий логику метода dollarize ()
#
# Copy
# //Результат будет выглядеть так:
# import moneyfmt
# cash = moneyfmt.MoneyFmt(12345678.021)
# print(cash) -- returns "$12,345,678.02"
# cash.update(100000.4567)
# print(cash) -- returns "$100,000.46"
# cash.update(-0.3)
# print(cash) -- returns "-$0.30"
# repr(cash) -- returns -0.3

#import moneyfmt
# def dollarize(d: float):
#     return f'{format(d, ",.2f")}'
#
# class MoneyMft:
#     def __init__(self, d):
#         self.d = d
#
#     def update(self, new_el):
#         return new_el
#
#     def repr(self):
#         return self.d
#
#     def str(self):
#         return f'{format(self.d, ",.2f")}'
#
#
# print(dollarize(5688888888))
# m = MoneyMft((5688888888.89))
# print(m.str())
#

########################################################################################################################


# 1 1-балл
# AK-47:
# У солдата Райана есть АК-47
# Солдаты могут стрелять («тиги-тигитиш»).
# Пистолеты могут стрелять пулями.
# Пистолеты могут начинать патроны - увеличивайте количество патронов (перезаряжает)
# Создайте класс Act_of_Shooting, который унаследует от класса Soldier класс Guns.
#
# Где солдат будет стрелять из пушки и перезаряжаться, и стрелять еще раз.
#
#
# class Guns:
#     def __init__(self, pul):
#         self.pul = pul
#
#     def shootGun(self):
#         return 'пуля пиу-пиу'
#
#     def count_pul(self):
#         return self.pul + 1
#
#
# class Soldier(Guns):
#     def __init__(self, shoot, pul):
#         super().__init__(pul)
#         self.shoot = shoot
#
#     def shootGunSoldier(self):
#         return 'стреляю из gun тиги-тигидищ'
#
#
#
# class Act_of_Shooting(Soldier):
#     def __init__(self, shoot, pul, y):
#         super().__init__(shoot, pul)
#         self.y = y
#
#
# gun = Guns(56)
# sold = Soldier(shoot='пиу-пиу', pul=gun.pul)
# print(sold.pul)
# print(sold.shootGun())
#
# print(sold.count_pul())
# print(sold.shootGun())

#
# Furniture:
# Тип дома, общая площадь и перечень наименований мебели В новом доме совсем нет мебели.
# Мебель имеет название и площадь, из которых Спальня: 4 квадратных метра Гардероб: 2 квадратных метра Стол: 1,5 квадратных метра.
# Добавьте в дом три вышеупомянутых предмета мебели.
# При печати дома требуются следующие данные: тип дома, общая площадь, оставшаяся площадь, список названий мебели.

# class House:
#     def __init__(self, ploshad):
#         self.ploshad = ploshad
#
#     def add_mebel(self, meb):
#         return f'эм {meb}'
#
#

# class Furniture(House):
#     def __init__(self,name, ploshadMebeli, ploshad):
#         super().__init__(ploshad)
#         self.name = name
#         self.ploshadMebeli = ploshadMebeli
#
#
# house = House(34)
# pl = Furniture('спальня', 23, house.ploshad)
# garderob = Furniture('гардероб', 27, house.ploshad )
# stol = Furniture('стол', 93, house.ploshad )
#
#
# house.add_mebel(pl)
# house.add_mebel(garderob)
# house.add_mebel(stol)
#
# print(pl.__dict__)
# print(garderob.__dict__)
# print(stol.__dict__)

from bs4 import BeautifulSoup
import requests

url = 'https://lalafo.kg/kyrgyzstan/nedvizhimost'
req = requests.get(url).content
soup = BeautifulSoup(req, 'html.parser')
div = soup.find_all('div', class_='AdTileHorizontal')

for i in div:
    a = i.find('div').find('a')
    print(a)
