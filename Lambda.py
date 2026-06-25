# lambda and sorted
_list=[("kiana",21),("kiarash",30),("sara",3),("fariba",53)]
x=sorted(_list,key= lambda age:age[1])
y=sorted(_list,key= lambda age:age[1],reverse=True)

print(x) 
print(y)
