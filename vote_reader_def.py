def vots (list):
    count = {}
    for name in list:
        if name in count:
            count[name] += 1
        else:
            count[name] = 1
    return count