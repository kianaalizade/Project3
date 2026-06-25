# map and filter=filter: Element Selector but map: Value Transformer
x=[2,4,8,9,20,45]
y=list(map(lambda a:a%2==0,x))       
print(y)
y1=list(filter(lambda a:a%2==0,x))        
print(y1)