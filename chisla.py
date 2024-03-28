from random import randint
# Загадать число! - Это делает компьютер, но важно, чтобы цифры были РАЗНЫЕ!
# Можно из модуля random использовать все!

# range(STOP1) от 0 до STOP1-1
# range(START, STOP1) от START до STOP1-1
# range(START, STOP1, STEP) от START до STOP1-1

# def - define a function
def create_number(nlen):
    # генератор - выражение - СПИСОК
    alph = [i for i in range(10)]  # list of int
    # result = []
    # for i in range(10):
    #     result.append(i)
    result = ''
    for i in range(nlen):
        digit = alph.pop(randint(0, len(alph) - 1))
        # pop извлекает (удаляет и возвращает) последний элемент
        # pop(N) извлекает и удаляет элемент на позиции N
        # вернуть alph[N]
        # del alph[N]
        result += str(digit)
    return result