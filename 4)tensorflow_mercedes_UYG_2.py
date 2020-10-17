#Bismillahirrahmanirrahim
#MERCEDES VERI ANALIZI TENSORFLOW

import pandas            as pd
import numpy             as np
import matplotlib.pyplot as plt
import seaborn           as sbn
from   sklearn.model_selection  import train_test_split
from   sklearn.preprocessing    import MinMaxScaler
from   tensorflow.keras.models  import Sequential #Modeli olusturuyoruz.
from   tensorflow.keras.layers  import Dense      #Katmanlari olusturuyoruz.
from   sklearn.metrics          import mean_absolute_error,mean_squared_error


#mpg ->1 milde ne kadar yaktigi
dataFrameMerc = pd.read_excel("merc.xlsx")

dataFrameMerc.describe()
dataFrameMerc.isnull().sum()##Hangi kolonda kac eksik var bunu gormek icin burada yok ama.

"""Fiyata gore grafik cizimi."""
#plt.figure(figsize=(10,8))
#sbn.distplot(dataFrameMerc["price"])

"""Hangi yilda kac araba var COUNT """
#plt.figure(figsize=(30,10))
#sbn.countplot(dataFrameMerc["year"])

dataFrameMerc.corr() #Verilerin birbirine gore iliskisi

dataFrameMerc.corr()["price"].sort_values() #price sutununu siraya gore diz.

"""Mil ve Fiyat arasindaki iliski SEABORN SCATTERPLOT"""
#sbn.scatterplot(x="mileage",y="price",data=dataFrameMerc)

"""VERIDEKI EN YUKSEK FIYATLI ARACLARIN TESPITI"""
dataFrameMerc.sort_values("price",ascending=False).head(74)#Bu sekilde fiyati yuksek olanlari bulup cikaracagiz.

len(dataFrameMerc) #Veri sayisi
len(dataFrameMerc)* 0.01 # Verinin %99 u kalsin %1 ini yani 131 tanesini (EN YUKSEK 131) cikaralim.

"""VERI TEMIZLIGI"""

dataFrameMerc_YUZDE_99 = dataFrameMerc.sort_values("price",ascending=False).iloc[131:]
dataFrameMerc_YUZDE_99.describe()
#Yeni DF grafik incelemesi
#plt.figure(figsize=(7,5))
#sbn.distplot(dataFrameMerc_YUZDE_99["price"])

#YILLARA GORE FIYAT DAGILIMI
dataFrameMerc.groupby("year").mean()["price"] #Yillara gore fiyatlarin ortalama dagilimi
dataFrameMerc_YUZDE_99.groupby("year").mean()["price"]#Yeni df'de yillara gore fiyat dagilimi

#1970'LER ıcın fiyatlar cok pahali. Normalde fiyat yil ile dogru orantili ama 1970 deki veriler
# veriyi bozuyor bunlari da cikarsak daha guzel mantikli bir sonuc elde edebiliriz.

#1970'leri cikaralim.
dataFrameMerc[dataFrameMerc.year != 1970].groupby("year").mean()["price"]

dataFrameMerc = dataFrameMerc_YUZDE_99
dataFrameMerc = dataFrameMerc[dataFrameMerc.year != 1970]

#Transmission numeric deger olmadigi icin onu da veriden ATALIM
dataFrameMerc = dataFrameMerc.drop("transmission",axis=1)

"""MODEL OLUSTURALIM"""

y = dataFrameMerc["price"].values
x = dataFrameMerc.drop("price",axis = 1).values# x = price haric her sey

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size= 0.3,random_state = 10)

# %30 olarak bolduk. VERILERIN %30'U TEST GERI KALANI TRAIN OLARAK BOLUNUR.
len(x_train)
len(x_test)

scaler = MinMaxScaler()

x_train = scaler.fit_transform(x_train) #TEK SEFERDE SCALE ETTIK.
x_test = scaler.fit_transform(x_test)

"""FIYATI SCALE ETMEMIZE GEREK YOK YANI y TEST VE TRAIN'i"""

model = Sequential()

model.add(Dense(12,activation="relu")) #En az 5 yazmaliyiz lakin 5 yetersiz kalmis 12 yazdik.NEURON SAYISI
model.add(Dense(12,activation="relu")) #En az 5 yazmaliyiz lakin 5 yetersiz kalmis 12 yazdik.
model.add(Dense(12,activation="relu")) #En az 5 yazmaliyiz lakin 5 yetersiz kalmis 12 yazdik.
model.add(Dense(12,activation="relu")) #En az 5 yazmaliyiz lakin 5 yetersiz kalmis 12 yazdik.
#4 katman

model.add(Dense(1)) #Cikis katmani

model.compile(optimizer="adam",loss="mse")#optimizer adam rmsprop'tan iyi.


model.fit(x=x_train,y=y_train, validation_data=(x_test,y_test),batch_size=250 ,epochs=300)

kayipVerisi = pd.DataFrame(model.history.history)


kayipVerisi.head()
#kayipVerisi.plot()

tahminDizisi = model.predict(x_test)
tahminDizisi

mean_absolute_error(y_test,tahminDizisi) #Tahmin ve gercek arasindaki fark

"""
plt.scatter(y_test,tahminDizisi)
plt.plot(y_test,y_test,"g-*")
"""     

""" Bir verinin price'ini dataFrameden cikarip kendimiz tahmin etmeye calisalim. """
#2. verinin price'ini cikardik.
dataFrameMerc.iloc[2]
YeniMercSeries = dataFrameMerc.drop("price",axis=1).iloc[2]


YeniMercSeries = scaler.transform(YeniMercSeries.values.reshape(-1,5))
model.predict(YeniMercSeries)



















