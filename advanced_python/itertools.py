import itertools

#infinte iterators

#cycle iterator
seq = ["Iman", "Nurul", "Pichu", "Snorlax"]
cycle1 = itertools.cycle(seq)

print(next(cycle1))
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))

#count iterator
count1 = itertools.count(100, 10)

counter_list = []
for i in range(10):
    a = next(count1)
    counter_list.append(a)

print(counter_list)

print(next(count1))
print(next(count1))

#accumulator tool to add up the previous numbers
vals = [10, 20, 30, 40, 50]
acc = itertools.accumulate(vals)
print(list(acc))

#chaining tool
x = itertools.chain("ABCD", "1234", "a")
print(list(x))

#dropwhile and takewhile
def testFunction(x):
    return x < 40

vals = [15, 5, 42, 53, 50, 6, 55]

#dropwhile will 'drop' values if the function retruns true
print(list(itertools.dropwhile(testFunction, vals)))
#takewhile is the opposite, where it takes the value if the testfunction returns true
print(list(itertools.takewhile(testFunction, vals)))

#try the rest here
#https://docs.python.org/2/library/itertools.html