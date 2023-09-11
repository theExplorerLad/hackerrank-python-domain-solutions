def split_and_join(line):
    a = line.split(" ")
    a = "-".join(a)
    return a


if __name__ == "__main__":
    line = input()
    result = split_and_join(line)
    print(result)


""" Alternate Solution:

def split_and_join(line):
    return print(line.replace(" ","-"))

line = input()
split_and_join(line)
"""
