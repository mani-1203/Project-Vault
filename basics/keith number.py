def keith(n):
    k=n
    l=[]
    while k>0:
        l.append(k%10)
        k=k//10
    l.reverse()
    while sum(l)<n:
        total=sum(l)
        l.pop(0)
        l.append(total)
    if sum(l)==n:
        return True
    return None
n=int(input())
if keith(n):
    print(n, "is Keith Number")
else:
    print(n,'not a Keith Number')
