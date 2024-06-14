from random import randint as r
while True:
    inp = input(" > ")
    if inp[0] == "c":
        print("\n"*70)
        continue
    inp = inp.split("d")
    if "+" in inp[1]:
        inp[1] = inp[1].split("+")
        inp.append(inp[1][1])
        inp[1] = inp[1][0]
    else:
        inp.append(0)
    if inp[0] != "":
        n = int(inp[0])
    else:
        n=1
    c = int(inp[2])
    for i in range(n):
        if int(inp[1]) != 20:
            c += r(1,int(inp[1]))
        else:
            a = r(0,1)
            c += r(1,int(inp[1]))+a            
    print(c)
