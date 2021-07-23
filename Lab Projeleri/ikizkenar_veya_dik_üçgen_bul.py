import math as m
while(True):
    try:
        kenar1 = float(input("1.kenar: "))
        kenar2 = float(input("2.kenar: "))
        kenar3 = float(input("3.kenar: "))

        if (kenar1+kenar2>kenar3):
            if(m.pow(kenar1,2) + m.pow(kenar2,2))==m.pow(kenar3,2):
                print("dik üçgen")
                break
            elif kenar1==kenar2==kenar3:
                print("hem ikizkenar hem de eşkenar üçgen")
                break
            elif kenar1==kenar2 or kenar2==kenar3 or kenar3==kenar1:
                print("ikizkenar üçgen")
                break
            else:
                print("sıradan bir üçgen")
                break
        else:
            print("herhangi bir üçgen sağlanmıyor")
    except ValueError:
        print("Üç kenarıda girmen lazım ya da tüm kenarların sayı olması lazım")