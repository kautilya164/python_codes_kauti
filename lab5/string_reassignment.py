def change_string(s):
    if s[0] == "x":
        return s
    else:
        s = "x" + s[1:]
        return s

s = input("Enter a name or anything: ")
s = change_string(s)

print("The string is", s)
