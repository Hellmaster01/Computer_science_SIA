array = [126, 66, 70, 4, 21, 99]
n = len(array)
sum = 0
i = 0
while i < n:
    sum = sum + array[i]
    i = i + 1
avg = sum / n
print("Среднее арифметическое элементов массива:", avg)