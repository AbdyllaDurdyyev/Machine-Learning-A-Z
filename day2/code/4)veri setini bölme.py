import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Seed değeri ayarlayalım
np.random.seed(0)

# Yaklaşık 30 kişilik rastgele boy ve kilo verileri oluşturalım
boy = np.random.normal(170, 10, 30)  # Ortalama 170 cm, standart sapma 10 cm
kilo = np.random.normal(70, 15, 30)  # Ortalama 70 kg, standart sapma 15 kg

# Pandas DataFrame oluşturalım
data = pd.DataFrame({'Boy': boy, 'Kilo': kilo})

# Veriyi görelim
print("Oluşturulan Veri Seti:\n", data.head())

# Veriyi bağımsız (X) ve bağımlı (y) değişkenlere ayıralım
X = data[['Boy']]  # Bağımsız değişken
y = data['Kilo']   # Bağımlı değişken

# Veriyi eğitim ve test setlerine ayıralım
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Eğitim ve test setlerinin boyutlarını yazdıralım
print("\nEğitim Seti Boyutu:", X_train.shape)
print("Test Seti Boyutu:", X_test.shape)
