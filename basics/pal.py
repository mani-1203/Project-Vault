# def pal(n):
#     t=n
#     res=0
#     while n>0:
#         r = n%10
#         res=res*10+r
#         n=n//10
#     return t==res
# n1 = int(input())
# n2 = int(input())
#
# for i in range(n1,n2+1):
#     if pal(i):
#         print(i)

def pal(n):
    t=n
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev==t
n1 =int(input())
n2 = int(input())
c=0
f=0
s=0
res=''
for i in range(n1,n2+1):
    if pal(i):
        c+=1
        f+=1
        if c==1:
            print("Alternative palindrome numbers in the given range are ",end=' ')
        if f%2==0:
            s+=i
            res=res+str(i)+" + "
print(res[:-3],end=' ')
if c>0:
    print(f'= {s}')