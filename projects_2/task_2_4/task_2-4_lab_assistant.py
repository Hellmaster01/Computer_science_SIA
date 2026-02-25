volume = float(input("Введите нужный объем раствора (в мл): "))

mass = volume * 0.009
vvolume = volume 

with open("C:/Users/Иван/OneDrive/Документы/sumenkov.ia/projects_2/task_2_4/recipe.txt", "w", encoding="utf-8") as card:
    
    card.write(f"ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n-----------------------\nОбщий объем: {volume} мл\nМасса соли:  {mass:.2f} г\nОбъем воды:  {vvolume} мл")
print(f"ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n-----------------------\nОбщий объем: {volume} мл\nМасса соли:  {mass:.2f} г\nОбъем воды:  {vvolume} мл")