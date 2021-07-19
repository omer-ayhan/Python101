list_comp = [0,1566461,4646161,46464,956]
list_comp2 = [0,16,16,58,0,25,4]

def find_max(nums):
    temp = None
    if isinstance(nums, list):
        for num in nums:
            if temp is None:
                temp = num
            elif num>temp:
                temp = num
        return temp
    else:
        print("Please enter a list")
        return None

print(find_max(list_comp))
print(find_max(list_comp2))