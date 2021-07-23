file = open("Kişisel Projelerim/checklist.txt", "r")
# file_list = file.readlines()

for line in file:
        print(":white_check_mark:" , line)
        
file.close()