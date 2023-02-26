testcase = int(input())
for tst in range(testcase):
    N,D = map(int, input().split())
    integer = str(N)
    indexing = len(integer)-1
    digit = str(D)
    X = []
    power = 0
    for y in range(len(integer)):
        if integer[indexing]==digit:
            if len(integer)==1:
                N+1
                X.append(1)
            else:
                if power==0:
                    N = N + 1
                    integer = str(N)
                    X.append(1)
                    power += 1
                    indexing -= 1
                elif power==1:
                    N = N + 10
                    integer = str(N)
                    X.append(10)
                    power += 1
                    indexing -= 1
                else:  
                    ten_pow = 10**power
                    indexed_len = int(integer[indexing+1:len(integer)])
                    differ = (ten_pow) - indexed_len
                    New_ass = N + differ
                    integer = str(New_ass)
                    power += 1
                    indexing -= 1
                    X.append(differ)
        else:
            power += 1
            indexing -= 1
    print(sum(X))