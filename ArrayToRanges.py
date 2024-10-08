nums = list(map(int, input().split()))

interval = []
s = ''
for i in range(len(nums)):
    if i == 0:
        s += str(nums[i])

    else:
        if nums[i] - nums[i - 1] == 1:
            if i == len(nums) - 1:
                s += '->' + str(nums[i])
                interval.append(s)

        else:
            if s != str(nums[i - 1]):
                print(s[0], str(nums[i - 1]))
                s += '->' + str(nums[i - 1])
            interval.append(s)
            s = str(nums[i])
            if i == len(nums) - 1:
                interval.append(s)

print(interval)