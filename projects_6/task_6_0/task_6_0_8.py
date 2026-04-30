import pandas as pd
df = pd.read_csv('wild_boars.csv')
males = df[df['gender'] == 'Male']
females = df[df['gender'] == 'Female']
males_std = males['tusk_length_cm'].std()
males_mean = males['tusk_length_cm'].mean()
males_cv = (males_std / males_mean) * 100
females_std = females['tusk_length_cm'].std()
females_mean = females['tusk_length_cm'].mean()
females_cv = (females_std / females_mean) * 100
print(f"Male CV: {males_cv:.2f}%")
print(f"Female CV: {females_cv:.2f}%")
with open('tusk_cv.txt', 'w') as f:
    f.write(f"Male CV: {males_cv:.2f}%\n")
    f.write(f"Female CV: {females_cv:.2f}%\n")