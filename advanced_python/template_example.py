from string import Template

def main():
    str1 = "This is {0} from {1}".format("Iman", "Singapore")
    print(str1)

    templ = Template("This is ${name} from ${country}")

    str2 = templ.substitute(name = "Nurul", country = "Singapore")
    print(str2)

    #using a dictionary
    data = (
        {
            "name" : "Pikachu",
            "country" : "Johto"
            # "random" : "unknown"
        },
        {
            "name" : "Ho-Oh",
            "country" : "Kanto"
        }
    )

    str3 = templ.substitute(data[0])
    print(str3)
    str4 = templ.substitute(data[1])
    print(str4)

if __name__=="__main__":
    main()