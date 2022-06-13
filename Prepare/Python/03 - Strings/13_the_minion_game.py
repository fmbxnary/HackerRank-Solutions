def minion_game(string):
    # The vowels in the alphabet
    vowels = "AEIOU"

    # initialize the score for each player
    stuart = 0
    kevin = 0

    # the length of the string
    length = len(string)

    # loop through the string
    for i in range(length):
        # calculate the point
        point = length - i
        # if the string[i] is a vowel, kevin gets the point
        if string[i] in vowels:
            kevin += point
        # if the string[i] is a consonant, stuart gets the point
        else:
            stuart += point

    # if player's score is equal, print "Draw"
    if stuart == kevin:
        print("Draw")
    # if stuart's score is greater, print "Stuart"
    if stuart > kevin:
        print("Stuart {}".format(stuart))
    # if kevin's score is greater, print "Kevin"
    if stuart < kevin:
        print("Kevin {}".format(kevin))

# main function
if __name__ == "__main__":
    s = input()
    minion_game(s)
