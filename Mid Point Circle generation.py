c=list(map(int,input("\nEnter xc yc r: ").strip().split()))

xc=c[0]
yc=c[1]
r=c[2]

p=1-r
k=0
x,y=0,r

print('%2d %3d %3d %3d %9s'%(k,p,x,y,"({},{})".format(x,y)))
print('%2s %3s %3s %3s %9s'%('k','pk+1','xk+1','yk+1',"octant"))

while x<y:
    x+=1
    if p<0:
        p=p+2*x+1
        
    else:
        y-=1
        p=p+2*(x-y)+1
    k+=1
    print('%2d %3d %3d %3d %9s'%(k,p,x,y,"{},{},{},{},{},{},{},{}".format((xc+x,yc+y)
    ,(xc-x,yc+y)
    ,(xc+x,yc-y)
    ,(xc-x,yc-y)
    ,(xc+y,yc+x)
    ,(xc-y,yc+x)
    ,(xc+y,yc-x)
    ,(xc-y,yc-x))))
    
