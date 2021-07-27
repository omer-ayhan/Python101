finput = input('Enter your file: ')
f_list = open(finput).read().split()
word_list=list()
for el in f_list:
    if el not in word_list:
        word_list.append(el)
        
word_list.sort()
print(word_list)

for e in range(len(word_list)):
    print(word_list[e])
