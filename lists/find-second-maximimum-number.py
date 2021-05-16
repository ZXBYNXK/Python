# ZXBYNXK
# Python3
# Run: py ./find-second-maximum-number.py

# Problem:
#   Find the second maximum number from an array of int, requires input 
#   Input 1: Number of elements (6)
#   Input 2: Numbers (123456) 
#   Output: Second maximimum (5)

# Input number of elements in list
nunmber_of_el = int(input("Qty of number elements: "))

# Generate a list from input usin map()
array = map(int, input("Insert number elements (Ex 1234...):").split())

# Make use of set to get rid of duplicates then convert set to list
array = list(set(array))

# Use max(<list>) and assign it as the maximimum number in the array variable
max_num = max(array)

# Remove the current maximimum number "max_num" using List.remove(<element>)
array.remove(max_num)

# Since the above removed the maximimum number the next value from max() will be the 
# second maximum number aka the new maximum number
second_max_number = max(array)

# Print the second maximum value from the original input  
print(second_max_number)