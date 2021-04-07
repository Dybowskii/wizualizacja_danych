import itertools as it

num_iterations = int(raw_input('How many? '))
def fib():
    a,b = 0,1
    while True:
        yield a
        b = a+b
        yield b
        a = a+b

for x in it.islice(fib(), num_iterations):
    print (x)