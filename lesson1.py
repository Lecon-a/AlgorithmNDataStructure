def linear_search(args, target):
    if len(args) == 0:
        return -1
    else:
        return target in args
        # for value in args:
        #     if value == target:
        #         return True
        # return False

result = linear_search([3], 1)

if result == -1:
    print("Array length cannot be zero")
else: 
    if result:
        print("Found!")
    else: print("Not found!")    