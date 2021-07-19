file = open("Kişisel Projelerim/checklist.txt", "r")
file_list = file.readlines()

file.close()
for line in file_list:
        print(":white_check_mark:" + line)