# doubkle of numner
def double_result(func):
    def wrapper(a,b):
        result= add(a,b)*2
        return result
    return wrapper
@double_result
def add(a,b):
    num=a+b
    return num
a=int(input("enter a value "))
b=int(input("enter a value "))
print("the double is ",add(a,b))