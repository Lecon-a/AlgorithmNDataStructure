def sort(args):
    for i in range(0, len(args)):
        for j in range(0, len(args)):
            if args[i] < args[j]:
                temp = args[i]
                args[i] = args[j]
                args[j] = temp 
    return args