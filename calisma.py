# İstenilen sayıya kadar olan sayıları topla
# def toplama(sayi):
#     toplam=0
#     for i in range(1,sayi+1):
#         toplam=toplam+i
#     return toplam

# sayi=int(input("bir sayi giriniz. \n"))
# print(toplama(sayi))


# Çarpma kullanmadan çarpım yapma
# sayi1= int(input("Birinci sayiyi giriniz. \n"))
# sayi2= int(input("İkinci sayiyi giriniz. \n"))
# def carpma(sayi1, sayi2):
#     toplam=0
#     for i in range(1,sayi2+1):
#         toplam=toplam+sayi1
#     return toplam
# print(carpma(sayi1, sayi2))


# # Faktoriyel hesaplama
# sayi=int(input("Bir sayi giriniz. \n"))
# def fakto(sayi):
#     fakto=1
#     for i in range(1,sayi):
#         fakto=fakto*i
#     return fakto
# print(fakto(sayi))


# sayi=int(input("Sayı giriniz. \n"))
# for ms in range(1,sayi):
#     toplam=0
#     for i in range(1,ms):
#         if ms%i==0:
#             toplam=toplam+i
#     if toplam==ms:
#         print("Mükemmel Sayı",ms)

def ms(sayi):
    toplam=0
    for i in range(1,sayi):
        if (sayi%i==0):
            toplam=toplam+i
    if toplam==sayi:
        print("Mükemmel sayi",sayi)
    
sayi=int(input("Sayı giriniz. \n"))

for k in range(1,sayi+1):
    ms(k)