N = int(input())
countries = set()
for _ in range(N):
    countries.add(input())
print(len(countries))


""" Alternate Solution:

N=int(input())
countries = [input() for _ in range(N)]
print(len(set(countries)))
"""
