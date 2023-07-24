import lesson4 as sort

def binary_search(args, target):
    args = sort.sort(args)
    left = 0
    right = len(args) - 1
    while left <= right:
        middle = (left + right) // 2
        if args[middle] == target:
            return True
        if args[middle] < target:
            return binary_search(args[middle+1:], target)
        else:
            return binary_search(args[:middle], target)
    return False
    
result = binary_search([1, 2, 4, 3], 3)

if result:
    print("Found!")
else: print("Not found!")    