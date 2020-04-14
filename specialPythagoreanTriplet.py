sum_of_sides = 1000
# white space
# white space
for a in range(1,sum_of_sides):                                     # Finding a, b and c using nested for loops
    # white space
    for b in range(a+1,sum_of_sides):
        # whitespace
        for c in range(b+1,sum_of_sides):
            # white space
            if c**2 == a**2 + b**2 and a + b + c == 1000:           # constraint, check for solution
                print(a, b, c)                                      # print values that add up to 1000
                print(a * b * c)                                    # print solution
                quit()                                              # it doesnt stop on its own 


