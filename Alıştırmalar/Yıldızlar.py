def star_triangle(rows):
    try:
        # the reason I gave +1 to the "rows" parameter is "range" keyword does not include last value as part of the iteration
        for row in range(rows+1):
            print("*" * row + "\n")
    except:
        print("Enter a number")
        return None

print("first triangle: ")
star_triangle(3)
print("second triangle: ")
star_triangle(5)