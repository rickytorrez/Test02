should_continue = True
if should_continue:
    print("Hello")

known_people = ["John", "Anna", "Mary"]
person = input("Enter the person you know: ")


# format lets you substitute things on strings #
# must use greater version than python3 #
if person in known_people:
    print("You know {}!".format(person))
else:
    print("You don't know {}!".format(person))

def who_do_you_know():
    people = input ("Enter the people you know separated by commas: ")      # John,Rolf,Anna,Greg
    people_list = people.split(",")                                         # ["John","Rolf","Anna","Greg"]
    people_without_spaces = []
    for person in people_list:                                              # loop to remove spaces from names
        people_without_spaces.append(person.strip())

    return people_without_spaces

def ask_user():
    person = input ("Enter a name of someone you know: ")
    if person in who_do_you_know():                                         # Grabs the list of the method above
        print("You konw {}!".format(person))

ask_user()                                                                  # Call the method