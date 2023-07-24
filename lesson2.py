import lesson4 as sort

def binary_search(args, target):
    if len(args) == 0:
        return -1
    else:
        args = sort.sort(args)
        left = 0
        right = len(args) - 1
        while left <= right:
            middle = (left + right) // 2
            if args[middle] == target:
                return True
            if args[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return False
    
result = binary_search([3, 2, 5, 1, 8, 6, 9], 30)

if result == -1:
    print("Array length cannot be zero")
else: 
    if result:
        print("Found!")
    else: print("Not found!")    