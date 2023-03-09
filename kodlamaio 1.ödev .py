#string - metinsel ifadeler
print("bu bir metinsel ifadedir")
print("36") #bu sayı değeri taşımaz yani bu da metinsel ifadedir
#int, integer - tam sayılı ifadeler
print(10) #direkt sayı olarak çıkar
#float, decimal, double - ondalıklı ifadeler 
print(365.6)
#bool, booleen - true ve ya false (Örneğim dövizde yükselişte değilse aşağı ok ikonu gibi)
#-----------------------------------------------------------------------------------------
#Değişken atama - String
t = "talimatlar"
k = "kişisel gelişim kursları"
p = "pyhton öğrenme kursu"
print(t)
print(k)
print(p)
#Değişken atama - integer
haftalikDersSaati = 35
birHaftadakiGünSayisi = 7
günlükDersSaati = print(haftalikDersSaati / birHaftadakiGünSayisi)
print(haftalikDersSaati)
print(birHaftadakiGünSayisi)
#matematiksel operatörler
# bölme
sehirSayisi = 81
barinakSayisi = 24300
köpekSayisi = 486000
sehreDüsenKöpekSayisi = print(köpekSayisi / sehirSayisi)
barinakBasinaDüsenKöpekSayisi = print(köpekSayisi / barinakSayisi)
# çarpma
barinakBasinaDüsenKöpekSayisi = 20
sehreDüsenKöpekSayisi = 600
print(barinakBasinaDüsenKöpekSayisi * sehreDüsenKöpekSayisi)
# toplama
print(sehirSayisi + sehreDüsenKöpekSayisi)
# çıkarma
print(barinakSayisi - barinakBasinaDüsenKöpekSayisi)


#mod alma - mod operatör(mod hesaplama-sayıların birbirine bölümünden kalan bulma)
print(sehirSayisi%barinakBasinaDüsenKöpekSayisi)

#mantıksal operatörler 
print(1 == 1) #true
print(2 == 1) #false
print(1 != 1) #false
print(2 != 1) #true

print(2 == 2 or 3 > 4 and 5 < 3 or 1 != 1) #true

#karar yapıları(if,if else, else)

sayi1 = 12
sayi2 = 10

if sayi1 > sayi2: 
    print("sayi1 sayi2 den büyüktür")
#eğer if bloğuna girmezse
elif sayi1 == sayi2:
    print("sayi1 ve sayi2 eşittir")
# eğer if ve else if(elif) bloklarından hiç birine girmezse
else:
    print("sayi1 sayi2 den küçüktür")


