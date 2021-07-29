fname = "Alıştırmalar/mbox-short.txt"
if len(fname)<1:
    # if the input is empty this will be assigned by default
    fname = "Alıştırmalar/mbox-short.txt"

f = open(fname)
f_list = list()
count = dict()

for line in f:
    if line.startswith("From"):
        # turns our line into a list
        f_list=line.split()
        # checks if our object exist in the dictionary if not it will add it into dictionary as new one
        count[f_list[1]] = count.get(f_list[1],0) + 1

# loops through our dictionary
for i in count:
    # checks which value inside dictionary matches maximum value inside that dictionary
    if count[i] == max(count.values()):
        print("most repeated mail: ",i,max(count.values()),"times")
