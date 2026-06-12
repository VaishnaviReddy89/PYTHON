year=int(input())
if(year%4==0 and year % 100!=0) or (year%400 ==0):
     print("Leap year")
else:
    print("Not leap year")
    '''
    if year%4==0 and year%100!=0:
          return True
elif year%4==0 and year%400==0 and year%100==0:
    return True
else:
     return False
     
 if (year % 4 == 0):
            if (year % 100 == 0):
            if (year % 400 == 0):
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False
     
    return leap

     
     '''
     