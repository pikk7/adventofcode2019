import math

fo = open("input.txt","r")

lines=fo.readlines()


def fuel_calculation_sum(lines):
    tmp=0
    rtm=0
    for element in lines:
        tmp=fuel_element(element)
        rtm=rtm+tmp
    return rtm


def fuel_element(element):
    return math.floor(int(element)/3)-2


print(fuel_calculation_sum(lines))

def fuel_recursive(a):
    rtm=0
    a=int(a)
    while(a>0):
        a=fuel_element(a)
        if(a>0):
            rtm=rtm+a
    return rtm

def fuel_calculation_recursive_sum(lines):
    tmp=0
    rtm=0
    for element in lines:
        tmp=fuel_recursive(element)
        rtm=rtm+tmp
    return rtm

print(fuel_calculation_recursive_sum(lines))