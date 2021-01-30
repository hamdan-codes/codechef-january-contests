# Contributor Chaudhary Hamdan

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    s = sum(a)
    if s%2 == 0:
        print(1)
    else:
        print(2)
    
    
    