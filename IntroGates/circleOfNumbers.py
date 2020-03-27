# // Given n and firstNumber, find the number which is radially opposite position to firstNumber

def circleOfNumbers(n, firstNumber):
    result = (firstNumber + n / 2) % n
    return result