# To find the vlaues > 50
def fun(x):
    return d[x] > 50
d = {"apple": 120,"banana":160,"coconut":30}


               #or

d = {"apple": 120,"banana":160,"coconut":30}
d1 = dict(filter(lambda x:x[1] > 50,d.items()))



# adding 5 to each element
l = [[1,2],[3,4,5],[5,6,8]]
l1 = list(map(lambda x: x + [5],l))

               #and

l = [[1,2],[3,4,5],[5,6,8]]
l1 = list(map(lambda x: [i+5 for i in x],l))



#finding largest number in the list

 # k = list(map(int, input().split()))
# m = -10
# for i in k:
#     if m < i:
#         m = i


#Square of each number and fliter and reduce
l = [10,20,50,60,32]
sq = list(map(lambda x:x**2,l))
print(sq)

l1 = list(filter(lambda x: x % 5 == 0,sq))
print(l1)

from functools import reduce
l3 = reduce(lambda x,y: x+y,l1)
print(l3)


#pipeline function
l4 = reduce(lambda x,y:x+y, filter(lambda x: x % 5 == 0, map(lambda x:x**2,l)))
print(l4)
