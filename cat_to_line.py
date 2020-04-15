import sys

def catter():

    inFile = sys.argv[1]
    outFile = sys.argv[2]
    with open(inFile,'r') as i:
        lines = i.readlines()

    processedLines= lines+["HELLOOOOO"]

    with open(outFile,'w') as o:
        for line in processedLines:
            o.write(line)

if __name__ =='__main__':
    catter()