# Contributor Chaudhary Hamdan

t = int(input())
for _ in range(t):
    l = int(input())
    a = input()
    size = l//4
    for i in range(size):
        letter = a[4*i:4*i+4]
        letter = int(letter,2)
        print(chr(letter+97),end='')
    print()


