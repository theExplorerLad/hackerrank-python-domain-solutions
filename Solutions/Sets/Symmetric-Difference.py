_, M, _, N = int(input()), set(input().split()), int(input()), set(input().split())
output_set = M.symmetric_difference(N)
print("\n".join(sorted(output_set, key=int)))


""" Alternate Solution:

_, M = int(input()), set(map(int, input().split()))
_, N = int(input()), set(map(int, input().split()))

symmetric_diff = (M.union(N)) - (M.intersection(N))
for i in sorted(symmetric_diff):
    print(i)
"""
