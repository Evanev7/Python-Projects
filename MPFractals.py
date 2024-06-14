from numba import jit
import numpy as np
import cmath
import multiprocessing as mp

#Error Handling
class BadPoly(Exception):
    pass

class BadTrig(Exception):
    pass

class BadExpo(Exception):
    pass

class NoChainRule(Exception):
    pass

class NotAFunction(Exception):
    pass

#Differentiate polynomials
def poly(fun, x="x"):
    try:
        try:
            complex(fun)
            return "0"
        except:
            pass
        scal, exp = fun.split(x)
        
        #Handle missing numbers/powers
        if scal == '':
            scal = 1
        elif not scal[-1].isdigit():
            scal += "1"
        if exp == "":
            exp = 1
        else:
            exp = exp[1:]
        
        #d/dx(x^n) = nx^(n-1)
        scal = complex(scal) * complex(exp)
        exp = complex(exp) - 1
        
        #Cleaned up output
        if scal == 0:
            return "0"
        elif exp == 1:
            return "" + str(scal) + x
        elif exp != 0:
            return "" + str(scal) + x + "^" + str(exp)
        else:
            return "" + str(scal)
    except:
        raise BadPoly("Not A Polynomial")

#Differentiate cos, sin
def trig(fun, x="x"):
    try:
        if fun == "sin("+x+")" or fun == "sin"+x:
            return "cos("+x+")"
        elif fun == "cos("+x+")" or fun == "cos"+x:
            return "-sin("+x+")"
        elif fun == "-sin("+x+")" or fun == "-sin"+x:
            return "-cos("+x+")"
        elif fun ==  "-cos("+x+")" or fun == "-cos"+x:
            return "sin("+x+")"
        raise Exception("No cos? NO CAUSE! YOU ARE NOT A KNIGHT!")
    except:
        raise BadTrig("Sumptin streeenge here wif da twigs")

#Differentiate exponentials
def expo(fun, x="x"):
    try:
        base, exp = fun.split("^")
        if exp != x:
            raise NoChainRule("Wheres the chain rule\nhurry up and implement it you lasy fug")
            #return chain("".join(fun.split("^").append(")").insert(1,"(")),x=x)
        #Error handling
        try:
            complex(base)
        except ValueError:
            raise NoChainRule("Chain rule plox")
            #return chain(fun,x=x)
        if float(base) < 0:
            raise Exception("NOHW NEGATIVE LOWGS")
        if complex(base) == 0:
            return "0"
        #Cleaned up output
        base = np.log(complex(base))
        if base == 1:
            return ""+fun
        elif base != 0:
            return "" + str(base)+"*"+fun
        else:
            return "0"
    except TypeError:
        raise BadExpo("exp crashed yo")

#Product rule
def product(f,g):
    msg = ""
    aig = True
    big = True
    if f == "": f = "1.0"
    if g == "": g = "1.0"
    try:
        if complex(ddx(f)) == 0: aig = False
    except: pass
    try:
        if complex(g) == 0: aig = False
    except: pass
    try:
        if complex(f) == 0: big = False
    except: pass
    try:
        if complex(ddx(g)) == 0: big = False
    except: pass
    if aig == True:
        msg += "("+ddx(f)+")*("+g+")"
    if aig and big:
        msg += "+"
    if big == True:
        msg += "("+f+")*("+ddx(g)+")"
    if msg ==  "":
        msg += "0"
    return msg

#Quotient rule
def quotient(f,g):
    try:
        if complex(g) == 0:
            raise ZeroDivisionError
    except: pass
    msg = ""
    aig = True
    big = True
    try:
        if complex(ddx(f)) == 0: aig = False
    except: pass
    try:
        if complex(g) == 0: aig = False
    except: pass
    try:
        if complex(f) == 0: big = False
    except: pass
    try:
        if complex(ddx(g)) == 0: big = False
    except: pass
    if aig == True:
        msg += "("+ddx(f)+")*("+g+")"
    if big == True:
        msg += "-("+f+")*("+ddx(g)+")"
    if aig == False and big == False:
        msg += "0"
    else:
        msg = "("+msg+")/(("+g+")^2)"
    return msg

#Get the "bottom layer" of the function
def bottomLayer(fun, x="x"):
    #Arrange brackets by height
    bC = 0
    obC = bC
    words = [[]]*len(fun)
    for i in range(len(fun)):
        obC = bC
        if fun[i] == "(":
            bC += 1
        elif fun[i] == ")":
            bC -= 1
        words[i] = [min(bC,obC), max(bC,obC), fun[i]]
        
    #Transform the list
    words = [i for i in zip(*words)]
    
    return words

#Chain rule
def chain(fun, x="x"):
    words = bottomLayer(fun, x=x)
    
    #Get the outermost layer and the next layer
    inner = ""
    outer = ""
    for i in range(len(words[0])):
        if words[0][i] > 0:
            inner += words[2][i]
        if words[1][i] == 0:
            outer += words[2][i]
        elif words[0][i] == 0:
            if words[2][i] == ")":
                outer += x
    
    if outer == x:
        return ddx(inner)
    
    #Actual chain bit
    return "("+ddx(outer).replace(x,"("+inner+")")+")*("+ddx(inner)+")"

#Split up outermost layer by symbol
def split(fun, searchterm):
    sec = []
    lasti = 0
    words = bottomLayer(fun)
    for i in range(len(words[0])):
        if words[2][i] == searchterm and words[1][i] == 0:
            sec.append("".join(words[2][lasti:i]))
            lasti = i+1
    sec.append("".join(words[2][lasti:]))
    return sec

