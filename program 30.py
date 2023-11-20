print("area of rectangle")
l = int(input("length:"))
b = int(input("breadth:"))
c = lambda x,y:x*y
print("area of rectangle:"+str(c(l,b)))
print("area of square")
s=int(input("side of square:"))
c=lambda x:x*x
print("area of square:"+str(c(s)))
print("area of triangle")
l=int(input("base:"))
b=int(input("height:"))
c=lambda x,y:.5*x*y
print("area of triangle:"+str(c(l,b)))