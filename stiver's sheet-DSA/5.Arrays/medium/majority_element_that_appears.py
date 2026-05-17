def majorityElement(arr):
    # Brute Force
    ###########################################################################
    # n = len(arr)
    # for i in range(n):
    #     count = 0
    #     for j in range(n):
    #         if arr[j] == arr[i]:
    #             count += 1
    #     if count > n//2:
    #         return arr[i]

    # Better-Hash Map
    ###########################################################################
    # freq = {}
    # n = len(arr)
    # for num in arr:
    #     freq[num] = freq.get(num,0) + 1
    #     if freq[num] > n//2:
    #         return num
    ###########################################################################
    # Optimal-Moore Voting Algorithm
    candidate = None
    count = 0
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
        return candidate
    ###########################################################################
    return -1

arr = [2,2,3,3,1,2,2]
print(majorityElement(arr))
