from math import *

def commodityprice(price,variance,time,Variable):
    pricez = price * exp(-.5 * variance * time + sqrt(variance) * sqrt(time) * Variable)
    return print(pricez)

print(commodityprice(11,.01,1,2))
