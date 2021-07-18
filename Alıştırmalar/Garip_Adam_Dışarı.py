def left_over(num_people, num_groups):
    if num_people<num_groups:
        return "group number should be equal or less than people's number"
    return num_people%num_groups
    
print(left_over(6,5))