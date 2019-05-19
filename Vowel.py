#Design a program that will take any word and print out the vowels
#Have a user input
#Assign A, E, I, O, U, to the funtcion
#Create a variable of type (int) to represent of "A's" in a vowel
#Use a for loop to search through word for the number of "A's"

def vowel():

    import fnmatch

    word = (input ("Type a word!: "))

    print ("You typed!: ", word)

    if fnmatch.fnmatch (word, "*a*"):
        print ("The Vowel 'A'")

    if fnmatch.fnmatch (word, "*e*"):
        print ("The Vowel 'E'")

    if fnmatch.fnmatch (word, "*i*"):
        print ("The Vowel 'I'")

    if fnmatch.fnmatch (word, "*o*"):
        print ("The Vowel 'O'")

    if fnmatch.fnmatch (word, "*u*"):
        print ("The Vowel 'U'")

    if fnmatch.fnmatch (word, "*y*"):
        print ("Maybe 'Y'")

    vowcnta = 0
    vowcnte = 0
    vowcnti = 0
    vowcnto = 0
    vowcntu = 0
    vowcnty = 0

    for name in word:
        if name == "a":
            vowcnta += 1
    if vowcnta != 0:
        print ("The word", word, "has {} A's".format(vowcnta))

    for name in word:
        if name == "e":
            vowcnte += 1
    if vowcnte != 0:
        print ("The word", word, "has {} E's".format(vowcnte))

    for name in word:
        if name == "i":
            vowcnti += 1
    if vowcnti != 0:
        print ("The word", word, "has {} I's".format(vowcnti))

    for name in word:
        if name == "o":
            vowcnto += 1
    if vowcnto != 0:
        print ("The word", word, "has {} O's".format(vowcnto))

    for name in word:
        if name == "u":
            vowcntu += 1
    if vowcntu != 0:
        print ("The word", word, "has {} U's".format(vowcntu))

    for name in word:
        if name == "y":
            vowcnty += 1
    if vowcnty != 0:
        print ("The word", word, "has {} Y's, but is Y really a vowel".format(vowcnty))
