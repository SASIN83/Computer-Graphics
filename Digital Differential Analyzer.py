c=list(map(int,input("\nEnter x1 y1 x2 y2: ").strip().split()))
x1=c[0]
y1=c[1]
x2=c[2]
y2=c[3]

dx,dy=x2-x1,y2-y1

if abs(dx)>=abs(dy):
    steps=abs(dx)
    
else:
    steps=abs(dy)

 
xinc,yinc=dx/steps,dy/steps

x,y=x1,y1

print('dx = {},dy = {}'.format(dx,dy))
print('xinc = {},yinc = {}'.format(round(xinc,1),round(yinc,1)))
print('x = {},y = {}'.format(x1,y1))
print('%2s %3s %5s %7s'%('k','x','y','(x,y)'))
print('%2d %3f %5f %7s'%(0,x,y,"({},{})".format(x,y)))

for i in range(0,steps):
    x+=round(xinc,1)
    y+=round(yinc,1)
    print('%2d %3f %5f %7s'%(i+1,round(x,1),round(y,1),"({},{})".format(round(x),round(y))))
    
    
