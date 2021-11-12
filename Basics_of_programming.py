# Дан массив целых чисел nums и целое число target. Написать функцию, возвращающую индексы элементов, дающих в сумме число target?
# Предполагается, что в каждом массиве имеется не больше одной пары дающих в сумме заданное число target. Нельзя использовать один и тот же элемент дважды?

# Если предположить, что вопросительные знаки нужно заменить на точки, то простейшее решение будет выглядеть следующим образом.

target = int(input('Введите target: '))
arr_str =  input("Введите массив числел nums через пробел: ").split(' ')
arr = [int(i) for i in arr_str]

indexes = []
for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            indexes.append(i)
            indexes.append(j)
            break
if len(indexes) == 0:
    print("Не найдено нужной пары элементов")
else:    
    print(f"array[{indexes[0]}] ({arr[indexes[0]]}) + array[{indexes[1]}] ({arr[indexes[1]]}) = {target} ")
