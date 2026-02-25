weight = float(input("Введите вес (кг): "))
height = float(input("Введите рост (м): "))

bmi = weight / ((height/100) ** 2)
print(f"\n--- Отчет о состоянии здоровья ---\nРост:\t{height} см\nВес:\t{weight} кг")
print(f"Индекс массы тела: {bmi:.2f}")