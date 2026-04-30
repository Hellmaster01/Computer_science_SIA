import pandas as pd

df = pd.read_csv('wild_boars.csv')
columns_config = [
    ('age_years', 'Age', 'years'),
    ('weight_kg', 'Weight', 'kg'),
    ('length_cm', 'Length', 'cm'),
    ('shoulder_height_cm', 'Shoulder Height', 'cm'),
    ('tusk_length_cm', 'Tusk Length', 'cm'),
    ('litter_size', 'Litter Size', ''),
    ('health_score', 'Health Score', ''),
    ('territory_ha', 'Territory', 'ha')
]
percentiles_config = [
    (0.25, "Percentile 25 (Q1)"),
    (0.50, "Median 50 (Q2)"),
    (0.75, "Percentile 75 (Q3)"),
    (0.90, "Percentile 90"),
    (0.95, "Percentile 95"),
    (1.00, "Max")
]
with open('percentiles.txt', 'w') as f:
    for col_name, display_name, unit in columns_config:
        header = f"{display_name}:\n"
        f.write(header)
        print(header.strip())
        for q_val, q_label in percentiles_config:
            value = df[col_name].quantile(q_val)
            if unit:
                unit_str = f" {unit}"
            else:
                unit_str = ""
            line = f"{q_label}:\t{value:.1f}{unit_str}\n"
            f.write(line)
            print(line.strip())
        f.write("\n")
        print()
