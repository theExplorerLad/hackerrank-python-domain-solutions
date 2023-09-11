_, english_subscribers = int(input()), set(map(int, input().split()))
_, french_subscribers = int(input()), set(map(int, input().split()))
print(len(english_subscribers.union(french_subscribers)))
