def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1

def permutations(string):
    dupes = {}
    for i in string:
        if i in dupes.keys():
            dupes[i] += 1
        else:
            dupes[i]  = 1
    product = 1
    for i in dupes.values():
        product *= factorial(i)
    return factorial(len(string)) / product

def doMechanics(e,h):
    v = (2*9.8*h)**.5
    n=0
    while h > 0.05:
        v *= e
        h = v**2/19.6
        n += 1
    return n

if False:
    while True:
        a = input(" > ")
        if a == "":
            break
        else:
            print(permutations(a))

if True:
    while True:
        a = input(" > ")
        if a == "":
            break
        else:
            print(doMechanics(float(a.split()[0]), float(a.split()[1])))


