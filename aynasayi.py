# ayna sayıları bulma programı 

sayi = int(input("Sayi giriniz"))
liste = []
for i in range(1,sayi+1):
    ssayi=str(i)
    if len(ssayi)%2==0:
        bas= ssayi[:int(len(ssayi)/2)]
        son= ssayi[int(len(ssayi)/2):]
        rson = son[::-1]
        if (bas==rson):
            print(i)
            liste.append(i)
print(len(liste),"tane ayna sayı vardır." )
