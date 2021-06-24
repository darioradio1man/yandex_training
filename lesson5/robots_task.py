def robots(period, string):
    extra, ans = 0, 0
    for i in range(len(string) - period - 1, -1, -1):
        if string[i] == string[i + period]:
            extra += 1
        else:
            extra = 0
        ans += extra
    return ans


per = int(input())
the_str = input()
print(robots(per, the_str))
