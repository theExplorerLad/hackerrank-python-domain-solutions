if __name__ == "__main__":
    N = int(input())
    l = []
    for _ in range(N):
        user = input().split()
        operation = user[0]
        args = user[1:]
        if operation != "print":
            operation += "(" + ",".join(args) + ")"
            eval("l." + operation)
        else:
            print(l)
