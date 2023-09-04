if __name__ == '__main__':
    marksheet = []
    for _ in range(int(input())):
        marksheet.append([input(), float(input())])
    second_highest_score = sorted(list(set([marks for name, marks in marksheet])))[1]
    print('\n'.join([name for name, marks in sorted(marksheet) if marks == second_highest_score]))