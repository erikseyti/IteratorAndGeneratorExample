# declaracao de um generator
def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


l = frange(100, 200, 1)
print(l)
# print(dir(limite))

# iterar um generator
for n in frange(0, 4, 0.5):
    print(n)

# convertendo o generator em lista
limite = list(frange(0, 1, 0.125))
print(limite)

def countdown(n):
    print('Starting to count from', n)
    while n > 0:
        print('Current generator number', n)
        yield n
        n -= 1
    print('Done!')

# Create the generator, notice no output appears
c = countdown(3)
# Run to first yield and emit a value
next(c)
# Run to the next yield
next(c)
# Run to next yield
next(c)
# Run to next yield (iteration stops)
# next(c)
# prints Done! on this iteration!