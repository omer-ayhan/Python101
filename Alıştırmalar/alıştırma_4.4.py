file = input('Enter File Name: ')
if len(file) < 1 : file = "mbox-short.txt"
fread = open(file).readlines()
counts= dict()

for line in fread:
    if line.startswith("From "):
        key = line.split()[-2]
        counts[key[:key.find(":")]] = counts.get(key[:key.find(":")],0) + 1

# long way
# for key,val in sorted(counts.items(),reverse=True):
#     print(f"saat {key}: {val} defa")

# shortened way
print("\n".join([f"hour {key}: {val} times" for key,val in sorted(counts.items(),reverse=True)]))