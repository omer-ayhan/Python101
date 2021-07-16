try:
    hrs = float(input("Enter hours: "))
    if hrs <= 40:
        rate = 10
    else:
        rate = 15

    pay = hrs * rate
    print("Your pay:", pay)
except:
    print('Please enter a number')