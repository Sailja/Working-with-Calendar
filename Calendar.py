import calendar
import pprint
for _ in range(int(input())):
    d,m,y,d1,m1,y1=map(int,input().split())
    if d>13:
        m+=1
    if d1<13:
        m1-=1
    count=0
    for i in range(y,y1+1):
        if i==y1 and i==y:
            s=m
            f=m1+1
        elif i==y1:
            s=1
            f=m1+1
        elif i==y:
            s=m
            f=13
        else:
            s=1
            f=13        
            
        
        for j in range(s,f):
            #print(i, j)
            ar=calendar.monthcalendar(i,j)
            #pprint.pprint(ar)
            z=ar[0][4]
            
            p=1
            while z<13:
                z=ar[p][4]
                p+=1
            if z==13:
                count+=1
            
          
    print(count)
