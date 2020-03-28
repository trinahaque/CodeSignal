def rangeBitCount(a, b):
    if (0<=a and a<=b):
        total = 0
        for i in range(a, b+1):
            t = i
            while (t != 0):
                if((t&1)==1):
                    total += 1
                t >>= 1 
        return total

    