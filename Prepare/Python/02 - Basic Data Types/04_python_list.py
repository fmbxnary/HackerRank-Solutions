if __name__ == '__main__':
    l = []
    N = int(input())
    commands = {
        "insert": lambda x, y, z: x.insert(y, z),
        "print": lambda x: print(x),
        "remove": lambda x, y: x.remove(y),
        "append": lambda x, y: x.append(y),
        "sort": lambda x: x.sort(),
        "pop": lambda x: x.pop(),
        "reverse": lambda x: x.reverse(),
    }
    for i in range(N):
        command = input().split(' ')
        if len(command) == 3:
            commands[command[0]](l, int(command[1]), int(command[2]))
        elif len(command) == 2:
            commands[command[0]](l, int(command[1]))
        else:
            commands[command[0]](l)
