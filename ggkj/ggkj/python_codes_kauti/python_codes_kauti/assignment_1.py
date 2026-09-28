# # list mutation
# def remove_last(lst,n):
#     lst.remove(n)
# lst=[]
# n=int(input("enter the number of elements you want to add"))
# for i in range (0,n):
#     element=int(input("enter the element"))
#     lst.append(element)
# remove_last(lst,n)
# print("the new list",lst)



# #string reassignment
# def change_string(s):
#     if s[0]=="x":
#         return s
#     else:
#         s= "x" +s[1:]
# s=input("enter a name or anything")
# change_string(s)
# print("the string is",s)


# d\
def add_entry(d):
    d["new_key"] = "new_value"
    print("Inside add_entry:", d)

def reassign_dict(d):
    d = {"completely_new_key": 42}
    print("Inside reassign_dict:", d)


my_dict = {"original_key": "original_value"}
print("Before add_entry:", my_dict)
add_entry(my_dict)
print("After add_entry:", my_dict) 


print("-" * 40)

my_dict = {"original_key": "original_value"}
print("Before reassign_dict:", my_dict)
reassign_dict(my_dict)
print("After reassign_dict:", my_dict)





# #  max of two numbers
# def maximum(a,b):
#     if (a>b):
#         print(a," is maximum")
#     else:
#         print(b," is maixmum")
# a=int(input("enter a number"))
# b=int(input("enter a number"))
# maximum(a,b)






# # factorial of number
# def factorial(n):
#     sum=1
#     if n==0:
#         print(sum)
#     else:
#         for i in range(1,n+1):
#             sum=sum*i
#     print("the factorial of given number is ",sum)
# n=int(input("enter a number "))
# factorial(n)




