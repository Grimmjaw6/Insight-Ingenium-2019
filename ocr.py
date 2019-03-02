#code for table extraction

import cv2
import numpy as np

def transform(pos):
# This function is used to find the corners of the object and the dimensions of the object
    pts=[]
    n=len(pos)
    for i in range(n):
        pts.append(list(pos[i][0]))
       
    sums={}
    diffs={}
    tl=tr=bl=br=0
    for i in pts:
        x=i[0]
        y=i[1]
        sum=x+y
        diff=y-x
        sums[sum]=i
        diffs[diff]=i
    sums=sorted(sums.items())
    diffs=sorted(diffs.items())
    n=len(sums)
    rect=[sums[0][1],diffs[0][1],diffs[n-1][1],sums[n-1][1]]
    #      top-left   top-right   bottom-left   bottom-right
   
    h1=np.sqrt((rect[0][0]-rect[2][0])**2 + (rect[0][1]-rect[2][1])**2)     #height of left side
    h2=np.sqrt((rect[1][0]-rect[3][0])**2 + (rect[1][1]-rect[3][1])**2)     #height of right side
    h=max(h1,h2)
   
    w1=np.sqrt((rect[0][0]-rect[1][0])**2 + (rect[0][1]-rect[1][1])**2)     #width of upper side
    w2=np.sqrt((rect[2][0]-rect[3][0])**2 + (rect[2][1]-rect[3][1])**2)     #width of lower side
    w=max(w1,w2)
   
    return int(w),int(h),rect

img = cv2.imread('fintech4.png',0)
img_col = cv2.imread('fintech4.png')
kernel_sharp = np.array([[-1,-1,-1],[-1, 9,-1],[-1,-1,-1]])
img = cv2.filter2D(img,-1,kernel_sharp)
edges = cv2.Canny(img,100,200)
cv2.imwrite('fin.png',edges)

size_of_image = img.shape[0]*img.shape[1]
#print(size_of_image)

img=cv2.imread('fin.png')
#print(img.shape)
img_ori = img

#img_ori = cv2.resize(img_ori,(256,256))
#print(img.shape)

r=500.0 / img.shape[1]
dim=(500, int(img.shape[0] * r))
img=cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
img_col=cv2.resize(img_col, dim, interpolation = cv2.INTER_AREA)

#img=cv2.resize(img, (256,256))
img_ori =cv2.resize(img_ori, dim, interpolation = cv2.INTER_AREA)
#print(img_ori.shape)
#cv2.imshow('INPUT',img)
#gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#gray=cv2.GaussianBlur(gray,(11,11),0)
edge=cv2.Canny(img,100,200)
#cv2.imshow('canny',edge)
contours,_=cv2.findContours(edge.copy(),1,1)
cv2.drawContours(img,contours,-1,[0,255,0],2)
cv2.imshow('Contours',img)
n=len(contours)
max_area=0
pos=0
for i in contours:
    area=cv2.contourArea(i)
    if area>max_area:
        max_area=area
        pos=i
peri=cv2.arcLength(pos,True)
approx=cv2.approxPolyDP(pos,0.02*peri,True)
size=img.shape
w,h,arr=transform(approx)
pts2=np.float32([[0,0],[w,0],[0,h],[w,h]])
pts1=np.float32(arr)
M=cv2.getPerspectiveTransform(pts1,pts2)
dst=cv2.warpPerspective(img,M,(w,h))
dst_ori = cv2.warpPerspective(img_ori,M,(w,h))
#cv2.imshow('j',dst_ori)
#cv2.waitKey(0)
image=cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)
#image_ori =cv2.cvtColor(dst_ori,cv2.COLOR_BGR2GRAY)
image_ori=dst_ori
#image=cv2.adaptiveThreshold(image,255,1,0,11,2)
image = cv2.resize(image,(w,h),interpolation = cv2.INTER_AREA)
image_ori = cv2.resize(image_ori,(w,h),interpolation = cv2.INTER_AREA)

size_of_image = img.shape[0]*img.shape[1]
#print(img.size)
print(size_of_image)

index = 0
areas = []
#finding the countour areas
for c in contours:
    areas.append(cv2.contourArea(c))
#print(areas)

areas = sorted(areas,reverse=True)
print(areas[0])
print(areas[1])
cnt = len(areas)
while cnt:
    if areas[index]< size_of_image-2000:
        break
    else:
        index = index+1
        cnt = cnt-1
print(index)

cnt = sorted(contours, key = cv2.contourArea, reverse = True)[2]
M = cv2.moments(cnt)
#print(M)

x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
ss = img_col[y:y+h,x:x+w]
cv2.imshow('bounded box image',ss)
cv2.imwrite('bbi.jpg',ss)

#cv2.imshow('bounded box image',ss)
cv2.waitKey(0)

#######################################

#code after table extraction
import numpy as np
import cv2 as cv
import cv2
from matplotlib import pyplot as plt
from PIL import Image, ImageOps
 
 
def add_border(input_image, output_image, border):
    img = Image.open(input_image)
 
    if isinstance(border, int) or isinstance(border, tuple):
        bimg = ImageOps.expand(img, border=border)
    else:
        raise RuntimeError('Border is not an integer or tuple!')
 
    bimg.save(output_image)

   
img = cv.imread('bbi.jpg',0)
edges = cv.Canny(img,100,200)
cv2.imwrite('fin.png',edges)
add_border('fin.png', output_image='fin.png',
               border=20)
#plt.subplot(121),plt.imshow(img,cmap = 'gray')
#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(edges,cmap = 'gray')
#plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
#cv2.imshow('canny',edges)
#cv2.waitKey(0)
#plt.show()
#cv2.imshow('h',edges)
#cv2.waitKey(0)
# Find contours for image, which will detect all the boxes

edges = cv2.imread('fin.png',0)

contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Sort all the contours by top to bottom.
#(contours, boundingBoxes) = sort_contours(contours, method="top-to-bottom")
cropped_dir_path = 'hackathon_images/'
idx = 0
for c in contours:
        # Returns the location and width,height for every contour
    x, y, w, h = cv2.boundingRect(c)
    if (w > 100 and h > 15) and w > 3*h:
        idx += 1
        new_img = img[y-10:y+h+10, x-10:x+w+10]
        cv2.imwrite(cropped_dir_path+str(idx) + '.png', new_img)

# If the box height is greater then 20, widht is >80, then only save it as a box in "cropped/" folder.
    if (w > 100 and h > 15) and w > 3*h:
        idx += 1
        new_img = img[y-10:y+h+10, x-10:x+w+10]
        cv2.imwrite(cropped_dir_path+str(idx) + '.png', new_img)