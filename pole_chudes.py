#Создать отдельно от игры поле чудес в отдельном файле
#словарь для игры с ключами и значениями (определениями).
#Импортировать этот словарь в свою игру
#Это не поле чудес,конечно,сделал что успел 
import random
from slovar_for_pole_chudes import slovo
key,value=random.choice(list(slovo.items()))
print(key) #выводим на экран ключ
otvet=input("Ваш ответ")
while otvet!= value:
   print('неа')
   otvet=input("Ваш ответ")
print('Браво!')
d=input('хотите сыграть еще?')
while d!="нет":
   while otvet!= value:                #не работает проверка если ответ!=значению
         print('неа')
         otvet=input("Ваш ответ")
         print('Браво!')
   if d!='нет':
    key,value=random.choice(list(slovo.items()))
    print(key) #выводим на экран ключ
    otvet=input("Ваш ответ")
    d=input('хотите сыграть еще?')
print('До скорого')



