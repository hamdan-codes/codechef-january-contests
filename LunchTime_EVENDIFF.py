# Contributor Chaudhary Hamdan

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    even,odd = 0,0
    for i in range(n):
        if a[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    print(min(even,odd))
            
        
        


