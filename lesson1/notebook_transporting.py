def area_of_notebook_transfering(a1, a2, b1, b2):
    slots = []
    dim1 = max(a2, b1) * (a1 + b2)
    slots.append([max(a2, b1), a1 + b2])
    dim2 = max(a2, b2) * (a1 + b1)
    slots.append([max(a2, b2), a1 + b1])
    dim3 = max(a1, b2) * (a2 + b1)
    slots.append([max(a1, b2), a2 + b1])
    dim4 = max(a1, b1) * (a2 + b2)
    slots.append([max(a1, b1), a2 + b2])
    min_sq = min(dim1, dim2, dim3, dim4)
    for i, num in enumerate([dim1, dim2, dim3, dim4]):
        if num == min_sq:
            print(slots[i][0], slots[i][1])
            break


a1t, a2t, b1t, b2t = map(int, input().split())
area_of_notebook_transfering(a1t, a2t, b1t, b2t)
