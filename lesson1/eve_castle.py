a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a <= d and b <= e or a <= e and b <= d:
    print("YES")
elif a <= d and c <= e or c <= d and a <= e:
    print("YES")
elif c <= d and b <= e or b <= d and c <= e:
    print("YES")
else:
    print("NO")
