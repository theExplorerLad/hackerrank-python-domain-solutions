n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    operation, *args = input().split()

    if operation == "pop":
        s.pop()
    elif operation == "remove":
        s.remove(int(args[0]))
    elif operation == "discard":
        s.discard(int(args[0]))

print(sum(s))
