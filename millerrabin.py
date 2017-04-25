import random

def numbits(num):
    return (len(bin(num)) - 2)

def brutePrime(num):
    isPrime = True
    i = 2
    while (i < num/2):
        if num % i == 0:
            isPrime = False
            return isPrime
        i = i + 1
    return isPrime

def MillerRabinPrime(num):
    isProbablyPrime = True
    k = 1000
    i = 0
    while i < k:
        randomCheck = random.randint(2, (num - 2))
        if num % randomCheck == 0:
            isProbablyPrime = False
            return isProbablyPrime
        i = i + 1
    return isProbablyPrime

p = long(raw_input("Enter the value of p: "))
q = long(raw_input("Enter the value of q: "))
g = long(raw_input("Enter the value of g: "))

print("Is q prime by brute force testing?")
print(brutePrime(q))

print("Is q prime by Miller-Rabin testing?")
print(MillerRabinPrime(q))

print("Is q of length 160 bits?")
if numbits(q) == 160:
    print("True")
else:
    print("False")

print("Does q divide (p-1)?")
if (p-1) % q == 0:
    print "True"
else:
    print "False"

print("Is number of bits of p between 512 and 1024?")
if numbits(p) >= 512 and numbits(p) <=1024:
    print "True"
else:
    print "False"

print("Is g of the right form - (2 ^ ((p-1)/q) mod p)")
h = 2
complexExponent = (p - 1) / q
if (pow(h, complexExponent) % p) == g:
    print "True"
else:
    print "False"
