T = int(input())
for test_case in range(1, T + 1):
    result=0
    N,M = map(int,input().split())
    n = sorted(list(map(int,input().split())))
    m= sorted(list(map(int,input().split())),reverse=True)
    print(m,n)
    for truck in m:
        if len(n)==0:
            break
        if truck>=n[-1]:
            print(truck,n[-1])
            result+=n[-1]
            n.pop()
        else:
            while truck<n[-1]:
                n.pop()
                if len(n)==0:
                    break
       
            continue
    print("#%d %d"%(test_case,result))
            
