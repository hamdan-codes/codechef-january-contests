# Contributor Chaudhary Hamdan
# 30 Points

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    m = a[0]
    a = a[1:]
    neg,pos = 0,0
    for i in range(m):
        if a[i] < 0:
            neg += 1
        else:
            pos += 1
    print(neg*pos)






