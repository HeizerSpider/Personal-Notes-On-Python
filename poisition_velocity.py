#input is initial velocity and time, return displacement and velocity

from math import pow

def position_velocity(v, t):
    g = 9.81
    y = round(v*t - 0.5*g*pow(t,2),2)
    yprime = round(v - g*t, 3)
    return print(y,yprime)

if __name__=="__main__":
    position_velocity(5,10)

#concepts/lessons: operators, import pow, round