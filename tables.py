###outputs an multiplication table of a given Integer
def mtable(n):
    rtup = tuple(range(n))
    l1 = " * |" + n*" [%i]"
    print(l1 % rtup)
    print(((n+1)*4)*"=")
    for line in range(n):
        text = ("[%i]|" % line) + " [%i]"*n
        print(text % tuple((line*i)%n for i in rtup))

###outputs an addition table of a given Integer
def atable(n):
    rtup = tuple(range(n))
    l1 = " + |" + n*" [%i]"
    print(l1 % rtup)
    print(((n+1)*4)*"=")
    for line in range(n):
        text = ("[%i]|" % line) + " [%i]"*n
        print(text % tuple((line+i)%n for i in rtup))
