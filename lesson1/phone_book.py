def reformat(num: str) -> str:
    num = num.replace('-', '').replace('(', '').replace(')', '')
    return num[-10:] if len(num) > 7 else '495' + num[-7:]


counts = 4
the_nums = [input() for _ in range(counts)]
for x in the_nums[1:]:
    print("YES" if reformat(the_nums[0]) == reformat(x) else "NO")
