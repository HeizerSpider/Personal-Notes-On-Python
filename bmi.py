#takes weight and height as input (kg, cm respectively)

from math import pow

def bmi_calculator(w,h):
    hm=h/100 #height in meters
    bmi = w/(pow(hm,2))
    return round(bmi,1)

def bmi_classifier(bmi):
    if bmi<18.5:
        print("nutritional deficiency")
    elif bmi<23 and bmi>=18.5:
        print("low risk")
    elif bmi<27.5 and bmi>=23:
        print("moderate risk")
    elif bmi>=27.5:
        print("high risk")

if __name__=="__main__":
    result = bmi_calculator(95.5,180)
    print(result)
    bmi_classifier(result)