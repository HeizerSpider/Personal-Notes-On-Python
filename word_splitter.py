def splitter(word):
    even = ""
    odd = ""
    if(word.isdigit()==False):
        for i in range(0, len(word)):
            if i%2==0:
                even += word[i]
            else:
                odd += word[i]
        print(even + " " + odd)

if __name__=='__main__':
    while True:
        try:
            word = input()
            splitter(word)
        except EOFError:
            break