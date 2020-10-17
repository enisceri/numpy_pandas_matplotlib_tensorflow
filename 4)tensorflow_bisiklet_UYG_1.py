#Bismillahirrahmanirrahim
import pandas            as pd
import seaborn           as sbn
import matplotlib.pyplot as plt
import tensorflow        as tf
from   tensorflow.keras.models import Sequential#Modeli bu siniftan olusturuyoruz.
from   tensorflow.keras.layers import Dense#Model icerisinde katmanlarla calismak icin.
from   sklearn.model_selection import train_test_split #TEST VE TRAIN ICIN AYIRMAK
from   sklearn.preprocessing   import MinMaxScaler #SCALE icin.
from   sklearn.metrics         import mean_absolute_error,mean_squared_error
from   tensorflow.keras.models import load_model
#Veriyi dataFrame'e aktarmak.
bisiklet_df = pd.read_excel("C:\\Users\\Admin\\Desktop\\YAPAY_ZEKA\\bisiklet_fiyatlari.xlsx")

#Verinin genel ozelliklerini yorumlamak adina genel grafigine SEABORN kutuphanesi ile bakabiliriz.
#sbn.pairplot(bisiklet_df)

"""
VERIYI TEST/TRAIN OLARAK IKIYE AYIRMAK

"""

# y = wx + b, w = 

"""
y -> fiyat   (label)
x -> ozellik (feature)

"""



y = bisiklet_df["Fiyat"].values #np dizisi (array)

x = bisiklet_df[["BisikletOzellik1","BisikletOzellik2"]].values #np array

#random_state cok onemli degil
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.33,random_state = 15)

x_train_sayi = x_train .shape
x_test_sayi  = x_test  .shape
y_train_sayi = y_train .shape
y_test_sayi  = y_test  .shape

# train_test_split ile TEST ve TRAIN olarak veriyi ikiye bolduk.

"""     SCALING
Burada verileri fit edip scaler sayesinde verileri 0 - 1 arasina uyarliyoruz.
"""

scaler = MinMaxScaler()
#scaler = MinMaxScaler(feature_range=(5,10)) ->Bu sekilde 5-10 arasina fit edebilirim.

scaler.fit(x_train)


#Trainler 0-1 araligina set edilir.
x_train = scaler.transform(x_train)
x_test  = scaler.transform(x_test)


""" MODEL VE KATMANLAR """
model = Sequential() #model olusturuldu.

#katmanlar
#Kac tane HIDDEN LAYER olacak ve kac tane NEURON olacak bunlar icin Dense kullanilir. 

# 3 kez add yaptik yani 3 HIDDEN LAYER var.
model.add(Dense(4,activation="relu")) # 4 = neuron sayisi
model.add(Dense(4,activation="relu"))
model.add(Dense(4,activation="relu"))

model.add(Dense(1)) # cikti katmani

#SON ISLEM COMPILE
model.compile(optimizer = "rmsprop",loss = "mse")


"""BATCH = Ornegin 10.000 veri var. Bunları 500'er 500'er isle demeye yariyor.
           Bu ornekte 1000 veri az sayida veri oldugu icin gerek yok.

"""

"""TRAINING """
model.fit(x_train,y_train,epochs = 250)
loss = model.history.history["loss"]
#sbn.lineplot(x=range(len(loss)),y = loss)

trainLoss = model.evaluate(x_train,y_train,verbose=0)
testLoss  = model.evaluate(x_test,y_test,verbose=0)

""" MODEL DEGERLENDIRMESI """
testTahminleri = model.predict(x_test) #Bu fiyattan satabilirsin diye tahmin ediyor.
                                       #Gercek fiyatlar da y_test de mevcut. Kiyaslayabiliriz.

tahminDF = pd.DataFrame(y_test,columns=["GERCEK Y"])

testTahminleri = pd.Series(testTahminleri.reshape(330,))#Test tahminlerini array'den series'e cevirdik. DF'ye eklemek icin.

#Tahmin ve gercek sonuclari tek bir dataframe'de birlestirelim.

tahminVEgercekTestDF = pd.concat([tahminDF,testTahminleri],axis=1)
tahminVEgercekTestDF.columns = ["GERCEK Y","TAHMIN Y"]

sbn.scatterplot(x="GERCEK Y",y="TAHMIN Y",data=tahminVEgercekTestDF)
#MEAN_ABSOLUTE_ERROR = mean_absolute_error(tahminVEgercekTestDF["GERCEK Y"],tahminVEgercekTestDF["TAHMIN Y"])


yeniBisikletOzellikleri = [[1750,1760]]
yeniBisikletOzellikleri = scaler.transform(yeniBisikletOzellikleri)
model.predict(yeniBisikletOzellikleri)

model.save("bisiklet_modeli.h5")#Modeli kaydetmek icin (UZANTISI H5)
sonradanCagirmakIcin = load_model("bisiklet_modeli.h5")


"""SON"""