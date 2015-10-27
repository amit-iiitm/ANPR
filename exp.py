import initial
import trial2
from numpy import ndarray

for i in range(1,2):
  im=initial.Process(i)
  
  imw=im.size[0]
  imh=im.size[1]
  max_wh=ndarray((imw,),int)
  max_h=0
  pix=im.load()
  for i in range(imw):
     max_wh[i]=0
     this_h=0
     for j in range(imh):
          if(pix[i,j]==0):
             max_wh[i]=max(max_wh[i],this_h) 
             this_h=0
          else:
             this_h+=1
     max_wh[i]=max(max_wh[i],this_h) 
     max_h=max(max_h,max_wh[i])
  
  for i in range(imw):
     if(abs(max_wh[i]-max_h)<10):
         for j in range(imh):
               im.putpixel((i,j),0)
  
  im.show()
  
