# __author__ = "那位先生Beer"
#
#
# def divide(  dividend, divisor ):
#     """
#     :type dividend: int
#     :type divisor: int
#     :rtype: int
#     """
#     flag = 0
#     dividendn = abs( dividend )
#     divisorn = abs( divisor )
#     while dividendn > 0:
#         if dividendn >= divisorn:
#             dividendn -= divisorn
#             flag += 1
#         else:
#             break
#     print(flag)
#     return flag if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)  else 0 - flag
# print(divide(7, -3))

def divide( dividend, divisor ):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    MAX_INT = 0x7fffffff
    if divisor == 0: return MAX_INT
    sign = 1
    if divisor < 0:
        sign = -sign
        divisor = -divisor
    if dividend < 0:
        sign = -sign
        dividend = -dividend
    res = 0
    while dividend >= divisor:
        redu = divisor
        res0 = 1
        while dividend > redu * 2:
            res0 <<= 1
            redu <<= 1
        dividend -= redu
        res += res0
    if sign < 0:
        res = -res
    if res > MAX_INT:
        res = MAX_INT
    return res
print(divide(-2147483648, -1))