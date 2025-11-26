"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""

def brute(n, t):
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            # sum of the values in two positions in n
            total = n[i]+n[j] 
            if (total) == t:
                return [i, j]

def optimized(n, t):
    dict = {}
    for i, num in enumerate(n):
        # subtracting the current number from the target to look for that instead
        # of going through the dict and finding what number sums to the target
        check = (t-num) 
        if check in dict:
            return [dict[check], i]
        dict[num] = i

def if_sorted(n, t):
    # if the list is sorted, we can just make two pointers on either side of the list,
    # and increment the start or decrement the end pointer depending on their sum
    start, end = 0, len(n)-1
    while end > start:
        s = n[end]+n[start]
        if s == t:
            return [start, end]
        # if the current sum is smaller, then we know we need to increment the start ptr, which
        # will give us a bigger sum, closer to the target
        if s < t:
            start += 1
        # if the current sum is larger, then we know we need to decrement the end ptr, which
        # will give us a smaller sum, closer to the target
        if s > t :
            end -= 1

def multiple_sol(n, t):
    # this is the same as the optimized code, however we store
    # the solutions in sols, instead of returning when we find one solution
    dict = {}
    sols = []
    for i, num in enumerate(n):
        if t-num in dict:
            sols.append([dict[t-num], i])
        dict[num] = i

    return sols


def two_sum(nums, target, func):
    # if a list of less than 2 numbers is given, than we can't get 
    # 2 numbers that sum to the target
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

