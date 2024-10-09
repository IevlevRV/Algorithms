def ZigzagIterator(list1, list2) -> list:
    i, j, n1, n2 = 0, 0, len(list1), len(list2)

    while i < n1 and j < n2:
        if i > j:
            res.append(list2[j])
            j += 1
        elif i == j:
            res.append(list1[i])
            i += 1
    if i <= n1 - 1:
        res.extend(list1[i:])
    elif j <= n2 - 1:
        res.extend(list2[j:])

    return res


print(ZigzagIterator([1, 2, 3, 4], [5, 6]))
print(ZigzagIterator([1], []))