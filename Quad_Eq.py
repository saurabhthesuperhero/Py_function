a=float(input("a :"))
b=float(input("b :"))
c=float(input("c :"))
# bx+c = 0
if a==0:
    x= -c/b
    print("Output :",x)
# ax^2+bx+c = 0
else: 
    x1 = (-b+(((b**2)-4*a*c)**0.5))/(2*a)
    x2 = (-b-(((b**2)-4*a*c)**0.5))/(2*a)
    print("Output :",x1,",",x2)
