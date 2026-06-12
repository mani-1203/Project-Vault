def duck(n):
    dc=0
    while n>0:
        r=n%10
        if r==0:
            dc+=1
        n=n//10
    if dc>=1:
        return True

n=int(input())
if duck(n):
    print(f'{n} is a duck number')
else:
    print('not a dick')