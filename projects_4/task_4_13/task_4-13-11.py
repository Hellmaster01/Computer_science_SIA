array = [126, 66, 70, 4, 21, 99]
n = len(array)
sum = 0
i = 0
count = 0
while i < n:
    sum = sum + array[i]
    count += 1
    i = i + 2
avg = sum / count
print("Среднее арифметическое элементов массива:", avg)