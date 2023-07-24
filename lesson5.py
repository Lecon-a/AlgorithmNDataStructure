def insert(args, value):
    # This is an example of true insertion
    arr = []
    if type(value) == type([]): arr.extend(value) 
    else: arr.extend([value])
    arr.extend(args)
    return arr

print(insert([5, 8, 9, 10], 20))    
