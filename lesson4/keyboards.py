n = int(input())
strength_of_key = list(map(int, input().split()))

k = int(input())
press_nums = list(map(int, input().split()))

for one_press in press_nums:
    strength_of_key[one_press - 1] -= 1

for strength in strength_of_key:
    print("YES" if strength < 0 else "NO")
