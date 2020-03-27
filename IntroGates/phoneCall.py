def phoneCall(min1, min2_10, min11, s):
    totalDuration = 0
    if s < min1:
        return totalDuration
    else: 
        totalDuration += 1
        s = s - min1
        if s - 9 * (min2_10) >= 0:
            totalDuration += 9
            s = s - (9 * min2_10)
            totalDuration += int(s / min11)
            return totalDuration
        # // not enough money
        else:
            totalDuration += int(s / min2_10)
            return totalDuration
