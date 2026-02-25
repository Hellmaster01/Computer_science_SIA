name = input("Введите название питательной среды: ")
con = input("Введите концентрацию агара (%): ")
tem = input("Введите температуру стерилизации (°C): ")

with open("C:/Users/Иван/OneDrive/Документы/sumenkov.ia/projects_2/task_2_3/recipe.txt", "w", encoding="utf-8") as card:
    
    card.write(f"{name}\n{con}%\t{tem}°C\n")
print("Файл 'recipe.txt' успешно сформирован!")