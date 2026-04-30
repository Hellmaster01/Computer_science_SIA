import pandas as pd
df = pd.read_csv('wild_boars.csv')
males = df[df['gender'] == 'Male']
females = df[df['gender'] == 'Female']
q1_males = males['length_cm'].quantile(0.25)
q3_males = males['length_cm'].quantile(0.75)
iqr_males = q3_males - q1_males
q1_females = females['length_cm'].quantile(0.25)
q3_females = females['length_cm'].quantile(0.75)
iqr_females = q3_females - q1_females
print(f"Male: IQR = {iqr_males:.1f} cm")
print(f"Female: IQR = {iqr_females:.1f} cm")
with open('iqr_length.txt', 'w') as f:
    f.write(f"Male: IQR = {iqr_males:.1f} cm\n")
    f.write(f"Female: IQR = {iqr_females:.1f} cm\n")
