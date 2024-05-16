# primefinder.py - a very ugly prime finder

""" To find all the prime numbers less than or equal to a given integer n by Eratosthenes' method:

3. Enumerate the multiples of p by counting in increments of p from 2p to n, and mark them in the list (these will be 2p, 3p, 4p, ...; the p itself should not be marked).

4. Find the smallest number in the list greater than p that is not marked. If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
5. When the algorithm terminates, the numbers remaining not marked in the list are all the primes below n.
 """

i = [i for i in range(2,101)] #  Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
p = [2] # Initially, let p equal 2, the smallest prime number.
# Enumerate the multiples of p by counting in increments of p from 2p to n, and mark them in the list (these will be 2p, 3p, 4p, ...; the p itself should not be marked).
m = 2 # multiplier

for n in i:
    i[m]
    p.append()