def fac(num):
    if num >= 2:
        return num*fac(num -1)
    elif num == 1:
        return 1
    elif num == 0:
        return 1