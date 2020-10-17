import numpy as np

#numpy arrays
liste = [20,30,40] 


matrix = [[1,2,3],[3,4,5],[6,7,8]]
print(np.array(matrix[1]))

#arange fonk.
print(np.arange(0,10))

#arange atlayarak saymak icin
print(np.arange(0,10,2))

#zeros ve ones
print(np.zeros(5))

#linspace   
print(np.linspace(0,20,6)) #esit mesafede 6 sayi 

#eye -> birim matris (identity matrix)
print(np.eye(3))

#random, rastgele bir array ya da matrix ya da tek bir deger
print(np.random.randn(4))
print(np.random.randint(1,10))

#indexlere erisim ve manipulasyon
benimDizim = np.arange(0,20)
benimDizim[0:8] = -3
print(benimDizim)

ikinciDizi  = np.arange(0,20)
slicingDizi = ikinciDizi[0:10]
slicingDizi[:] = 600
print(slicingDizi)   
print(ikinciDizi) # !!!!!!!!!!! ikinciDizi'nin elemanlari da degisti.

#matrixlerle index erisimi
benimListem = [[1,2,3],[4,5,6],[7,8,9]]
benimMatrixDizim = np.array(benimListem)
print()
print(benimMatrixDizim[0:3,0:2]) # tum satirlari al, ilk iki sutunu al

#Operasyonlar: toplama, cikarma vs.
dizi1 = np.random.randint(1,100,20)
print(dizi1 > 24)

dizi2 = np.arange(0,10)
dizi3 = dizi2 + dizi2
print(dizi3)