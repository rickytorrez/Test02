my_variable = "hello"

#print(my_variable[0])
#print(my_variable[1])
#print(my_variable[2])
#print(my_variable[3])
#print(my_variable[4])

print("____________________")

# same as bellow #
for character in my_variable:                                   # iterables are strings, list, sets and tuples #
    print(character)                                            # character can be called whatever you want
print("____________________")

my_list = [1,3,5,7,9]
for number in my_list:
    print(number ** 2)

print("____________________")
user_wants_number = True
while user_wants_number == True:
    print(10)

    user_input = input(" should we print again? (y/n) ")        # parameter to the input method #
    if user_input == 'n':
        user_wants_number = False