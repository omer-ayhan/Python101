try:
    hrs = float(input("Enter Hours:"))
    rate = float(input("Enter a rate: "))
    hrs_rate = hrs * rate
    print("Pay:", hrs_rate)
except:
    # This will evaluate if users don't enter a number
    print("Please enter a number")