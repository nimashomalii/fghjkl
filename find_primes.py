import sys
from prime_utils import PrimeChecker

def find_primes_between(start, end):
    checker = PrimeChecker()
    primes = []
    for num in range(start, end + 1):
        if checker.is_prime(num):
            primes.append(num)
    return primes

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python find_primes.py <start> <end>")
        sys.exit(1)

    start = int(sys.argv[1])
    end = int(sys.argv[2])
    primes = find_primes_between(start, end)
    print("Prime numbers:", primes)
