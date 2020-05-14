# import sys
# inFile = sys.argv[1]

def run():
    number = int(input())
    dict={}
    for i in range(0,number):
        a,b = input().split()
        dict[a]=b
    return dict

def check(dict):
    while True:
        try:
            name = input()
            if name in dict:
                print(name + "=" +dict[name])
            else:
                print("Not found")
        except EOFError:
            break

    
# def test(lines):
#     try:
#         number = lines
#         dict={}
#         for i in range(0,number):
#             a,b = input().split()
#             dict[a]=b
#         for i in range(0,number):
#             name = input()
#             if name in dict:
#                 print(name + "=" +dict[name])
#             else:
#                 print("Not found")
#     except RuntimeError:
#         pass
        
if __name__=='__main__':
    # with open(inFile,'r') as i:
    #     lines = i.readlines()
    #     test(lines)
    dict= run()
    check(dict)
    #on terminal run "python3 dict_run.py < dict_test.txt"

        