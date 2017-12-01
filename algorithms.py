from math import sqrt

###returns the greates common divisior
def gcd(num1, num2, show = False):
    if num1 == num2:
        return num1
    if num1 == 0:
        return 0
    if num2 == 0:
        return 0
    a = num1 if num1 > num2 else num2
    b = num1 if num1 < num2 else num2
    while not b == 0:
        h = a % b
        if show:
            print("%i mod %i = %i" % (a, b, h))
        a = b
        b = h
    return a

###returns the least common multiple
def lcm(num1, num2):
    return abs(num1 * num2)/gcd(num1, num2)

##returns the euclidean distance between two points in 2 or 3 dimensions
def distance(p1, p2):
    if len(p1) == len(p2):
        if len(p1) == 1:
            return p1[0]-p2[0]
        if len(p1) == 2:
            return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
        if len(p1) == 3:
            return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2] - p2[2])**2)
    raise Exception('Invalid Arguments')

def chain(points):
    sum = 0
    for i in range(len(points)-1):
        sum += distance(points[i], points[i+1])
    return sum
