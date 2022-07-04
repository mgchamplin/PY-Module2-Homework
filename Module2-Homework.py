# Return the largest of any number of integers (include the required 3 for ths assignment)

def max_num( *args ):
    max = 0;
    for i in args:
        if (i > max): max = i
    return max

print("Max of 1, 15,7 is",max_num(1,15,7))
print("Max of 5, 1, 9 is",max_num(5,1,9))
print("Max of 15,10,3 is",max_num(15,10,3))
print("")

# Return the results of all numbers multiplied in a list

def mult_list (num_list):
    if (len(num_list) == 0): return 0

    result = 1
    for i in num_list:
        result *= i
    return result

print("Multipying 2,3,4 is",mult_list([2,3,4]))
print("Multipying 54 by 1 is",mult_list([54]))
print("Multipying 5,10,10 is",mult_list([5,10,10]))
print("")


# Return a string reversed

def rev_string(str):
    return str[::-1]

print("Hello reversed is:",rev_string("Hello"))
print("XYZ reversed is:",rev_string("XYZ"))
print("Python reversed is:",rev_string("Python"))
print("")


# Return true/false if the first arg falls within the range of the second two args

def num_within(mid, low, high):
    if (low > high):
        return "Error 2nd arg must be less than 3rd arg"
    return (low <= mid and mid <= high)

print("Is 7 within 3 and 8? ",num_within(7,3,8))
print("Is 9 within 15 and 80? ",num_within(9,15,80))
print("Is 3 within 20 and 1? ",num_within(3,20,1))
print("")

 # print out Pascals triangle for n-rows

def pascal(n):

    print("Pascal Triangle for",n,"rows:")

    row = []
    prev_row = []

    prev_row.append(1)
    prev_row.append(1)

    # Not valid
    if (n <= 0): return

    # The two base cases n=1, and n=2.  Just print out the 1s
    print("1")
    if (n == 1):
        return

    print("1  1")
    if (n == 2):
        return

    current_row_len = 2

    # Do for each row after the second row.....
    for j in range (2,n):

        # build the new row 
        row.append(1)
        print("1", end = "")

        # perform the pascal math and continue building the row
        for i in range (1, current_row_len):
            pascal_num = prev_row[i-1] + prev_row[i] 
            print(" ",pascal_num, end = "")
            row.append(pascal_num)

        # close out the row
        row.append(1)
        print("  1")

        # save current row to be used as prev row on the next iteration
        prev_row = row
        row = []

        current_row_len += 1

    return

pascal(6)
print("")
pascal(10)


