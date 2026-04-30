import pandas as pd
df = pd.read_csv('wild_boars.csv')
m = df.median(numeric_only=True)
with open('medians.txt', 'w') as f:
    for c, m_value in m.items():
        f.write(f"{c}: {m_value:.2f}\n")
for c, m_value in m.items():
    print(f"{c}: {m_value:.2f}")