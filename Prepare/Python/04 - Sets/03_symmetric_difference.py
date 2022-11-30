M = input()
a = set(map(int, input().split()))
N = input()
b = set(map(int, input().split()))

sd = a.symmetric_difference(b)

for i in sorted(sd):
    print(i)
