english_students = int(input())
english_roll_numbers = set(map(int, input().split()))
french_students = int(input())
french_roll_numbers = set(map(int, input().split()))
english_only = english_roll_numbers.difference(french_roll_numbers)
print(len(english_only))


""" Alternate Solution:
english_students = int(input())
english_roll_numbers = set(map(int, input().split()))
french_students = int(input())
french_roll_numbers = set(map(int, input().split()))
print(len(english_roll_numbers - french_roll_numbers))
"""
