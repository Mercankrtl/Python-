# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 19:30:37 2024

@author: merca
"""

'''
programa_diller=["Python","C#","Java","Javascript"]

sonuc=programa_diller
sonuc=type(programa_diller)
sonuc=programa_diller[0:2]
sonuc=programa_diller[:2]
sonuc=programa_diller[:]
sonuc=programa_diller[-3:-1]
sonuc=programa_diller[-3:]


print(sonuc)

'''

'''
#1-"Toyota,BMW ,Renault,Mercedes"elemanlarina sahip  markalar isimli bir liste olusturunuz.

markalar=["Toyota","BMW" ,"Renault","Mercedes"]

#2-Liste kac elemanlidr?

sonuc=len(markalar)


#3-Listenin ilk ve son elemani nedir?

print(markalar[0])
print(markalar[-1]) 

#4-"Renault" markasini "Togg" ile guncelleyiniz.

markalar[2]="Togg"
sonuc=markalar 

#5-"Togg" listenin bir elemani miidr?

sonuc="Togg" in markalar

#6-Listenin ilk 2 elemanini aliniz.

sonuc= markalar[0:2]

#7-Listenin sonuna "Ford" ve "Citroen" markalarini ekleyiniz.

sonuc=markalar+["Ford","Citroen"]

#8-Listenin son elemanini siliniz.

del markalar[-1]
sonuc=markalar

#9-Asagidaki verileri liste icerisinde saklayiniz.
      #Ogrenci1:Yigit Bilgi 2010[70,80,90]
      #Ogrenci2:Ada Bilgi   2011[70,70,80]
      #Ogrenci3:Cinar Turan 20017[60,60,90]
      
ogrenci1=["Yigit", "Bilgi", "2010",[70,80,90]]  
ogrenci2=["Ada", "Bilgi", "2011",[70,70,80]]   
ogrenci3=["Cinar", "Turan", "2017",[60,60,90]]    

ogrenciler=[ogrenci1,ogrenci2,ogrenci3]

      
 #10-Ogrencilerin yaslarini hesaplayiniz
 
yasYigit=2024-ogrenci1[2]
yasAda=2024-ogrenci2[2]
yasCinar=2024-ogrenci3[2]

print(yasYigit,yasAda,yasCinar)
 
#11-Ogrencilerin not ortalamalarini hesaplayiniz.

print(sonuc)     


'''

sayilar=[4,6,8,2,56,78,90]
isimler=['canan','ahmet','zeynep','gokhan','ali']

sonuc=min(sayilar)
sonuc=min(isimler)
sonuc=max(sayilar)
sonuc=max(isimler)

'''
#ekleme
sayilar.append(12)
isimler.append('mercan')
sonuc=isimler

sayilar.insert(0,100)
sayilar.insert(-1,100)
sayilar.insert(-3,100)
sayilar.insert(len(sayilar),100)


#silme
sayilar.pop()
sayilar.pop(0)
isimler.remove('canan')
sonuc=isimler


#siralama

sayilar.sort()
isimler.sort()
sayilar.reverse()


sonuc=sayilar



print(sonuc)



customers=['sadikturan','ahmetyilmaz','cinarturan','yigitbilgi']
order_totals=[12000,13000,5000,15000]


#1-'sadikturan' kullanici adiyla yapilan 5000 liralik siparisi listeye ekleyiniz.

customers.append('sadikturan')
order_totals.append(5000)

sonuc=customers
sonuc=order_totals


#2-son eklenen siparisi siliniz.

customers.pop()
sonuc=customers

order_totals.pop()
sonuc=order_totals


#3-Tum siparisler icin asagidaki ozet cumleyi yazdiriniz:
      #'<username>' isimli musterinin siparis toplami'<1000>' liradir.
      
#sonuc=f"{customers[1]} isimli musterinin siparis toplami {order_totals[1]} liradir.}"

#4-Musterileri alfabetik olarak siralayiniz.

customers.sort()
sonuc=customers

#5-Siparis toplamlarini azalan sekilde siralayiniz.

order_totals.sort()
order_totals.reverse()
sonuc=order_totals

#6-En dusuk siparis hangisidir?

sonuc=min(order_totals)
sonuc=max(order_totals)


#7-'sadikturan' isimli kullanicinin kac tane siparisi vardir?

sonuc=customers.count('sadikturan')

#8-Customers listesinden 'ahmetyilmaz' isimli kullaniciyi siliniz.

customers.remove('ahmetyilmaz')

#9-Listelerdeki tum icerikleri siliniz.

customers.clear()
sonuc=customers

order_totals.clear()
sonuc=order_totals

#10-Kullaniciidan aldiginiz kullanici adi ve siparis toplamlarini listeye ekleyiniz.

username=input('musteri adi: ')
toplam= input('toplam: ')

customers.append(username)
order_totals.append(toplam)

print(customers)
print(order_totals)


print(sonuc) 

'''

'''
#TUPLE : listeden farkli olarak elemanlar degistirilemez.Ekleme,cikarilma ya da silme yaplamz..Kucuk alanda klair .Liste kucuktur.
my_list=[1,2,3]
my_tuple=(1,2,3,1)

print(type(my_list))
print(type(my_tuple))  #degistirilemez.


my_list[0]=2
#my_tuple[0]=2

my_list.append(3)

sonuc=my_tuple.count(1)
print(sonuc)

'''














































