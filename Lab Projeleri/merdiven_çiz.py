def merdiven(adet,boşluk=1):
    for i in range(1,adet+1):
        print(" "*(adet-i)+ "#"*i,end="")
        print(' '*boşluk,end="")
        print("#"*i)
while True:
    try:
        adet_input = int(input("Basamak sayısını giriniz: "))
        boşluk_input = int(input("Boşluk sayısını giriniz: "))
        merdiven(adet_input, boşluk_input)
        break
    except:
        print("Lütfen sayı giriniz")