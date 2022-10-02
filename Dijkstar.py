# dijstar algo
###as it is taking tooo much colour I resized the image and applied thresholding
import numpy as np
import cv2
from collections import deque

#colour definition
white =[255,255,255]
black = [0,0,0]
green= [0,255,0]
blue = [255,0,0]
red = [0,0,255]

img=cv2.imread('Map Task-1 Part-2.png',cv2.IMREAD_COLOR)
print(img.shape)
img=cv2.resize(img,(411,259))
print(img.shape)
l,w,t=img.shape
for i in range (img.shape[0]):
    for j in range (img.shape [1]):
        if ((img[i][j])>0).all():
            img[i][j][0]=255
            img[i][j][1]=255
            img[i][j][2]=255
            cv2.imshow('image',img)
            cv2.waitKey(1)
start =(48,293)
end=(188,120)

def calcDist(point,current):
    return (point[0]-current[0])**2+(point[1]-current[1])**2

def iswell(img,x,y):
    return (x>=0 and x<img.shape[0] and y>=0 and y < img.shape[1])

def dijkstra(img,start,end):
    h,w,t =img.shape
    dist=np.full((h,w),fill_value=np.inf)
    dist[start]=0

    parent=np.zeros((h,w,2))
    visited=np.zeros((h,w))
    current=start
    visited[start]=1
    while current !=end :
        # print(current)
        visited[current]=1
        for i in range (-1,2):
            for j in range (-1,2):
                point = (current[0]+i,current[1]+j)
                if iswell(img,point[0],point[1]) and visited[point] !=1 and img[point][0]==white[0] and img[point][1]==white[1]and img[point][2]==white[2]:
                    if calcDist(point,current)+dist[current]<dist[point]:
                        dist[point]=calcDist(point,current)+dist[current]
                        parent[point[0],point[1]]=[current[0],current[1]]
        min= np.inf
        for i in range (h):
            for j in range (w):
                if min>dist[i,j] and visited[i,j]!=1:
                    min = dist[i,j]
                    current=(i,j)

    showPath(img,current,start ,parent)

def showPath(img,current,start , parent):
    new=np.copy(img)
    while current !=start :
        var=int(parent[current][0]),int (parent[current][1])
        new[int(var[0]),int(var[1])]=green
        current=(var[0],var[1])
        cv2.namedWindow('window',cv2.WINDOW_NORMAL)
        cv2.imshow('window',new)
        cv2.waitKey(0)

dijkstra(img,start,end)