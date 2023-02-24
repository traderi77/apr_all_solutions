def max_sum_sequence(nums):

    if not nums:
        return 0

    running_sum = max_sum = nums[0]

    for i in nums[1:]:
        running_sum = max(i, running_sum + i)
        max_sum = max(max_sum, running_sum)

    return max_sum

print(max_sum_sequence([31, -41, 59, 26, -53, 58, 97, -93, -23]))
# runtime O(n)n space O(1)
