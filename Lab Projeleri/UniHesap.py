while True:
    try: 
        isim = input('İsminiz:')
        yaş = int(input('Yaş:'))
        ortalama = int(input('ortalama: '))

        if(ortalama>0 and ortalama<100):
            if((yaş>17 and yaş<21) and ortalama>=80):
                print("sayın",isim,"geçtiniz")
                break
            else:
                print("sayın",isim,"kaldınız ve geçemediniz")
                break
        else:
            print("0-100 arası giriniz")
    except:
        print("Not a number")