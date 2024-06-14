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
        c += r(1,int(inp[1]))
    print(c)
    def stuff(f):
        f()
    stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(stuff(print("hi"))))))))))))))))))))))))))))))))))))))))
