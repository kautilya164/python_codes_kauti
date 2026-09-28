# decorator called show_info()
def show_info(func):
    def wrapper(num):
        print("calling function")
        result = func(num)
        print("after the function")
        return result
    return wrapper
@show_info
def square(num):
    return num * num
num = int(input("Enter a number: "))
print("The square of the number is", square(num))
