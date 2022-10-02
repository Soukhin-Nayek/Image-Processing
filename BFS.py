#map 1 analysis using bsf
# it is same code that of part 1 only the image and starting and ending point is different

import cv2
from collections import deque

img1=cv2.imread('Map Task-1 Part-2.png',1)
img=cv2.imread('Map Task-1 Part-2.png',1)
print(img1.shape)

red=[0,0,255]
green=[0,255,0]
white=[255,255,255]
blue=[255,0,0]
grey=[127,127,127]
black =[0,0,0]
global m,l
m,l=359,563
class Node():
    def __init__(self,index,parent):
        self.x=index[0]
        self.y=index[1]
        self.parent=parent

def show_path(end,start):
    print('e',end.x,end.y)
    print('s',start.x,start.y)
    current=end
    while(current != start ):
        img[current.x][current.y]=green
        current=current.parent

def bfs(start):
    q=deque()
    q.append(start)
    cv2.namedWindow('path',cv2.WINDOW_NORMAL)
    while len(q):
        current=q.popleft()
        i,j =current.x,current.y
        if i == l and j == m :
            break
        cv2.imshow('path',img)
        cv2.waitKey(1)

        if j + 1 < img.shape[1]:
            if (img[i][j + 1] != black).any() and (img[i][j + 1] != grey).any():
                if i==l and j == m:
                    break
                img[i][j+1]=grey
                n=Node((i,j+1),current)
                q.append(n)

        if i+1 <img.shape[0]:
            if (img[i+1][j] != black).any() and (img[i+1][j] !=grey).any():
                if i==l and j == m:
                    break
                img[i+1][j]=grey
                n=Node((i+1,j),current)
                q.append(n)

        if j-1 >0 :
            if (img[i][j-1] != black).any() and (img[i][j-1] !=grey).any():
                if i==l and j == m:
                    break
                img[i][j-1]=grey
                n=Node((i,j-1),current)
                q.append(n)

        if i-1 >0:
            if (img[i-1][j] != black).any() and (img[i-1][j] !=grey).any():
                if i==l and j == m:
                    break
                img[i-1][j]=grey
                n=Node((i-1,j),current)
                q.append(n)

    show_path(current,start)

start=Node((145,880),None)
bfs(start)

print("done!")
cv2.namedWindow('final',cv2.WINDOW_NORMAL)
cv2.imshow('final',img)
cv2.waitKey(0)