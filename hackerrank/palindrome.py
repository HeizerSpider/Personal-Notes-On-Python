#given a number, determine if the number is a palindrome (same number even when it is flipped)

def is_palindrome(number):
    n=str(number)
    result=""
    i=0
    counter=0
    while i<len(n):
        letter=n[len(n)-1-i:len(n)-i]
        result += letter
        i+=1
    result=int(result)
    print(result)
    if result==number:
        print(True)
    else:
        print(False)
    

if __name__=="__main__":
    is_palindrome(123421)