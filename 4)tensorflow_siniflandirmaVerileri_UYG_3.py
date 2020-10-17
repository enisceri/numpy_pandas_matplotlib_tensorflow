#Bismillahirrahmanirrahim
import pandas            as pd
import seaborn           as sbn
import matplotlib.pyplot as plt
import tensorflow        as tf
from   tensorflow.keras.models import Sequential#Modeli bu siniftan olusturuyoruz.
from   tensorflow.keras.layers import Dense, Activation,Dropout #Model icerisinde katmanlarla calismak icin.
from   sklearn.model_selection import train_test_split #TEST VE TRAIN ICIN AYIRMAK
from   sklearn.preprocessing   import MinMaxScaler #SCALE icin.
from   sklearn.metrics         import mean_absolute_error,mean_squared_error
from   tensorflow.keras.models import load_model
from   tensorflow.keras.callbacks import EarlyStopping
from   sklearn.metrics         import classification_report,confusion_matrix

dataFrameMalicious = pd.read_excel("C:\\Users\\Admin\\Desktop\\YAPAY_ZEKA\\maliciousornot.xlsx")

dataFrameMalicious.info()

dataFrameMalicious.describe()
dataFrameMalicious.corr()["Type"].sort_values()

#sbn.countplot(x="Type",data=dataFrameMalicious)


#dataFrameMalicious.corr()["Type"].sort_values().plot(kind="bar")

y = dataFrameMalicious["Type"].values
x = dataFrameMalicious.drop("Type",axis=1).values


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.3,random_state = 15)     

scaler = MinMaxScaler()

scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

x_train.shape


model = Sequential()

model.add(Dense(units=30,activation="relu"))#30 noron
model.add(Dense(units=15,activation="relu"))#ara katmanlar 1 - 30 arasi
model.add(Dense(units=15,activation="relu"))#ara katmanlar 1 - 30 arasi
model.add(Dense(units=1,activation="sigmoid"))#Cikis katmani, sigmoid siniflandirma problemlerinde

model.compile(loss= "binary_crossentropy",optimizer="adam")

model.fit(x=x_train, y= y_train,epochs=700 ,validation_data=(x_test,y_test),verbose=1)#overfitting olsun epochs'u abartalim

modelKaybi = pd.DataFrame(model.history.history)

modelKaybi.plot()


"""OVERFITTING OLURSA VERI EGITIMINI DEVAM ETTIRMEYE GEREK YOK. ZATEN BITMIS YANI ->EARLY STOPPING KULLANIMI"""
"""
model.add(Dense(units=30,activation="relu"))#30 noron
model.add(Dense(units=15,activation="relu"))#ara katmanlar 1 - 30 arasi
model.add(Dense(units=15,activation="relu"))#ara katmanlar 1 - 30 arasi
model.add(Dense(units=1,activation="sigmoid"))#Cikis katmani, sigmoid siniflandirma problemlerinde

model.compile(loss= "binary_crossentropy",optimizer="adam")

earlyStopping = EarlyStopping(monitor="val_loss",mode="min",verbose=1,patience=25)
model.fit(x=x_train,y=y_train,epochs=700,validation_data=(x_test,y_test),verbose=1,callbacks=[earlyStopping])

Mesela burada 700'de degil 246 'da durdu. EARLY STOPPING CUNKU.
"""
#################################################################
"""DROPOUT"""

"""
model.add(Dense(units=30,activation="relu"))#30 noron
model.add(Dropout(0.6))#HER KATMANA KONUR. CIKIS HARIC CUNKU 1 UNIT VAR CIKISTA.

model.add(Dense(units=15,activation="relu"))#ara katmanlar 1 - 30 arasi
model.add(Dropout(0.6))

model.add(Dense(units=15,activation="relu"))#ara katmanlar 1 - 30 arasi
model.add(Dropout(0.6))

model.add(Dense(units=1,activation="sigmoid"))#Cikis katmani, sigmoid siniflandirma problemlerinde

model.compile(loss= "binary_crossentropy",optimizer="adam")

earlyStopping = EarlyStopping(monitor="val_loss",mode="min",verbose=1,patience=25)

model.fit(x=x_train,y=y_train,epochs=700,validation_data=(x_test,y_test),verbose=1,callbacks=[earlyStopping])





kayipDataFrame = pd.DataFrame(model.history.history)


kayipDataFrame.plot()
tahminlerimiz = model.predict_classes(x_test)
tahminlerimiz

print(classification_report(y_test,tahminlerimiz))
print(confusion_matrix(y_test,tahminlerimiz))
"""
