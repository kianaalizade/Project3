x=[12,45,98,0,-1,4,123,56,-15]
value=int(input("please enter a number:"))

def linear_search(x,value):
    b=len(x)
    for item in range(b):
       if x[item]==value:
           return f"{value} found in index {item}"
    else:
        return f"{value} not found"
end=linear_search(x,value)
print(end)

       
    
