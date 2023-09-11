_, english = int(input()), set(map(int, input().split()))
_, french = int(input()), set(map(int, input().split()))
print(len(english.intersection(french)))
