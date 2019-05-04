__author__ = "那位先生Beer"


def findRestaurant(list1, list2 ):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    loveFood = []
    for i in range(len(list1)):
        for j in range( len(list2) ):
            if list1[i] == list2[j]:
                loveFood.append((i + j, list1[i]))
    return sorted(loveFood)[0][1]
print(findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],["KFC", "Shogun", "Burger King"]))