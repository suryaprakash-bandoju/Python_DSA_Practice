def maxSubArraySum(arr):
    ##########################################################################
    # Brute Force
    ##########################################################################
    # n = len(arr)
    # maxi = float('-inf')
    # for i in range(n):
    #     for j in range(i, n):
    #         total = 0
    #         for k in range(i,j):
    #             total += arr[k]
    #             maxi = max(maxi, total)
    # return maxi
    
    ##########################################################################
    # Better
    ##########################################################################
    # n = len(arr)
    # maxi = float('-inf')
    # for i in range(n):
    #     total = 0
    #     for j in range(i,n):
    #         total += arr[j]
    #         maxi = max(maxi, total)
    # return maxi
    
    ##########################################################################
    #Optimal-Kadane's Algorithm
    ##########################################################################
    max_sum = arr[0]
    current_sum = arr[0]
    
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum
    
arr = [2, 3, 5, -2, 7, -4]
print(maxSubArraySum(arr))
