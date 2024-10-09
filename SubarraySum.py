def SubarraySumK(nums, k) -> int:
    n = 0
    sums = 0
    d = {}
    d[0] = 1

    for i in range(len(nums)):
        sums += nums[i]
        n += d.get(sums - k, 0)
        d[sums] = d.get(sums, 0) + 1

    return n