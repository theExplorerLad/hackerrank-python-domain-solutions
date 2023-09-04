if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().strip().split()))
    winner_score = max(A)
    while winner_score in A:
        A.remove(winner_score)
    print(max(A))
