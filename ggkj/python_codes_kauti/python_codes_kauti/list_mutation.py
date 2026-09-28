# list mutation
def remove_last(lst,n):
    lst.remove(n)
lst=[]
n=int(input("enter the number of elements you want to add"))
for i in range (0,n):
    element=int(input("enter the element"))
    lst.append(element)
remove_last(lst,n)
print("the new list",lst)