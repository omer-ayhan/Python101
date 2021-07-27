finput = "Alıştırmalar/mbox-short.txt"
# turns all lines into a list element to keep them in one list 
f = open(finput).readlines()
# to count number of persons
count = 0
for line in range(len(f)):
    # choose lines that starts with "From"
    if f[line].startswith("From"):
        # loop over that line
        for name in f[line].split():
            # to check if that list item includes "@" symbol
            if "@" in name:
                count += 1
                # print both person's number and our chosen sliced string
                print(count,":",name[0:name.find("@")])

print(count,"person")