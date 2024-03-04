import random
sayi=random.randint(1,101)
sayac=1
while True:
    sayiver=int(input("Sayi tahmin ediniz."))
    if sayi==sayiver:
        print("Tahmininiz doğru",sayiver)
        print(sayac)
        break
    if sayi<sayiver:
        print("Daha küçük bir sayi gir.")
        sayac+=1
    if sayi>sayiver:
        print("Daha büyük bir sayi gir.")
        sayac+=1
