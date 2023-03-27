# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# Input 11 6 2 4 6 8 10 12 10 8 6 4 2
# Input 3 6 9 12 15 18
# Output 6 12


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

list1 = CreateRandomList()
list2 = CreateRandomList()
result = []

for i in list1:
  if i in list2:
    result.append(i)

result.sort()
summary = set(result)
print(f"Без повторений в порядке возрастания все числа, которые встречаются в обоих наборах")
print(summary)

