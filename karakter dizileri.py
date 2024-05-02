# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 16:28:42 2024

@author: merca
"""
'''
kursAdi="Python ile Programlama"
kursAciklama="Guzel bir kurs"
kursSuresi="20 Saat"

mesaj="kurs adi: "+kursAdi+" "+"Kurs aciklamasi: "+kursAciklama+" "+"Kurs Suresi: "+kursSuresi

print(mesaj) 
'''

'''
kurs="Python ile Programlama"

print(kurs[0])
print(kurs[-1])

adet=len(kurs)

print(adet)
print(kurs[adet-1])
print(kurs[0:6])
print(kurs[6])
print(kurs[11:len(kurs)])
print(kurs[11:])
print(kurs[-11:-1])
print(kurs[0:20:2])

print(kurs[::1])

'''

'''
#string contact
ad="Sadik"
soyad="Turan"
yas=40

msj= "My name is "+ad+" "+soyad+"."+"I'm "+str(yas)+" years old."
print(msj)

#string format

msj="My name {} {} . I'm {} years old.".format(ad,soyad,yas)
msj="My name is {0} {1}.I'm {2} years old.".format(ad,soyad,yas)
msj="My name is {a} {s}. I'm {y} years old.".format(a=ad, s=soyad, y=yas)
print(msj)


#f string

msj=f"My name {ad} {soyad}. I'm {yas} years old."
print(msj)

'''

'''
title="Python ile Programlama Dersleri"

#1-'title' degiskeni icerisindeki karakter sayisi nedir?

adet=len(title)
print(adet)

#2-'title' icerisindeki 'Python' kelimesini alin.

print(title[ :6])


#3-'title' degiskeninin ilk 5 ve son 5 karakterini alin.

print(title [:6])
print(title [-5:])


#4-'title' degiskenini tersten yazdirin.
print(title[ ::-1])


#5-Klavyeden girilen ogrenci bilgisine gore ornek verilen cumleyi yazdriniz.
   #ornek=Cinar Turan iismli ogrencinin 1.notu 60 , 2.notu 60 ve notortalamasi 60 olarak hesaplanmistir.
   
ad=input('ad: ')
soyad=input('soyad: ')
not1= input('1.not: ')
not2=input('2.not: ')
ortalama=(float(not1)+ float(not2))/2

sonuc=f"{ad} {soyad} isimli ogrencinin 1.notu {not1}, 2.notu {not2} ve ortalamasi {ortalama} olarak hesaplanmistir."
print(sonuc)

'''
'''

mesaj="btk akademi, python kursu"

sonuc=mesaj.upper()
sonuc=mesaj.lower()
sonuc=mesaj.title()
sonuc=mesaj.capitalize()
sonuc="abc".isalnum()

sonuc=mesaj.islower()
sonuc=mesaj.strip()
sonuc=mesaj.split()
sonuc=mesaj.split(',')
sonuc=mesaj.index("akademi")
sonuc=mesaj.replace("python","javascript")


print(sonuc)

'''

'''

kursAdi="Btk Akademi Python ile Programlam Dersleri"
website="https ://www.btkakademi.gov.tr/"

#1-'Btk Akademi ' karakter dizisinin bas ve sondaki bosluk birakarak karakterlerini siliniz.

sonuc='Btk Akademi '.strip()


#2- kursAdi degiskenindeki tum karakterleri kucuk harfe ceviriniz.

sonuc=kursAdi.lower()

#3-website degiskeninde kac tane '.' karakteri vardir?

sonuc=kursAdi.count('.')


#4-website degiskenini 'https' ile mi basliyor ?

#sonuc=website.startwith('https')

#5- website 'tr' ile mi bitiyor?

#sonuc=website.endwith('tr')

#6-kursAdi icerisindeki tum karakterler harflerden mi olusuyor?

sonuc=kursAdi.isalpha()

#7-kursAdi degiskenindeki tum bosluklari'-' ile degistirniz.

sonuc=kursAdi.replace(' ','-')


#8-kursAdi degiskenindeki Python kelimesini ReactJs ile degistiriniz.

sonuc=kursAdi.replace('Python','ReactJs')


#9- website degiaskeni 'www' iceriyor mu ?

sonuc=website.index('www')


#10-kursAdi degiskenini listeye ceviriniz.

sonuc=kursAdi.split()


print(sonuc)

'''












































