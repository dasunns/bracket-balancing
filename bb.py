print("Hello")
print("hello world")
#function to print fibinnacci series
def print_fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return print_fib(x-1) + print_fib(x-2)

print(print_fib(3))