"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """   
    
    count = 0 # инициируем переменную для получения числа попыток
    low = 1  # Нижняя граница диапазона поиска числа
    high = 101  # Верхняя граница диапазона поиска числа
    
    while True:
        count += 1
        predict = (low + high) // 2  # Предполагаемое число - середина текущего диапазона
        if predict == number:
            break  # Угадали число, выходим из цикла
        elif predict < number:
            low = predict + 1  # Если предполагаемое число меньше загаданного, сдвигаем нижнюю границу
        else:
            high = predict - 1  # Если предполагаемое число больше загаданного, сдвигаем верхнюю границу
    
    return count

def score_game(game_core_v3) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict_1 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))    
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")   
    return score

if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)
