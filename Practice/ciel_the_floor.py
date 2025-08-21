nums = [3, 4, 4, 4, 8, 8, 9, 10, 12, 14, 15]

def ceil_floor(nums, target):
    low, high = 0, len(nums) - 1
    floor, ceil = -1, -1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return [nums[mid], nums[mid]]

        elif nums[mid] < target:
            floor = nums[mid]   # candidate for floor
            low = mid + 1
        else:
            ceil = nums[mid]    # candidate for ceil
            high = mid - 1

    return [floor, ceil]


k = int(input("Enter a value: "))
result = ceil_floor(nums, k)
print('-----------------------------------------------')
print("List :", nums)
print("-----------------------------------------------")
print(f"Floor and Ceil value of {k} : {result}")
