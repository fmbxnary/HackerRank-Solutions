def print_formatted(number):
    lw = len(format(number, "b"))
    for i in range(1, number + 1):
        decimal = str(i).rjust(lw)
        octal = format(i, "o").rjust(lw)
        hexadecimal = format(i, "x").upper().rjust(lw)
        binary = format(i, "b").rjust(lw)
        print("{} {} {} {}".format(decimal, octal, hexadecimal, binary))


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
