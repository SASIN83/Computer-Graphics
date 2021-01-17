def bezierCurve(x, y, z):
    xu = round(0.0,3)
    yu = round(0.0,3)  
    zu=round(0.0,3)
    u = 0  
    i = 0 
    co=[]
    while u<=1:
        xu = round(pow(1-u,3)*x[0]+3*u*pow(1-u,2)*x[1]+3*pow(u,2)*(1-u)*x[2]+pow(u,3)*x[3],3)
        yu = round(pow(1-u,3)*y[0]+3*u*pow(1-u,2)*y[1]+3*pow(u,2)*(1-u)*y[2]+pow(u,3)*y[3],3)
        zu = round(pow(1-u,3)*z[0]+3*u*pow(1-u,2)*z[1]+3*pow(u,2)*(1-u)*z[2]+pow(u,3)*z[3],3)
        co.append(tuple((xu , yu, zu)))
        u+=0.1
        
    return(co)

        
x=list(map(int,input("Enter the x coordinates: ").strip().split()))
y=list(map(int,input("Enter the y coordinates: ").strip().split()))
z=list(map(int,input("Enter the z coordinates: ").strip().split()))
x=bezierCurve(x, y, z)
print(x,y,z)
for i in range(len(x)):
    print(x[i])
