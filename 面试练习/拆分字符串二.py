
def wordBreak( s, wordDict ):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    res = []
    path = []
    helper( s, res, path, wordDict )
    for i in range( len( res ) ):
        res[i] = ' '.join( res[i] )
    print(res)

def helper( s, res, path, wordDict ):
    if not s:
        res.append( path )
    for word in wordDict:
        if word == s[:len( word )]:
            helper( s[len( word ):], res, path + [word], wordDict )


wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"])



