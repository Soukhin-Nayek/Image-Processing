#using astar algo
import cv2
import numpy as np
img=cv2.imread('Map Task-1 Part-2.png')
img_copy=img.copy()

red=(0,0,255)
blue=(255,0,0)
white=(255,255,255)
black=(0,0,0)
green=(0,255,0)
orange=(0,128,255)

w,h,c=img.shape

class Node():
    def __init__(self,parent,position):
        self.parent=parent
        self.position =position
        self.g=np.inf
        self.h=np.inf
        self.f=np.inf

def get_position(p1,p2):
    return np.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def get_manhattan_distance(p1,p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])

def is_obstacle(p):
    x,y=p
    if img[x][y][0]==0 and img[x][y][1]==0 and img[x][y][2]==0:
        return True
    return False

def get_min_dist_node(open_list):
    min_dist=np.inf
    min_node=None
    for node in open_list:
        if open_list[node].f<min_dist:
            min_dist=open_list[node].f
            min_node=open_list[node]
    return min_node

def show_path(node):
    path=[]
    while node.parent is not None:
        path.append(node)
        node=node.parent
    path.reverse()
    for i in range(len(path)-1):
        print(path[i].position)
        img[path[i].position]=green
    cv2.imshow('path finding',img)
    cv2.waitKey(0)

def aster_algo(start,end):
    path_found=False
    print("aster algo ")
    open_list={}   # which are currently to be examined
    closed_list=[] #nodes whose children have been examined

    start_node=Node(None,start)
    start_node.g=0
    start_node.h=get_position(start_node.position,end)
    start_node.f=start_node.g+start_node.h
    open_list[start]=start_node
    while len(open_list)>0:
        current_node=get_min_dist_node(open_list)
        img[current_node.position[0],current_node.position[1]]=orange
        open_list.pop(current_node.position)

        if current_node.position==end:
            path_found=True
            print('path found')
            show_path(current_node)
            return

        for new_position in [(0,-1),(-1,0),(1,0),(0,1),(1,1),(-1,-1),(-1,1),(1,-1)]:
            node_position=(current_node.position[0]+new_position[0],current_node.position[1]+new_position[1])
            if node_position[0]>(w-1) or node_position[0]<0 or node_position[1]>(h-1) or node_position[1]<0:
                continue
            if is_obstacle(node_position):
                continue
            if node_position in closed_list:
                continue
            new_node=Node(current_node,node_position)
            new_node.g=current_node.g+get_position(current_node.position,new_node.position)
            new_node.h=get_position(new_node.position,end)
            new_node.f=new_node.g+new_node.h

            if node_position in open_list:
                if new_node.g<open_list[node_position].g:
                    open_list[node_position]=new_node

            else:
                open_list[node_position]=new_node

        closed_list.append(current_node.position)
        cv2.namedWindow('path',cv2.WINDOW_NORMAL)
        cv2.imshow('path',img)
        cv2.waitKey(1)
    if not path_found:
        print('path not found')

start=(145,880)
end=(563,359)
aster_algo(start,end)