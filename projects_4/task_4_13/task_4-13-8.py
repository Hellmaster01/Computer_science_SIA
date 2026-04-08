array = [126, 66, 70, 4, 21, 99]
n = len(array)
i = 0
count = 0

while i < n:
    if array[i] > 0:
        count = count + 1
    i = i + 1

print("Количество положительных чисел в массиве:", count)