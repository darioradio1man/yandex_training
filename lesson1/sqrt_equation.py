def sqrt_equation_sol(a, b, c):
    if c < 0 or (a == 0 and b != c ** 2):
        return 'NO SOLUTION'
    if (a == b == c == 0) or (a == 0 and b == c ** 2):
        return 'MANY SOLUTIONS'
    if (c ** 2 - b) % a == 0:
        return str(int((c ** 2 - b) / a))
    else:
        return 'NO SOLUTION'


a1, b1, c1 = int(input()), \
          int(input()), \
          int(input())
print(sqrt_equation_sol(a1, b1, c1))
