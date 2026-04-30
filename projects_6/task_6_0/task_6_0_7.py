import pandas as pd
df = pd.read_csv('wild_boars.csv')
df_f = df.iloc[:, 2:] 
with open('v_sd_cv.txt', 'w') as f:
    for c in df_f.columns:
        variance = df_f[c].var()
        std_dev = df_f[c].std()
        mean = df_f[c].mean()
        if mean != 0:
            cv = (std_dev / mean) * 100  
        else:
            cv = 0
        f.write(f"{c}:\n")
        f.write(f"  Variance: {variance:.2f}\n")
        f.write(f"  Standard Deviation: {std_dev:.2f}\n")
        f.write(f"  Coefficient of Variation: {cv:.2f}%\n")
        f.write("\n")
        print(f"{c}:")
        print(f"  Variance: {variance:.2f}")
        print(f"  Standard Deviation: {std_dev:.2f}")
        print(f"  Coefficient of Variation: {cv:.2f}%")
        print()