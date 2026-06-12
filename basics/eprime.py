def prime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    if fc==2:
        return True
n1=int(input())
n2=int(input())

s=0
avg=0
for i in range(n1,n2+1):
    rev=0
    if prime(i) and i>11:
            a=i
            while a>0:
                r=a%10
                rev=rev*10+r
                a=a//10
            if prime(rev):
                s+=i
                avg+=1
if avg>0:
    print(f'{s/avg:.3f}')
else:
    print('not found')