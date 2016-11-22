import timeit

def main():
    time1 = timeit.timeit('sumSeq(1000)','from __main__ import sumSeq',
                          number=10000)
    time2 = timeit.timeit('sumSeq2(1000)','from __main__ import sumSeq2',
                          number=10000)
    
    print(time1, time2, (time2-time1)/time2)

def sumSeq(n):
    add = 0
    for i in range(n+1):
        add += i

def sumSeq2(n):
    add = 0
    while (n > 0):
        add += n
        n = n -1

if __name__ == "__main__":
    main()
