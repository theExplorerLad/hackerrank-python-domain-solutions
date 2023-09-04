if __name__ == "__main__":
    n = int(input())
    input_list = map(int, input().split())
    t = tuple(input_list)
    print(hash(t))
