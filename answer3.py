def cat_dog(str):
    count1 = 0
    count2 = 0
   
    if 'dog' and 'cat' not in str:
        return True
    for i in range(len(str)-1):
        if str[i:i+3] == 'cat':
            count1 += 1
        if str[i:i+3] == 'dog':
            count2 += 1
    if count1 == count2:
        return True
    else:
        return False