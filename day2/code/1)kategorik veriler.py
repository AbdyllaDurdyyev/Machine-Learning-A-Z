from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Daha büyük bir kategorik veri seti örnekleri
categories = ['kırmızı', 'mavi', 'yeşil', 'mavi', 'yeşil', 'mavi', 'kırmızı', 'mavi', 'kırmızı', 'kırmızı', 'yeşil', 'yeşil']
data=pd.DataFrame(categories,columns=["renkler"])
label_encoder=LabelEncoder()

data["encoded"]=label_encoder.fit_transform(data["renkler"])
#%%
from sklearn.preprocessing import OneHotEncoder

categories = ['kırmızı', 'mavi', 'yeşil', 'mavi', 'yeşil', 'mavi', 'kırmızı', 'mavi', 'kırmızı', 'kırmızı', 'yeşil', 'yeşil']
data1=pd.DataFrame(categories,columns=["renkler"])

ohe=OneHotEncoder(sparse=False)

#data1=ohe.fit_transform(data1[["renkler"]])


# OneHotEncoder'ı uygulama
encoded_data = ohe.fit_transform(data1[["renkler"]])

# OneHotEncoder'dan sütun isimlerini almak
column_names = ohe.get_feature_names_out(input_features=["renkler"])

# Dönüştürülen verileri bir DataFrame'e dönüştürme ve sütun isimlerini ayarlama
encoded_df = pd.DataFrame(encoded_data, columns=column_names)


print(data1)

#%%
import pandas as pd

# Kategorik verileri içeren DataFrame oluşturma
df = pd.DataFrame({'renk': ['kırmızı', 'mavi', 'yeşil', 'mavi', 'yeşil', 'mavi', 'kırmızı', 'mavi', 'kırmızı', 'kırmızı', 'yeşil', 'yeşil']})

one_hot_encoded_df = pd.get_dummies(df, columns=['renk'])

print(one_hot_encoded_df)