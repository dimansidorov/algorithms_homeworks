"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


# O(n log n)
def top3_1(dct):
    result = sorted(dct, key=dct.get, reverse=True)     # O(n log n)
    return f'Наибольшая годовая прибыль у компаний: {result[0]}, {result[1]}, {result[2]}.'     # O(1)


# O(n)
def top3_2(dct):
    first = ['', 0]     # O(1)
    second = ['', 0]    # O(1)
    third = ['', 0]     # O(1)
    d_items = list(dct.items())     # O(n)
    for item in d_items:    # O(n)
        if item[1] > first[1]:  # O(1)
            third = [i for i in second]     # O(1)
            second = [j for j in first]     # O(1)
            first = [k for k in item]       # O(1)
        elif item[1] > second[1]:   # O(1)
            third = [i for i in second]     # O(1)
            second = [k for k in item]      # O(1)
        elif item[1] > third[1]:    # O(1)
            third = [k for k in item]
    return f'Наибольшая годовая прибыль у компаний: {first[0]}, {second[0]}, {third[0]}.'   # O(1)


companies = {'Industrial and Commercial Bank of China': 45.8,
             'Apple inc.': 63.9,
             'Amazon inc.': 21.3,
             'Saudi Aramco': 49.3,
             'JPMorgan Chase': 40.3,
             'Berkshire Hathaway': 42.5,
             'China Construction Bank': 39.3,
             'Bank of America': 17.9,
             'Ping An Insurance': 20.8,
             'Agricultural Bank of China': 31.3,
             'Булочки от тёти Глаши': 0.0001}


print(top3_1(companies))
print(top3_2(companies))