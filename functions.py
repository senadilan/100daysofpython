# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 16:32:37 2025

@author: sena
"""

******************************
#1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
def mukemmel_mi(sayı):
    toplam=0
    for i in range(1,sayı):
        if (sayı%i==0):
            toplam+=i
    if (toplam==sayı):
        return True
    else:
        return False
    
for j in range(1,1001):
    if (mukemmel_mi(j)):
        print("{} mukemmel sayıdır".format(j))
        

********************************
#Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.      

a=int(input("ilk sayı girin:"))
b=int(input("ikinci sayı girin:"))

def ebob(a,b):
    max_ebob=1
    for i in range(1,max(a,b)):
        if (a%i==0) and (b%i==0):
            if (i>max_ebob):
                max_ebob=i
     
    print(max_ebob)           


          
ebob(a, b)



***********************************
#Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.
sayi1 = int(input("İlk sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))
  

def ebob(a, b):
    max_ebob = 1
    for i in range(1, min(a, b) + 1):
        if (a % i == 0) and (b % i == 0):
            max_ebob = i
    return max_ebob 

def ekok(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // ebob(a, b) 



print(f"EKOK({sayi1}, {sayi2}) = {ekok(sayi1, sayi2)}")


*************************************
#Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.
 
sayı=int(input("sayı giriniz: "))



birler=["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]
onlar=["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]

def okunus(sayı):
    ikinci=sayı//10
    birinci=sayı%10
    return onlar[ikinci] + " " + birler[birinci]

print(okunus(sayı))


*******************************************
#1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)

def pisagor_bulma():
    
    pisagor_listesi = list()
    for i in range(1,101):
        for j in range(1,101):

            c = (i ** 2 + j ** 2) ** 0.5

            if (c == int(c) ):
                pisagor_listesi.append((i,j,int(c)))

    return pisagor_listesi

for i in pisagor_bulma():
    print(i)
