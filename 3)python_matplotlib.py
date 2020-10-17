import numpy      as np 

import matplotlib.pyplot as plt

#GRAFIK ILK ORNEK
"""
yas_listesi  = [10,20,30,30,30,40,50,60,70,75]
kilo_listesi = [20,60,80,85,86,87,70,90,95,90]

np_yas_array  = np.array(yas_listesi)
np_kilo_array = np.array(kilo_listesi)

plt.plot(np_yas_array,np_kilo_array,"r")#r = red, g = green vs.
plt.title("Yaş-Kilo Grafiği")
plt.xlabel("Yaş")
plt.ylabel("Kilo")
plt.grid(True)
"""
########MULTI GRAFIK - COKLU GRAFIK
"""
np_dizi1 = np.linspace(0,10,20)
np_dizi2 = np_dizi1 ** 3

plt.subplot(2,1,1)
plt.plot(np_dizi1,np_dizi2,"r*-")
plt.title("MOTOR RPM")

plt.subplot(2,1,2)
plt.plot(np_dizi2,np_dizi1,"b--")
plt.title("MOTOR HIZ")

plt.show()
"""
###FIGURE FIGURE FIGURE FIGURE FIGURE FIGURE
###TEK BIR KODDA COKLU GRAFIK ICIN, ornegin Motor RPM ve Motor Sicaklik, Motor Bataryasi vs gibi

#figure1 = plt.figure()
#figure2 = plt.figure()

motor_sicaklik = np.array([20,18,21,19,26,28])
motor_rpm      = np.array([2,4,6,5,6,13])
zaman          = np.array([10,20,30,40,50,60])
"""figure1_axes = figure1.add_axes([0.2,0.2,0.9,0.9])
figure1_axes.plot(motor_rpm,motor_sicaklik,"g")
figure1_axes.set_xlabel("RPM")
figure1_axes.set_ylabel("Sıcaklık")
figure1_axes.set_title("RPM-SICAKLIK")

"""
#Motor sicaklik ve rpm'ini cizmek istiyorum diyelim.

#MOTORA ait iki ya da daha cok farkli grafigi burada gorebilirim.
figure1 = plt.figure(figsize=(10,10)) 

ax = figure1.add_subplot(1,1,1)
ax.plot(motor_rpm,motor_sicaklik,"b",label ="motor sicakligi")
ax.set_title("Motor RPM-Sıcaklık Grafiği")
ax.set_xlabel("RPM")
ax.set_ylabel("Sıcaklık")
ax.legend()


figure3 = plt.figure(figsize=(10,10),dpi=100) 

ax3 = figure3.add_subplot(1,1,1)
ax3.plot(motor_rpm,motor_sicaklik,"b",label ="motor sicakligi")
ax3.set_title("Motor RPM-Sıcaklık Grafiği")
ax3.set_xlabel("RPM")
ax3.set_ylabel("Sıcaklık")
ax3.legend()



figure2 = plt.figure()
ax2 = figure2.add_subplot(1,1,1)
ax2.plot(zaman,motor_sicaklik,"r--")
ax2.set_title("Motor Zaman-Sıcaklık Grafiği")
ax2.set_xlabel("Zaman (saniye)")
ax2.set_ylabel("Sıcaklık")

plt.show()

#FIGURE KAYIT ETMEK ICIN
#figure1.savefig("C:\\Users\\Admin\\Desktop\\YAPAY_ZEKA\\resim1.png",dpi = 200)
#figure1.savefig("C:\\Users\\Admin\\Desktop\\YAPAY_ZEKA\\resim2.png",dpi = 1800)
"""
Dpi'in degeri cozunurluk icin onem tasir. Kaliteli bir resim icin dpi buyuk secilebilir.
"""


#SCATTER PLOT
"""
figure4 = plt.figure()
ax4 = figure4.add_subplot(1,1,1)
ax4.scatter(motor_rpm,motor_sicaklik)
plt.show()
"""

#HISTOGRAM
"""
plt.hist(motor_rpm)
plt.show()
"""
#BOXPLOT
"""
yeni_dizi= np.arange(0,10)
plt.boxplot(yeni_dizi)
"""















