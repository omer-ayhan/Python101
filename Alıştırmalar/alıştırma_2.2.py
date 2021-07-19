largest = None
smallest = None
# list of written numbers
nums = []

while True:
    try:
        num_input = input("Enter a number: ")
        if num_input=="Done!":
            print("Done!")
            # jumps out of the loop
            break
        elif int(num_input):
            int(num_input)
            # after converting the number to an integer it gets added to the list
            nums.append(num_input)
            print(nums)
            # looping through our list of numbers
            for num in nums:
                # we have to assign our first number to our variables so we can compare them after the first iteration
                if largest is None and smallest is None:
                    largest = num
                    smallest = num
                # for finding the largest number
                if largest<num:
                    largest = num
                # for finding the smallest number
                elif smallest>num:
                    smallest = num
    # if given input is not a number it wil give this message but also it won't break the loop
    except:
        print("Please enter a number")

print("Smallest", smallest)
print("Largest", largest)