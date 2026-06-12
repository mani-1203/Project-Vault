def arm(n):
    t=n
    dc=0
    sum=0
    while n>0:
        r=n%10
        dc+=1
        n=n//10
    n=t
    while n>0:
        r=n%10
        sum=sum + (r**dc)
        n=n//10
    return sum==t
n1 = int(input())
n2 = int(input())

for i in range(n1,n2+1):
    if arm(i):
        print(i)
