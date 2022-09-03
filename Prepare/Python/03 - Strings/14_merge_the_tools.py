import textwrap


def merge_the_tools(string, k):
    wrapper = textwrap.TextWrapper(width=k)
    word_list = wrapper.wrap(text=string)
    for element in word_list:
        print("".join(set(element)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
