__author__ = "那位先生Beer"


def findWords(words ):
    line1 = set( ['q','w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'] )
    line2 = set( ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'] )
    line3 = set( ['z', 'x', 'c', 'v', 'b', 'n', 'm'] )
    reList = []
    for i in range( len( words ) ):
        if len(set(words[i].lower()) & set(line1)) == len(set(words[i].lower())) or len(set(words[i].lower()) & set(line2)) == len(set(words[i].lower())) or len(set(words[i].lower()) & set(line3)) == len(set(words[i].lower())):
            reList.append(words[i])
    return reList
print(findWords(["Hello", "Alaska", "Dad", "Peace"]))