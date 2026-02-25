protein = float(input("Введите массу белков в продукте (г): "))
fats = float(input("Введите массу жиров в продукте (г): "))
carb = float(input("Введите массу углеводов в продукте (г): "))

cal = protein * 4 + fats * 9 + carb * 4
print(f"Общая калорийность: {cal}")