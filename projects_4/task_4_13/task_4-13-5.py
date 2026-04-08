n = int(input("Введите количество чисел N: "))
nom1 = float(input("Введите 1 число: "))
max_n = nom1
i = 2
while i <= n:
    a = float(input(f"Введите {i} число:"))
    if a > max_n:
        max_n = a
    i = i + 1
print("Максимальное из введённых чисел:", max_n)