my_list = [0,1,2,3,4]
an_equal_list = [x for x in range(5)]                                           # Same as above [0,1,2,3,4]

multiply_list = [x * 3 for x in range(5)]
print(multiply_list)                                                            # [0,3,6,9,12]

print(8 % 3)                                                                    # 8 / 3 == 6r2, so 8 % 3 == 2

print(9 % 2)                                                                    # use modulo 2 to find out if a number is odd or even
                                                                                    # 4 % 2 = 0
                                                                                    # 5 % 2 = 1
                                                
print([n for n in range(10) if n % 2 == 0])                                     # [0,2,4,6,8]
                                                                                # for number less than 10 divisible by 2

people_you_know = ["Rolf", "John", "anna", "GREG"]
normalised_people = [person.strip().lower() for person in people_you_know]

print("_____________________")
print(normalised_people)                                                        # ['rolf', 'john', 'anna', 'greg']