__author__ = "那位先生Beer"


def compress(chars):
    flag = 0
    count = 1
    if len(chars) == 1:
        return 1
    chars.append( 0 )
    for i in range(1, len(chars)):
        if chars[i - 1] == chars[i]:
            count += 1
        else:
            if count > 1:
                chars[flag] = chars[i - 1]
                for j in range( len( str( count ) ) ):
                    chars[flag + j + 1] = str( count )[j]
                flag = flag + len( str( count ) ) + 1
                count = 1
            else:
                chars[flag] = chars[i - 1]
                flag += 1
    print(chars[0:flag])
    return flag
print(compress(["a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","b"]))
