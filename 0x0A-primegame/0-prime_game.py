#!/usr/bin/python3
"""Prime Game"""

def findPrimes(limit):
    """Given a set of consecutive integers starting from 1 up to and including n,
     they take turns choosing a prime number from the set and removing
      that number and its multiples from the set.
     The player that cannot make a move loses the game.
    """
    primes = []
    sieve = [True] * (limit + 1)
    current = 2
    while current <= limit:
        if sieve[current]:
            primes.append(current)
            multiple = current
            while multiple <= limit:
                sieve[multiple] = False
                multiple += current
        current += 1
    return primes


def isWinner(x, nums):
    """
    Assuming Maria always goes first and both players play optimally
    determine who the winner of each game is.
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    
    Maria = Ben = 0
    roundIndex = 0
    
    while roundIndex < x:
        primes = findPrimes(nums[roundIndex])
        if len(primes) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
        roundIndex += 1
    
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    
    return None
