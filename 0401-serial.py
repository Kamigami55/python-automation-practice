def arrToStr(arr):
    leng = len(arr)
    str = ''
    isFirst = True
    for i in range(len(arr)):
        if isFirst:
            str = arr[i]
            isFirst = False
        elif i == leng-1:
            str = str + ', and ' + arr[i]
        else:
            str = str + ', ' + arr[i]
    return str

spam = ['cat', 'dog', 'yoo', 'doggy', 'thisisaword', 'another world!!!!']

str = arrToStr(spam)

print(str)
