#это  мы писали игру быки и коровы
#так как поле чудес я не делал 
# я сделал импорт одной из функций 
from chisla import create_number # чтобы импортировать функцию из модуля нужно  написать так,типа из модуля импортируем такую то функцию

def main():
    NLEN = 4
    chislo = create_number(NLEN)  # digital string
    print('Мы чииииитеры! Правильный ответ: ', chislo)
    popitka = 0
    while chislo != popitka:
        popitka = input('введите %i-значное число' % NLEN)
        if len(popitka) == 4:
            print(bulls_cows(chislo, popitka))
        else:
            print('Учись cчитать до четырёх!!!')
    #цикл пока загаданное_число != число_пользователя
    #while ........:
    # Спрашивает: #  if ..... список, по индексу.... советую написать функцию, возвращающую быков и коров
    #  
#              '5439'   '6530'
def bulls_cows(answer, user_try):
    bulls = 0
    cows  = 0
    for nomer_elementa in range(len(answer)):  # Мы предполагаем, что в ответе и попытке одинаковое количество цифр
        print('index: ', nomer_elementa,
              'right: ', answer[nomer_elementa],
              'try:', user_try[nomer_elementa])
        if answer[nomer_elementa] == user_try[nomer_elementa]:
            print('Пользователь молодец! ')
            bulls += 1  # мы нашли быка! по номеру элемента совпали цифра ответа и цифра попытки!
        elif user_try[nomer_elementa] in answer:  # есть цифра, но не там
            cows += 1
    return bulls, cows  # 2 быка и 3 коровы. В 4хзначном числе ))))))

if __name__ == "__main__":
    main()
