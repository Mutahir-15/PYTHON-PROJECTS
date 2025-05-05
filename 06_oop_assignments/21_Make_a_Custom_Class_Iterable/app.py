# Assignment: Make a Custom Class Iterable

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # returns the iterator object itself

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # signals the end of iteration
        value = self.current
        self.current -= 1
        return value

# Example usage
countdown = Countdown(5)

print("Countdown:")
for number in countdown:
    print(number)

# Understaing concepts
"""
Custom Class Iterable:
1.  __iter__() returns the iterator (usually self if the class maintains state).
2.  __next__() defines what value to return each time and when to stop.
3.  When the countdown reaches below 0, StopIteration is raised automatically to stop the loop.
"""