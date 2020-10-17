import numpy  as np
import pandas as pd

#series
dict1 = {"Enis" : 22, "M. Eren" : 15, "Husna" : 9}
print(pd.Series(dict1))

yaslar  = [22,15,9]
isimler = ["Enis","M.Eren","Husna"]
print()
#data solda index sagda yazilmasi daha uygun.
print(pd.Series(data = yaslar, index = isimler))
#bu yazimda index sagdaki olur
yarisma = pd.Series([90,80,70],["Mehmet","Akif","Arif"])
print()
print(yarisma)

#dataframes

random_matrix = np.random.randint(0,100,(4,3)) #0 - 100 arasinda 4'e 3'luk bir matrix

dataFrame = pd.DataFrame(random_matrix,index=["Mehmet","Akif","Arif","Enis"],columns=["Mat 1","Mat 2","Mat 3"])
print()
print(dataFrame)

print(dataFrame["Mat 1"])
dataFrame["Fen 1"] = [30,40,50,60]
print(dataFrame)

#bir satiri ya da bir sutunu silmek
dataFrame.drop("Fen 1",axis = 1, inplace = True) #sutun axis = 1 oluyor ve df'den bir sey silmek icin inplace TRUE olmali
print("\n\n")
print(dataFrame)

#loc ile degere erisme
print("\n\n")
print(dataFrame.loc["Enis"]["Mat 1"])
print(dataFrame.loc["Enis","Mat 3"])

print(dataFrame < 50)

#mat 1 sinavinda 50'den buyuk alanlari gorelim mesela
print(dataFrame[dataFrame["Mat 1"] > 50]) 

#indexlerle calismak
yeni_index = ["Enis Ceri","Mehmet Ersoy","Akif Sabanci","Arif Sabuncu"]
dataFrame["Yeni indexler"] = yeni_index
dataFrame.set_index("Yeni indexler",inplace=True)

#multi index
ilk_indeksler = ["Ceri","Ceri","Ceri","Killioglu","Killioglu","Killioglu"]
ikinci_indeks = ["Enis", "Seyit","M.Eren","Onur","Duran","Sumeyya"]
birlesik_indeks = list(zip(ilk_indeksler,ikinci_indeks))
print(birlesik_indeks)
birlesik_indeks = pd.MultiIndex.from_tuples(birlesik_indeks)
print("\n")
print(birlesik_indeks)

yas_meslek_list = [[22,"Muhendis"],[50,"Muhendis"],[15,"Ogrenci"],[30,"Yonetici"],[60,"Sofor"],[28,"Sekreter"]]

aile_df = pd.DataFrame(yas_meslek_list,birlesik_indeks,["Yas","Meslek"])


print(aile_df)
aile_df.index.names = ["Soyad","Ad"]

ceri = aile_df.loc["Ceri"]


#operasyonlar - eksik veriler

sozluk = {"Istanbul":[30,29,np.nan],"Ankara":[25,np.nan,26],"Izmir":[33,32,30]}
havaDurumu_df = pd.DataFrame(sozluk,index=[1,2,3])
havaDurumu_df.index.names = ["Gunler"]

#dataFrame1.dropna(axis=1,thresh=2) dersek 2 adet NaN olan sutunlari atar sadece
havaDurumu_df.fillna(10,inplace=True)


#groupby
dict1 = {"Departman":["Yazilim","Yazilim","Yapay Zeka","Yapay Zeka","IT","IT","IK","IK"],
         "Isim":["Enis","Eren","Mustafa","Husna","Seyit","Umran","Ahmet","Erva"],
         "Maas:":[3000,2800,4100,3900,3600,4000,2500,3500]}

indeks_sirket = np.arange(1,9)
sirket_df = pd.DataFrame(dict1,index=indeks_sirket )
sirket_df.index.names = ["Eleman"]



grup_objesi = sirket_df.groupby("Departman")
print(grup_objesi.count())

grup_describe = (grup_objesi.describe())


#concatenation - concat, DATAFRAME'leri birlestirmek
#pd.concat([dataFrame1,dataFrame2,dataFrame3],axis=0)

#merge - kaynastirmak,iki ayni tablo ama bir sutunda farkli bir ozellik varsa ve onu tek bir 
#tabloda birlestirmek istitorsak
#pd.merge(dataFrame1,dataFrame2, on="Isim"),Isim sutunu ortak mesela,on dedigi ortak nokta

#maasDataFrame["Departman"].unique() #Hangi departmanlar var gormek icin
#maasDataFrame["Departman"].nunique()#Kac departman var gormek icin
#maasDataFrame["Departman"].value_counts() #Hangi departmandan kac tane var gormek icin


#FONKSYIYONLARLA DATAFRAMELER
dict_maas = {"Departman":["Yazilim","Satis","Hukuk","Yazilim"],
             "Isim": ["Hakan","Semih","Barkin","Suleyman"],
             "Maas":[200,300,180,420]}
maasDataFrame = pd.DataFrame(dict_maas)


def Brutten_NetMaasa(maas):
    return maas * 0.66

net_maas = maasDataFrame["Maas"].apply(Brutten_NetMaasa)
maasDataFrame["Net Maas"] = net_maas
null_var_mi = maasDataFrame.isnull()#NULL var mi gormek icin yani NaN


#PIVOT TABLE
yeni_dict = {"KANAL":["CARTOON NETWORK","CARTOON NETWORK","TRT COCUK","TRT COCUK","TRT COCUK"],
           "KARAKTER":["Buggs Bunny","Tom ve Jerry","Niloya","Pepe","Pepe"],
           "YAS":[22,16,5,4,6]}

karakter_DF = pd.DataFrame(yeni_dict)
karakter_pivot = karakter_DF.pivot_table(values="YAS",index=["KANAL","KARAKTER"],aggfunc=np.sum)











