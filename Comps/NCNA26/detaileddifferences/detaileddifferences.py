test_cases = int(input())

for i in range(test_cases):
    string_1 = input()
    string_2 = input()

    diffs = ""

    for j in range(len(string_1)):
        if string_1[j] == string_2[j]:
            diffs += "."
        else:
            diffs += "*"
    print(string_1)
    print(string_2)
    print(diffs)
    print()