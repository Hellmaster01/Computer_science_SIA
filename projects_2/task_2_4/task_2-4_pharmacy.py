count = int(input("Введите общее количество произведенных капсул: "))
capacity = int(input("Введите количество капсул в одной упаковке: "))

full = count // capacity
left = count % capacity 
print("--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:	{full}")
print(f"Остаток капсул:		{left}")