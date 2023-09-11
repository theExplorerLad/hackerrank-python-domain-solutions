_ = int(input())
english_subscribers = set(map(int, input().split()))
_ = int(input())
french_subscribers = set(map(int, input().split()))
print(len(english_subscribers.symmetric_difference(french_subscribers)))


""" Alternate Solution:

_, english = int(input()), set(map(int, input().split()))
_, french = int(input()), set(map(int, input().split()))
english_or_french = english.union(french) - english.intersection(french)
print(len(english_or_french))
"""
