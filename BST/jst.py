def func(word1, word2):
    m = len(word1)
    n = len(word2)

    d = [[0 for j in range(m + 1)] for i in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word2[i - 1] == word1[j - 1]:
                d[i][j] = d[i - 1][j - 1] + 1
            else:
                d[i][j] = max(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1])

    print(d[n][m])

    i, j = n, m
    ans = ""
    while (i > 0 and j > 0):
        if word2[i - 1] == word1[j - 1]:
            ans = ans + word2[i - 1]
            i -= 1
            j -= 1
        elif d[i - 1][j] >= d[i][j - 1]:
            i -= 1
        else:
            j -= 1

    print(ans[::-1])


word1 = "bd"
word2 = "abcd"

func(word1, word2)
