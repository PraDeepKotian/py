def checknum(num):
    res = num%10
    if res == 1:
        print(num -1)
    elif res == 2:
        print(num -2)
    elif res == 3:
        print(num -3)
    elif res == 4:
        print(num -4)
    elif res == 5:
        print(num)
    elif res == 6:
        print(num +4)
    elif res == 7:
        print(num +3)
    elif res == 8:
        print(num +2)
    elif res == 9:
        print(num +1)
    else:
        print(num)
        
checknum(108)        
        
    
