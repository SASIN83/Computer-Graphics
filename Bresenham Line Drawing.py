c=list(map(int,input("\nEnter x1 y1 x2 y2: ").strip().split()))
x1=c[0]
y1=c[1]
x2=c[2]
y2=c[3]

if x1<x2:
    x=x1
    y=y1
else:
    x=x2
    y=y2
dx,dy=x2-x1,y2-y1

m=dy/dx
k=0
if m<1:
    pk=2*dy-dx
    print('%2s %3s %5s %7s %9s'%('k','pk','x','y','(x,y)'))
    print('%2d %3d %5d %7d %9s'%(0,pk,x,y,"({},{})".format(x,y)))
    for i in range(x1,x2):
        x+=1
        if pk<0:
            pk=pk+2*dy
            y=y
        else:
            pk=pk+2*(dy-dx)
            y+=1
        k+=1
        print('%2d %3d %5d %7d %9s'%(k,pk,x,y,"({},{})".format(x,y)))
    
else:
    pk=2*dx-dy
    print('%2s %3s %5s %7s %9s'%('k','pk','x','y','(x,y)'))
    print('%2d %3d %5d %7d %9s'%(0,pk,x,y,"({},{})".format(x,y)))
    for i in range(y1,y2):
        y+=1
        if pk<0:
            pk=pk+2*dx
            x=x
        else:
            pk=pk+2*(dx-dy)
            x+=1
        k+=1
        print('%2d %3d %5d %7d %9s'%(k,pk,x,y,"({},{})".format(x,y)))
        
