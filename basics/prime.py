# n1 = int(input())
# n2 = int(input())
# for i in range(n1,n2+1):
#     fc=0
#     for j in range(1,i+1):
#         if i%j==0:
#             fc+=1
#     if fc == 2:
#         print(i)
#
# def prime(n):
#     fc=0
#     for j in range(1,n+1):
#         if n%j==0:
#             fc+=1
#     if fc==2:
#         return True
#     return None
#
#
# n1 = int(input())
# n2 = int(input())
#
# for i in range(n1,n2+1):
#     if prime(i):
#         print(i)

def prime(n):
    fc=0
    for i in range(1,n+1):
        if n%i==0:
            fc+=1
    if fc==2:
        return True
    return None
c=0
n=int(input())
for j in range(1,n+1):
    if n%j==0:
        if prime(j):
            c+=1
            if c==1:
                print(f'Prime Factors of {n} is',end=' ')
            print(j,end=' ')