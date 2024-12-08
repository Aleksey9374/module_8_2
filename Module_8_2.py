def  personal_sum(numbers):
    result = 0
    correct_data = 0
    for i in numbers:
        try:
            result += i
            correct_data += 1
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    return [result, correct_data]

def calculate_average(numbers):
    try:
        sum_ = personal_sum(numbers)
        arithmetic_mean = sum_[0] / sum_[1]
        return arithmetic_mean
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')

print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать