name = input("Введите имя оператора: ")
value = input("Введите текущее значение давления (Па): ")

with open("C:/Users/Иван/OneDrive/Документы/sumenkov.ia/projects_2/task_2_3/sensor_log.txt", "a", encoding="utf-8") as card:
    
    card.write(f"{name}\t| Давление: {value}\n")
print("Данные успешно сохранены в sensor_log.txt")