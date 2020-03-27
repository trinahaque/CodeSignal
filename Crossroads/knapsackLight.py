def knapsackLight(value1, weight1, value2, weight2, maxW):
    totalWeight = weight1 + weight2
    if totalWeight <= maxW:
        return value1 + value2
    else:
        if weight1 > maxW and weight2 > maxW:
            return 0 
        elif weight1 <= maxW and weight2 <= maxW:
            if value1 > value2:
                return value1
            else:
                return value2
        elif weight1 <= maxW and weight2 >= maxW:
            return value1
        elif weight2 <= maxW and weight1 >= maxW:
            return value2