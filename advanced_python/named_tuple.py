import collections

def main():
    Point = collections.namedtuple("Hello", "x y z")
    p1 = Point(11, 12, 13)
    p2 = Point(10, 20, 30)
    print(p1,p2)
    print(p1.x, p2.z)

if __name__=="__main__":
    main()