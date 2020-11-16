num1=[1,2,3,6,4]
num2=[2,1,3,4,2]
i=0
sum=0
while (i<len(num1)):
    j=0
    while(j<len(num2)):
        sum=num1[i]+num2[j]
    
        print (sum)
        sum=0
        j=j+1
    i=i+1

