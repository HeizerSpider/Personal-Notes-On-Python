from collections import defaultdict

def dd():
    fruits = ['apple', 'pear', 'peach', 'apple', 'peach', 'mango'] 
    fruit_dict = defaultdict(lambda: 100)

    for i in fruits:
        fruit_dict[i]+=1

    for (i,j) in fruit_dict.items():
        print(i + ':' + str(j))

dd()