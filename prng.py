seed = input("Enter a seed value for RNG:\n")
a = 1103515245
c = 12345
m = 2147483647

def lcg():
    global seed
    seed = ((a * seed) + c) % m
    return seed

n = input("How many numbers to generate?:\n")

print "Here are %d random numbers:" %n
i = 0
while i < n:
    print(lcg())
    i = i + 1
