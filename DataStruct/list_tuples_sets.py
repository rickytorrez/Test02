my_variable = "hello"

# LIST TUPLES AND SETS #

grade_one = 77
grade_two = 80
grade_three = 90
grade_four = 95
grade_five = 100
# same as below #

gradesList  = [77, 80, 90, 95, 100]                 ## LIST     - Most flexible of them all
                                                    ##          * Always ordered in the way we put elements in
gradesTuple = (77, 80, 90, 95, 100)                 ## TUPLE    - Immutable, we cannot increase its size            
                                                    ##          * Use when there's no need to remove or add elements
setGrades   = {77, 80, 90, 95, 100}                 ## SET      - Unique and unordered, values cannot be repeated  

# increase the size of a list #
gradesList.append(108)
print(gradesList)

# we can not increase the size of a tupe but we can add to it #
# you must have a comma at the end #
gradesTuple = gradesTuple + (100,)
print(gradesTuple)

# changing the value of an index in a list #
gradesList[0] = 60
print(gradesList)

# we cannot change the value of a particular index on a tuple because they're inmutable #
# we cannot change the value of a particular index on a set because they are unordered #

# however, we can add variables to a set #
setGrades.add(89)
print(setGrades) 


# SET OF OPERATIONS # 
print("___________________________")
print("SET OF OPERATIONS")
print("___________________________")

your_lottery_numbers = {1,2,3,4,5}
winning_numbers = {1,3,5,7,9,11}

# how to check if these numbers match #

# intersection prints the numbers that are in the first and second set # 
print(your_lottery_numbers.intersection(winning_numbers))
#  set([1, 3, 5])   #

# union combines both sets # 
print(your_lottery_numbers.union(winning_numbers))
#  set([1, 2, 3, 4, 5, 7, 9, 11])  #

# diference prints the numbes that are different #
print({1,2,3,4}.difference({1,2}))
#  set([3, 4])  #
