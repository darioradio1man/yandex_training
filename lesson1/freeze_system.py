def freeze_system(room_t, cond_t, mode_off):
    if mode_off == 'heat':
        return max(room_t, cond_t)
    elif mode_off == 'freeze':
        return min(room_t, cond_t)
    elif mode_off == 'auto':
        return cond_t
    elif mode_off == 'fan':
        return room_t


troom, tcond = map(int, input().split())
mode = input()
print(freeze_system(troom, tcond, mode))
