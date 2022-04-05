def isPalin(s):
    return s == s[::-1]

s ="malayalam"
ans = isPalin(s)

if ans:
    print("Yes")
else:
    print("No")