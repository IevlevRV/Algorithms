n = int(input())
nums = [list(map(float, input().split())) for _ in range(n)]


def isReflected(points) -> bool:
    min_x, max_x = float('inf'), -float('inf')
    point_set = set()
    for x, y in points:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        point_set.add((x, y))
    s = min_x + max_x
    return all((s - x, y) in point_set for x, y in points)


print(isReflected(nums))