# Here's an alternative solution to the problem using the replace() method.
# def split_and_join(line):
#     return print(line.replace(" ","-"))


def split_and_join(line):
    a = line.split(" ")
    a = "-".join(a)
    return a


if __name__ == "__main__":
    line = input()
    result = split_and_join(line)
    print(result)
