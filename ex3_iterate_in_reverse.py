a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)


# Print a file backwards
f = ['a','b','c']
for line in reversed(list(f)):
    print(line, end='')

class Countdown(object):
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

# Create a instance of the Countdown Class.
c = Countdown(11)
print(c.__iter__())
print(c.__reversed__())

# Expouse the values from the generator on a iteration and backwords.
print(list(c.__iter__()))
print(list(c.__reversed__()))