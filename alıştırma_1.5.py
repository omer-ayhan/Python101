try:
    score = float(input("Enter Score: "))
    if score>=0.0 and score<=1.0:
        if score>=0.9:
            print(score,"A")
        elif score>=0.8:
            print(score, "B")
        elif score >= 0.7:
            print(score, "C")
        elif score >= 0.6:
            print(score, "D")
        elif score<0.6:
            print(score, "F")
    else:
        print("Sayı aralık dışında")
        quit()

except ValueError:
    print("Please enter a number")