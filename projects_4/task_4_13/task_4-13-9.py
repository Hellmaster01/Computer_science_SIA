array = [126, 66, 70, 4, 21, 99]
n = len(array)
i = 0
sum = 0

while i < n:
    if array[i] % 2 != 0:
        sum = sum + array[i]
    i = i + 1

print("Сумма нечётных чисел в массиве:", sum)