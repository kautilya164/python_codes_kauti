def even_numbers(limits):
    while limits > 0:
        if limits % 2 == 0:
            yield limits
        limits = limits - 1
limits = int(input("Enter the value: "))
for i in even_numbers(limits):
    print(i)
