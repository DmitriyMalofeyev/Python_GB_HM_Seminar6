# Snimok_ekrana_30.png
# Пам-парам


def rifma(poems):
    # Количество слогов в первом слове
    num=int()

    for i in poems:
        # Счётчик гласных во всех остальных словах
        count=0
        # Считаем количество гласных во фразе
        count=len([j for j in i if j in ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']])
        # Записываем количество гласных в первом слове
        if not num: num=count

        if num!=count:
            print('Пам парам')
            break
        # Если дошли до последнего слова, то всё норм - рифма есть
        if i == poems[-1]: print('Парам-пам-пам')    

slog=(input('Введите фразу ->')).split(' ')
rifma(slog)