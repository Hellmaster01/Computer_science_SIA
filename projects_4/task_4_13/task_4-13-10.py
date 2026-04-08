array = [126, 66, 70, 4, 21, 99]
n = len(array)
i = 1
sum = 0

while i < n:
    sum = sum + array[i]
    i = i + 2

print("Сумма чисел с нечётным индексом в массиве:", sum)