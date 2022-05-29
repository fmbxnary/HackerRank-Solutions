N, M = map(int, input().split())

WELLCOME = "WELCOME".center(M, '-')
SYMBOL = ".|."

for i in range(1, N, 2):
    print(str(SYMBOL * i).center(M, '-'))
print(WELLCOME)
for i in range(N - 2, -1, -2):
    print(str(SYMBOL * i).center(M, '-'))
