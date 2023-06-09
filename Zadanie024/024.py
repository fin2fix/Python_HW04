# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

# Функция создания и печати рандомного списка чисел
def CreateRandomList():
    from random import randint
    list = []
    listLength = int(input("Введите размер массива (кол-во элементов)  "))

    for i in range(listLength):
        list.append(randint(1, 6))
    print()
    print(list)
    print()
    return list


garden = CreateRandomList()
result = []

for i in range(-1, len(garden) - 1):
    result.append(garden[i-1] + garden[i] + garden[i+1])
print("Маскимальное число ягод с трех соседних кустов = ", end="")
print(max(result))

# Второй вариант
print()
print("Второй вариант решения:")

max = 0
for i in range(-1, len(garden) - 1):
    if (garden[i-1] + garden[i] + garden[i+1]) > max:
        max = (garden[i-1] + garden[i] + garden[i+1])
print("Маскимальное число ягод с трех соседних кустов = ", end="")
print(max)