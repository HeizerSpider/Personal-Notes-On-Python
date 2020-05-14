from collections import Counter

def main():
    class1 = ["Ali", "Amanda", "Alice", "Justin", "Amanda", "Daryll", "Justin"]
    class2 = ["Ahmad", "Cheryl", "Alice", "Cheryl", "Amanda", "Daryll", "James"]

    c1 = Counter(class1)
    c2 = Counter(class2)

    print(c1["Ali"])

    print(c1.values())
    print(sum(c1.values()),  " students in the class")

    c1.update(class2)
    print(sum(c1.values()),  " students in the class")

    c1.subtract(class2)
    print(sum(c1.values()),  " students in the class")

    print(c1.most_common(3))#top 3 most common names

    print(c1 & c2)
    print(c1 or c2)

main()