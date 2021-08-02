import string
fopen = open("Lab Projeleri/lorem.txt").read().lower()
alphabet = [i for i in string.ascii_lowercase]
histogram = dict()

for word in fopen:
    if word.isalnum() and word.isnumeric()==False:
        histogram[word] = histogram.get(word, 0) + 1

for key, value in histogram.items():
    print(f"{key} : {value:3} {'*'*value}")