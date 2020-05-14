def main():
    even = [2,4,6,8,10,12,14,16,18]
    odds = [1,3,5,7,9,11,13,15,17]

    evenSquared = [e**2 for e in even]
    print(evenSquared)

    oddSquared = [i**2 for i in odds if i>5]
    print(oddSquared)

main()