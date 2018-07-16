#sets
my_set = {1, 3, 5}

# list within a dictionary
my_dict = {'name': 'Rick', 'age':90, 'grades': [13,45,66,90]}                   # dictionaries are keys and values set, allow to to store data
another_dict = {1 : 15, 2 : 75, 3 : 150}

# tuple within a dictionary
lottery_player = {
    'name': 'Fel',
    'numbers': (13,45,66,23,22)
}

# list of dictionaries
universities = [
    {
        'name': 'Oxford',
        'location': 'UK'
    },
    {
        'name': 'MIT',
        'location': 'US'
    }
]

# with a set, we couldn't access element number zero
# with a dictionary, we can access a specific key
sum(lottery_player['numbers'])
