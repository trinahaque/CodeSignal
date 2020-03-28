def arrayPacking(a):
    if(1 <= len(a) and len(a) <= 4):
        result = 0
        for i in range(0, len(a)):
            if(a[i]>256 or a[i]<0):
                return
            else:
                result += a[i] << 8 * i
        return result
   