id = {"name":"Kenwood Harris", "buname":"khjr"}

import string

def word_count (SomeTextString):
    counter = {}                    #Sets the dictionary that stores the word count
    words = SomeTextString.split()      #Sets words equal to a list containing all the words in the string
    num = 0                             #Sets internal counter for number of unique words
    punctuation = []                    #Holds list of all punctuation values
    #---------------------------------------------------------------------------------------------
    """
    The following section of Code removes all punctuation from the words that are split
    """
    for i in string.punctuation:        #Loops through the internal python list which contains all punctuation
        punctuation.append(i)           #appends all the punctuation into a list for easy comparablity

    for x in punctuation:                   #Loops through all the punctuation
        for word in range(0,len(words)):    #Sets the iterable "word" equal to a value between 0 and the length of the list of words
            if  x in words[word]:           #If one or more of the puntuation symbols are in the word, perfom the following:
                newstring = ''              #Sets a newstring internal variable to save the value of the string without punctuation
                for i in range(0,len(words[word])):         #Sets the iterable i to a value between 0 and the lenght of the current sting in postion word in words
                    if words[word][i] != x:                 #If the current character is not the punctuation trigger:
                        newstring = newstring + words[word][i]      #Add it to the value of the newstring, which does not contain punctuation
                words[word] = newstring                     #Placest the word in the new string with the word with no punctuation
    #----------------------------------------------------------------------------------------------
    """
    The following section of Code makes all the characters in of the words in the wordlist lowercase
    """
    for h in range(0,len(words)):      #Sets the iterable h to a value between 0 and the length of words
        words[h] = words[h].casefold()    #Sets the string to its lowercase equivalent

    #-------------------------------------------------------------------------------------------------------
    """
    The following seciton creates a dictionary with the key as the word, and the value as the frequency
    """
    for i in words:               #Loops through the words
        if i in counter:            #If the word already exists in the dictionary
            counter[i] = counter[i] + 1         #Set the value equal to one plus the value
        else:
            counter[i] = 1          #If the word is not already in the dictionary add it and set the counter to one
    return(counter)              #Returns the dictionary


def analyze (d):
    longerthanone = []      #Stores the words that appear more than one
    frequency = []          #Stores teh words with the highest frequency
    longest = []            #Stores the longest word(s)
    keys = list(d.keys())      #Sets keys to the list of keys
    values = list(d.values())   #Sets values to the list of values
    #------------------------------------------------------------------------------------------------------
    """
    Checks for keys whose values are greater than one
    """
    for i in range(0, len(keys)):           #Sets an iterable i to a value between zero and the length of keys
        if values[i] > 1:                     #if the value at i(key) is larger than one
            longerthanone.append(keys[i])       #Append the key
    #--------------------------------------------------------------------------------------------------------
    """
    Checks for the max frequency
    """
    maximum = max(values)               #Sets the variable maximum to the max value in the values list
    for i in range(0,len(keys)):        #Uses the iterable i to iterate through the list and the keys
        if values[i] == maximum:        #If the value of value at i is equal to the maximum
            frequency.append(keys[i])     #Append its respective key to the longest list
    #---------------------------------------------------------------------------------------------------------
    """
    Checks for the longest words
    """
    lon = 0             #Initializes the lon, will store the longest word in the dictionary
    lengths = []        #Stores the lengths of all teh words in the dictionary

    for x in keys:      #Loops through the keys
        lengths.append(len(x))  #Appends all teh lengths of the keys

    lon = max(lengths)      #Sets lon to the largest length of the keys

    for i in keys:          #Loops through the keys
        if len(i) == lon:       #If the length of the word is equal to the lon
            longest.append(i)   #append it to the longest list

    return longerthanone        #Returns all values longer than one
    return frequency            #Returns the words of highest frequency
    return longest              #Returns the longes words


def top_words (d,n):
    keys = list(d.keys())      #Sets keys to the list of keys
    values = list(d.values())   #Sets values to the list of values
    answer = []                 #Stores the tuples of the top words
    valsort = []                #Creates valsort which will store the sorted non-duplicate list
    valsort = sorted(values)    #Sorts the list by size
    valsort = list(set(valsort))    #Rids the list of duplicates
    valsort.reverse()           #Reverses the list to max to min
    counter = 0                 #Stores the counter, which counts the number of tuples that are added
    #------------------------------------------------------------------------------------------------------
    """
    Loops through the top words, and appends them if they are less than the counter
    """
    for i in valsort:           #Loops through the sorted by max to min non-duplicated list
        if counter <= n:
            for x in range(0,len(keys)):
                if values[x] == i:
                    answer.append((keys[x],values[x]))
                    counter = counter + 1

    return answer


def word_count_from_set(SomeTextString, ValidWordSet):
    counter = {}                    #Sets the dictionary that stores the word count
    words = SomeTextString.split()      #Sets words equal to a list containing all the words in the string
    num = 0                             #Sets internal counter for number of unique words
    punctuation = []                    #Holds list of all punctuation values
#---------------------------------------------------------------------------------------------
    """
    The following section of Code removes all punctuation from the words that are split
    """
    for i in string.punctuation:        #Loops through the internal python list which contains all punctuation
        punctuation.append(i)           #appends all the punctuation into a list for easy comparablity

    for x in punctuation:                   #Loops through all the punctuation
        for word in range(0,len(words)):    #Sets the iterable "word" equal to a value between 0 and the length of the list of words
            if  x in words[word]:           #If one or more of the puntuation symbols are in the word, perfom the following:
                newstring = ''              #Sets a newstring internal variable to save the value of the string without punctuation
                for i in range(0,len(words[word])):         #Sets the iterable i to a value between 0 and the lenght of the current sting in postion word in words
                    if words[word][i] != x:                 #If the current character is not the punctuation trigger:
                        newstring = newstring + words[word][i]      #Add it to the value of the newstring, which does not contain punctuation
                words[word] = newstring                     #Placest the word in the new string with the word with no punctuation
#----------------------------------------------------------------------------------------------
    """
    The following section of Code makes all the characters in of the words in the wordlist lowercase
    """
    for h in range(0,len(words)):      #Sets the iterable h to a value between 0 and the length of words
        words[h] = words[h].casefold()    #Sets the string to its lowercase equivalent
#-------------------------------------------------------------------------------------------------------
    """
    The following seciton creates a dictionary with only the words from the wordset
    """
    for i in words:               #Loops through the words
        if i in ValidWordSet:       #If the word is in the valid wordset
            if i in counter:            #If the word already exists in the dictionary
                counter[i] = counter[i] + 1         #Set the value equal to one plus the value
            else:
                counter[i] = 1          #If the word is not already in the dictionary add it and set the counter to one
    return counter              #Returns the dictionary
