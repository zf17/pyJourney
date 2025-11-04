def brute(n, t):
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if (n[i]+n[j]) == t:
                return [i, j]

def optimized(n, t):
    dict = {}
    for i, num in enumerate(n):
        if t-num in dict:
            return [dict[t-num], i]
        dict[num] = i

def if_sorted(n, t):
    start, end = 0, len(n)-1
    while end > start:
        s = n[end]+n[start]
        if s == t:
            return [start, end]
        if s < t:
            start += 1
        if s > t :
            end -= 1

def multiple_sol(n, t):
    dict = {}
    sols = []
    for i, num in enumerate(n):
        if t-num in dict:
            sols.append([dict[t-num], i])
        dict[num] = i

    return sols


def two_sum(nums, target, func):
    if len(nums) < 2:
        return None
    if func == "brute":
        return brute(nums, target)
    elif func == "optimized":
        return optimized(nums, target)
    elif func == "if_sorted":
        return if_sorted(nums, target)
    elif func == "multiple_sol":
        return multiple_sol(nums, target)


def main():
    nums = [1, 2, 3, 4, 5, 6]
    target = 5
    func = "multiple_sol"
    print(two_sum(nums, target, func))


if __name__ == "__main__":
    main()