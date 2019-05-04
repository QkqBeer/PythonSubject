__author__ = "那位先生Beer"


def subdomainVisits( cpdomains ):
    """
    :type cpdomains: List[str]
    :rtype: List[str]
    """
    reDir = {}
    for i in range( len( cpdomains ) ):
       t = cpdomains[i].split( ' ' )
       n = int(t[0])
       q = t[1].split('.')
       for i in range(len(q)):
           newStr = ".".join(q[i:])
           if newStr not in reDir:
               reDir[newStr] = n
           else:
               reDir[newStr] += n
    reList = []
    for key in reDir:
        reList.append(str(reDir[key]) + " " + key )
    print(reList)

subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])

