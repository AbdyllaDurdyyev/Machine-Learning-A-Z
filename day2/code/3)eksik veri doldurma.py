import pandas as pd
import numpy as np

# Örnek veri seti oluşturalım
data = {'A': [1, 2, np.nan, 4, 5],
        'B': [5, np.nan, np.nan, 8, 10],
        'C': [10, 20, 30, 40, 50]}

df = pd.DataFrame(data)

# Veri setindeki eksik değerlere bakalım
print("Orijinal Veri Seti:\n", df)

# A ve B sütunlarındaki eksik değerleri ortalama ile dolduralım
df['A'].fillna(df['A'].mean(), inplace=True)
df['B'].fillna(df['B'].mean(), inplace=True)

# İmpute edilmiş veri setini görelim
print("\nİmpute Edilmiş Veri Seti:\n", df)
#%% median ile doldurma
df['A'].fillna(df['A'].median(), inplace=True)
#%% mod
df['A'].fillna(df['A'].mode()[0], inplace=True)
#%% önceki sonrkai değerler

# Önceki değerle doldurma
df['A'].fillna(method='ffill', inplace=True)

# Sonraki değerle doldurma
df['A'].fillna(method='bfill', inplace=True)
