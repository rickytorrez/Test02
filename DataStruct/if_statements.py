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