def computePay(hrs):
    if hrs<=40:
    # pay is 10 TL up to 40 hours
        pay = 10
    else:
    # pay is 15 TL if it's more than 40 hours 
        pay = 15
    # computes the brut pay
    return hrs * pay
    
try:
    work_hrs = float(input("Enter hours: "))

    # saves the residual value of our "computePay" function to "brut_pay" variable
    brut_pay = computePay(work_hrs)

    print("Your brut pay:", brut_pay)
    
except ValueError:
    print("Please enter a number ")
    quit()
    