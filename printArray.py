from random import choice
from array import array

prime = [2]
count = 2
randomPrime = []

def primeCount(count):
    for num in range(2, int(count**0.5)+1):
        if count % num == 0:
            return False
    prime.append(count)
    return True

# Getting the first 1000 Prime Numbers
while len(prime) != 1000:
    if count%2 != 0:
        primeCount(count)
    count += 1

# Setting the generated Prime Number in a Random array
for _ in range(1000):
    n = choice(prime)
    randomPrime.append(n)

# Chuncking the Prime numbers into a 3D 10x10x10 array
def chunk(arr, size):
    cum = []
    for i in range(0, len(arr), size):
        cum.append(arr[i:i+size])
    return cum

def chunk3d10(arr):
    return [chunk(x, 10) for x in chunk(arr, 100)]

print(chunk3d10(randomPrime))
