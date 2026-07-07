import random
items=[1,2,3,4,5,6,7,8,9]
def shuffle_list(items):
    n=len(items)
    for i in range(n-1,0,-1):
        j=random.randint(0,i)
        items[i],items[j]=items[j],items[i]
    return items

b=shuffle_list(items)
print(b)
