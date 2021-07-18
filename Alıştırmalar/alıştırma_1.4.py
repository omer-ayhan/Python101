try:
    hrs = float(input("Enter hours: "))
    if hrs <= 40:
        # (Türkçe)40 saate kadar saatbaşı 10 TL
        # (English)10 TL per hour up to 40
        rate = 10
        pay = hrs * rate
    else:
        rate = 15

    # (Türkçe)Buradaki işlemde 40 saate kadar saatbaşı ücret 10 TL olduğundan onu çıkarıp kalan saati belirlediğimiz 15 TL ile çarpıp daha sonra 40 saate kadar olan toplam ücreti ayrı bir şekilde ekliyoruz
    # (English)the reason we substract 40 from 'hrs' variable is because we can only multiply hours after 40 with 15 TL(which is the 'rate' variable). After that calculation is done then we add the total pay up to 40 hours seperately. Since we need sum of all values 
    pay = ((hrs - 40) * rate) + 400
    print("Your pay:", pay)
except:
    print('Please enter a number')