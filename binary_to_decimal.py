def binary_to_decimal(s):

    ''' 101 
    res = 2 + 0
    res = 2*res + next
    '''
    lmd = 0
    res = int(s[0])
    for i in range(len(s)-1):
        res = 2 * res + int(s[i+1])
    
    return res 


print(binary_to_decimal('101'))
print(binary_to_decimal('100'))