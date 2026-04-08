n = int(input("Введите N: "))
sum = 0
i = 1
while i <= n:
    sum = sum + i * i  
    i = i + 1   
print("Сумма квадратов первых", n, "натуральных чисел равна", sum)