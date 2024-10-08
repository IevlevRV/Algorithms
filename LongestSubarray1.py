def LongestSubarray(nums) -> int:
    max_len = 0
    new_len = 0
    prev_len = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            new_len += 1
            prev_len += 1
        else:
            max_len = max(max_len, prev_len)
            prev_len = new_len
            new_len = 0

    if max_len < len(nums) - 1:
        return max_len
    else:
        return max_len - 1


n = int(input())
nums = list(map(int, input().split())) + [0]
print(LongestSubarray(nums))