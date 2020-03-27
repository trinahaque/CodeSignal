# For n = 808, the output should be
# lateRide(n) = 14.

# 808 minutes mean that it's 13:28 now, so the answer should be 1 + 3 + 2 + 8 = 14.

def lateRide(n):
    hours = int(n/60)
    minutes = n % 60
    hourSum = sum(int(digit) for digit in str(hours))
    minuteSum = sum(int(digit) for digit in str(minutes))
    return hourSum + minuteSum