def count_substring(s, sub_s):
    count = 0
    for i in range(len(s)):
        if s[i:].startswith(sub_s):
            count += 1
    return count


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
