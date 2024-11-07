# Задача 3.Сортировка
# Дан список из N чисел. Напишите программу, которая сортирует элементы списка по возрастанию и выводит их на экран. Дополнительный список использовать нельзя.
# Также нельзя использовать готовые функции sorted/min/max и метод sort. Постарайтесь придумать и написать как можно более эффективный алгоритм сортировки.
# Пример:
# Изначальный список: [1,4,–3,0,10]
# Отсортированный список: [–3,0,1,4,10]

n = [1, 4, -3, 0, 10,]
print("Изначальный список:",*n)

for element in range(len(n) - 1): #Проход по всем элементам списка 
    for elements in range(len(n) - 1 - element): #
        if n[elements] > n[element + 1]: #
            n[elements], n[elements + 1] = n[elements + 1], n[elements] #

print(*n)

