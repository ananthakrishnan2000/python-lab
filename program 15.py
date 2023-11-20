a = str(input("enter the str 1:"))
b = str(input("enter the str 2:"))
print(a.replace(a[0],b[0]) + ' ' + b.replace(b[0],a[0]))