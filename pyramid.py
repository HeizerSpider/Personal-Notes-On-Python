def pyramid(layers):
    for i in range(0,layers):
        space = (layers - i) * " "
        stars = i * "* "
        result = space + stars
        print(result)

if __name__ == '__main__':
    pyramid(10)