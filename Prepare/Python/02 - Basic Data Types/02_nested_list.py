if __name__ == '__main__':
    l = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])

    scores = sorted(set([x[1] for x in l]))
    for name in sorted(x[0] for x in l if x[1] == scores[1]):
        print(name)
