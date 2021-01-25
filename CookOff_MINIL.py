# Contributor Chaudhary Hamdan

t = int(input())
for _ in range(t):
    n,m = [int(x) for x in input().split()]
    a = []
    for i in range(n):
        b = input()
        a.append(b)
    odd,even = 0,0
    for i in range(n):
        for j in range(m):
            if i%2==0 and j%2==0 and a[i][j]=='*':
                even += 1
            if i%2==0 and j%2==1 and a[i][j]=='.':
                even += 1
            if i%2==1 and j%2==0 and a[i][j]=='.':
                even += 1
            if i%2==1 and j%2==1 and a[i][j]=='*':
                even += 1
                
            if i%2==0 and j%2==0 and a[i][j]=='.':
                odd += 1
            if i%2==0 and j%2==1 and a[i][j]=='*':
                odd += 1
            if i%2==1 and j%2==0 and a[i][j]=='*':
                odd += 1
            if i%2==1 and j%2==1 and a[i][j]=='.':
                odd += 1
    if n%2 and m%2:
        print(odd)
    else:
        print(min(odd,even))
