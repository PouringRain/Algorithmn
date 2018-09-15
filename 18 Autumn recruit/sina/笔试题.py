# coding=utf-8
import sys

# 最长公共子序列
def sina_1(a, b):
    if not a or not b:
        return 0
    lenA, lenB = len(a), len(b)
    dp = [[0 for i in range(lenB)] for j in range(lenA)]
    dp[0][0] = 1 if a[0]==b[0] else 0
    for i in range(1, lenA):
        if a[i]==b[0]:
            dp[i][0] = 1
        else:
            dp[i][0] = max(dp[i-1][0], 0)

    for i in range(1, lenB):
        if b[i]==a[0]:
            dp[0][i] = 1
        else:
            dp[0][i] = max(dp[0][i-1], 0)

    for i in range(1, lenA):
        for j in range(1, lenB):
            if a[i]==b[j]:
                dp[i][j] = max(dp[i-1][j-1]+1, dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # print(dp)
    return dp[-1][-1]

if __name__ == "__main__":
    # 读取第一行的n
    a = input()
    b = input()
    # ab  ba
    ret = sina_1(a, b)

    print(ret)
