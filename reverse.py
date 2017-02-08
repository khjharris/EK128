"""
Takes a sentence multiple sentences and reverses their order.
"""
def reverse_sentences(S):
    senlist = []
    ends = []
    revlist = []
    sentencedef = []
    mid = []
    finalstring = ""
    for i in range(0,len(S)):
        sentencedef.append(S[i])

    for x in range(0,len(sentencedef)):
        if x != len(sentencedef) - 1:
            if sentencedef[x] == ".":
                if sentencedef[x+1] == " ":
                    ends.append(x)
            if sentencedef[x] == "?":
                if sentencedef[x+1] == " ":
                    ends.append(x)
            if sentencedef[x] == "!":
                if sentencedef[x+1] == " ":
                    ends.append(x)
        if x == len(sentencedef)- 1:
            if sentencedef[x] == ".":
                ends.append(x)
            if sentencedef[x] == "?":
                ends.append(x)
            if sentencedef[x] == "!":
                ends.append(x)

    for t in range(0,len(ends)):
        newstring = ""
        if t == 0 :
            for u in range(0,ends[t]+1):
                newstring = newstring + sentencedef[u]
            mid.append(newstring)
            newstring = ""
        else:
            for u in range(ends[t-1]+2,ends[t]+1):
                newstring = newstring + sentencedef[u]
            mid.append(newstring)
            newstring = ""

    for i in reversed(mid):
        finalstring = finalstring + i + "\n"

    return finalstring

reverse_sentences("Hello my name is Kenwood. I am 19 years old? I am also tweleve, and important!")
