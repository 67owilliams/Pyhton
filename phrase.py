#Pick a phrase
#Have user input to pick two characters out of the phrase for the range.
#Use str.find(str, beg = 0, end = len (string))
#Have the function calculate the range and return the value

def words():
    phrase = input ("Type whatever!, TRY ME!!!: ")
    print ("You typed!: ", phrase)
    a = ("a", "e", "i", "o", "u")
    print ("You typed", a, phrase.find (a))
    #print (a,(int (float (phrase.find (a)))))
pop = words()
