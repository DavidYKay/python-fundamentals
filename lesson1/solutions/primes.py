# find the sum of all primes below one million

def sum_primes_up_to(limit):
    # By default, we consider everything a prime number
    is_prime = [True] * limit

    # Except for 0 and 1.
    is_prime[0] = False
    is_prime[1] = False

    # Now, check each number. If it is prime, then mark all of its multiples as non-prime
    for i in range(0, limit):
        if is_prime[i]:
            for n in range(i*i, limit, i):
                # Mark muliples non-prime
                is_prime[n] = False

    # Now go back and tally up all the prime numbers
    tally = 0
    for i in range(0, limit):
        if is_prime[i]:
            tally = tally + i

    return tally

print(sum_primes_up_to(1000000))
