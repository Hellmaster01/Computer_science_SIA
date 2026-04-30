import pandas as pd
df = pd.read_csv('wild_boars.csv')
df_f = df.iloc[:, 1:] 
m = df_f.mode()
with open('modes.txt', 'w') as f:
    for c in df_f.columns:
        m_value = m[c].dropna().tolist()
        f.write(f"{c}: {m_value}\n")
for c in df_f.columns:
    m_value = m[c].dropna().tolist()
    print(f"{c}: {m_value}")