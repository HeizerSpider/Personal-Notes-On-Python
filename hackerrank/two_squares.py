#given middle point coordinates of 2 squares and the respective length of each sides, output code true false if the two squares overlap or not

class Coordinate():
    x=0
    y=0

s1 = Coordinate()
s1.x,s1.y = 10,10
s2 = Coordinate()
s2.x,s2.y = 20,10

def is_in_square(square1, length1, square2, length2):
    #falls within range, x-side and y-side meet
    #left or right and top or bottom
    #midpoint s2 falls within range of mid s1 plus both lengths all around
    if square1.x+length1+length2>=square2.x and square1.x-length1-length2<=square2.x and square1.y+length1+length2>=square2.y and square1.y-length1-length2<=square2.y:
        return True
    else:
        return False

if __name__=="__main__":
    print(is_in_square(s1,5,s2,4))

