import pandas as pd
df = pd.read_csv('wild_boars.csv')
a = df.mean(numeric_only=True)
with open('averages.txt', 'w') as f:
    for c, a_value in a.items():
        f.write(f"{c}: {a_value:.2f}\n")
for c, a_value in a.items():
    print(f"{c}: {a_value:.2f}")