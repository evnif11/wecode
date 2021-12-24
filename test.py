def even():
    li = list(range(1,51))
    return list(filter(lambda x: x%2==0, li))
