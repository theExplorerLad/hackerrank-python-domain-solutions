T = int(input())
for _ in range(T):
    A, set_A = int(input()), set(map(int, input().split()))
    B, set_B = int(input()), set(map(int, input().split()))
    print(set_B.intersection(set_A) == set_A)


""" Alternate Solution:

for _ in range(int(input())):
    A, set_A = int(input()), set(map(int, input().split()))
    B, set_B = int(input()), set(map(int, input().split()))
    print(set_A.issubset(set_B))
"""
