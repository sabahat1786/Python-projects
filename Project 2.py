def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Take array input from user
arr = list(map(int, input("Enter space separated integers: ").split()))

# Ask for index value to search
target = int(input("Enter the value to search: "))
