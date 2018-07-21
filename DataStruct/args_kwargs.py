def my_method(arg1, arg2):
    return arg1 + arg2
my_method(5,6)

def my_long_method(arg1, arg2, arg3, arg4, arg5, arg6):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6

def my_list_addition(list_arg):
    return sum(list_arg)

my_long_method(3, 5, 7, 12, 14, 55)
my_list_addition([3, 5, 7, 12, 14, 55])

## ARGS - Unlimited numbers to be added and need for a list to pass those numbers

def addition_simplified(*args):
    return sum(args)

addition_simplified(3, 5, 7, 12, 14, 55)

##

def what_are_kwafs(*args, **kwargs):
    print(args)
    print(kwargs)

what_are_kwafs(12, 34, 56, name='Jose', location='UK')