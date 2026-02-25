dphenotype = input("Введите фенотип группы крови донора (I, II, III, IV): ").strip().upper()
rphenotype = input("Введите фенотип группы крови реципиента (I, II, III, IV): ").strip().upper()
if dphenotype == "I":
    print("Переливание донорской крови возможно любому пациенту")
elif dphenotype == "II" and rphenotype == "II" or dphenotype == "III" and rphenotype == "III" or dphenotype == "IV" and rphenotype == "IV":
    print("Переливание донорской крови возможно")
else:
    print("Переливание донорской крови невозможно")