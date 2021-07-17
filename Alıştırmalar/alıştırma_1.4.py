try:
    hrs = float(input("Enter hours: "))
    if hrs <= 40:
        rate = 10
        pay = hrs * rate
    else:
        rate = 15

    pay = ((hrs - 40) * rate) + 400
    print("Your pay:", pay)
except:
    print('Please enter a number')