#Main Derivative Function
def ddx(fun,x="x"):
    #Setup
    fun = "".join(fun.split())
    polyFail = trigFail = expoFail = True
    
    #Formatting handler of extra 0s and e/pi
    def ret(x):
        x = x.replace("+0+", "+")
        if x[-2:] == "+0":
            x = x[:-2]
        if x[:2] == "0+":
            x = x[2:]
        return x
    
    words = bottomLayer(fun, x=x)
    
    #Get the outermost layer and the next layer
    inner = ""
    outer = ""
    for i in range(len(words[0])):
        if words[0][i] > 0:
            inner += words[2][i]
        if words[1][i] == 0:
            outer += words[2][i]
        elif words[0][i] == 0:
            if words[2][i] == ")":
                outer += x
    
    #Distribute over additives
    if "+" in outer:
        return ret("+".join([ddx(i) for i in split(fun,"+")]))
    
    #Distribute over products
    if "*" in outer:
        f = "".join(split(fun,"*")[0])
        g = "*".join(split(fun,"*")[1:])
        return ret(product(f,g))
    
    #Distribute over division
    if "/" in outer:
        f = "".join(split(fun,"/")[0])
        g = "/".join(split(fun,"/")[1:])
        return ret(quotient(f,g))
    
    #Distribute over brackets
    if "(" in fun:
        return ret(chain(fun))
    
    #Handle Polynomials
    try:
        return ret(poly(fun))
    except BadPoly:
        polyFail = False
    
    #Handle trigonometric functions
    try:
        return ret(trig(fun))
    except BadTrig:
        trigFail = False
    
    #Handle exponentiation
    try:
        return ret(expo(fun))
    except BadExpo:
        expoFail = False
    
    raise NotAFunction(fun)

#Clean up outputs to allow  mathematical evaluation with numexpr
def handler(fun):
    fun=fun.replace(")(", ")*(")
    fun=fun.replace("x(", "x*(")
    fun=fun.replace(")x",")*x")
    fun=fun.replace("^", "**")
    fun=fun.replace("sin", "NPSIN")
    fun=fun.replace("cos", "NPCOS")
    return fun

#Evaluate a function at a point
import numexpr
@jit
def evaluate(fun,val,x="x"):
    fun = handler(fun)
    fun = fun.replace(x,str(val))
    fun = fun.replace("NPSIN", "np.sin")
    fun = fun.replace("NPCOS", "np.cos")
    return eval(fun)

#f(x)/f'(x)
rap = lambda x: handler("("+x+")/("+ddx(x)+")")

#Iterate through the Newton-Raphson formula to find a root
@jit
def getRoot(itr,fun,val,a=1,x="x"):
    if cRound(val,3) == 0:
        return "False"
    for i in range(itr):
        val = val - a*evaluate(fun,val)
    return complex(val.real, val.imag%2*np.pi)

from matplotlib import pyplot as plt
from time import time

#Complex Rounding Function
def cRound(num,det):
    return complex(round(num.real,det),round(num.imag,det))

#Test a point to and return its Newton Fractal

def testPoints(fun,a,detail,itr,area):
    rfun = rap(fun)
    pts = []
    dst = [area[1][0] - area[0][0], area[1][1] - area[0][1]]
    for x in range(detail+1):
        for y in range(detail+1):
            pts.append([0,0,0])
            pts[-1][0] = area[0][0] + x * dst[0] / detail
            pts[-1][1] = area[0][1] + y * dst[1] / detail
            if pts[-1][0] != 0 or pts[-1][1] != 0:
                try:
                    pts[-1][2] = getRoot(itr, rfun, complex(pts[-1][0], pts[-1][1]), a=a)
                except OverflowError:
                    pts[-1][2] = "False"
    return pts, dst

#Main Program for drawing newton fractals
def draw(fun, a=1, detail=100, itr=100, area = [[-5,-5],[5,5]]):
    t=time()
    
    pts, dst = testPoints(fun,a,detail,itr,area)
            
    x,y,c=[i for i in zip(*pts)]
    cs = []
    
    #Basic Basin Colouring
    #print(list(set([cRound(i,3) for i in c if i != "False"])))
    #colourmap = {complex(1,0):(1,0,0), complex(-.5,.866):(0,0,1), complex(-.5,-.866):(0,1,0), "False":(.8,.8,.8)}
    #for i in c:
    #    try:
    #        cs.append(colourmap[cRound(i,3)])
    #    except:
    #        cs.append(colourmap["False"])
    
    #Argument Colouring
    #for i in c:
    #    v = (cmath.phase(i)/np.pi)
    #    if v > 0:
    #        cs.append((v,1-v,0))
    #    else:
    #        cs.append((0,1+v,-v))
    
    #Updated Basin Colouring
    cols = list(set([cRound(i,5) for i in c if i != "False"]))
    if len(cols) == 1:
        print("Only one root reached;",cols[0])
        width = [0]
    else:
        width = [2*i/(len(cols)-1)-1 for i in range(len(cols)) if i != "False"]
    for i in c:
        if i != "False":
            v = width[cols.index(cRound(i,5))]
            if v > 0:
                cs.append((v,1-v,0))
            else:
                cs.append((0,1+v,-v))
        else:
            cs.append((0.6,0.6,0.6))
    
    print(time() - t)
    fig = plt.figure(figsize=[15,15*dst[1]/dst[0]])
    plt.axis('equal')
    ax = fig.gca()
    ax.scatter(x,y,marker=',', c=cs)
    plt.show()
    print(time()-t)
    return x,y,cols,width,cs,c,pts
    
dat=draw("x^5+-10".replace("e",str(np.e))+"+-2", 1, 100, 50, [[-1,-1],[1,1]])
