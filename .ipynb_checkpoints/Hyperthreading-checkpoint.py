from multiprocessing import Pool, TimeoutError
from time import time

def f(x):
    y=0
    for i in range(10000000):
        y += x
    return y

def main():
    with Pool(processes = 4) as pool:
        try:
            t=time()
            r = pool.starmap_async(f, [(3,)]*10)
            print(r.get())
            print(round(time()-t,3))
        except TimeoutError as e:
            print(e)
        
    

if __name__ == '__main__':
    __spec__ = None
    t=time()
    print([f(3) for i in range(10)])
    print(round(time()-t,3))
    main()
