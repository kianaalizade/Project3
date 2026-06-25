x=[-1,6,12,67,98,100,109,1000,2345]
def binary_search(_list1,value):
    if len(_list1)==0:
        return "value not find "
    
    mid=len(_list1)//2
    if _list1[mid]==value:
        return 1
    elif _list1[mid]<value  :
        _list2=_list1[mid+1:]
        return binary_search(_list2,value)
    else:
        _list2=_list1[:mid]
        return binary_search(_list2,value)
    
    
    


end=binary_search(x,23)
print(end)

