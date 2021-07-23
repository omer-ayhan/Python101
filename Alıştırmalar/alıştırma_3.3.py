# finput = input("Enter the directory: ")
file = open('Alıştırmalar/mbox-short.txt',"r")
total = 0
count = 0
for line in file:
    # this will only take strings that starts with "X-DSPAM-Confidence: "
    if line.startswith("X-DSPAM-Confidence: "):
        # chosen string will be sliced accordingly so we can take the string with digits to convert it to a float
        # also every converted number will add up with previous number each time
        total += float(line[line.find(':')+1:])
        # counts how many time we performed this process to calculate the average number
        count+=1
# at the end we calculate our both values according to the formula of average number
print("Average X-DSPAM-Confidence:", total/count)