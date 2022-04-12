if __name__ == '__main__':
    s = input()
    list_method = ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']
    for m in list_method:
        print(any(map(eval("str.{}".format(m)), s)))
