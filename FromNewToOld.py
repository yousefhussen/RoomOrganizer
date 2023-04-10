import math
from NewRoomModel import *
import json
import pygame
import numpy as np
def drawRects(majorAngle, minAngle,rects,walls_dimensions):
    WallRects=[]

    for pos, rect in enumerate(rects):
        angle = round((majorAngle+minAngle[pos])%360)

        if abs(angle) == 0 or abs(angle) == 180 or abs(angle)== 360:
            rect.width=walls_dimensions[pos][0]
            rect.height=1
            

        else:
            rect.width=1
            rect.height=walls_dimensions[pos][0]
            # return a list of rects not one  
        WallRects.append(pygame.Rect(rect.centerx-rect.width/2+rect.height/2,rect.centery-rect.height/2+rect.width/2,rect.width,rect.height))
    return WallRects
def drawRects2(majorAngle, RectAngle,rects,walls_dimensions):
    WallRects=[]
    
    for pos, rect in enumerate(rects):
        angle = round((majorAngle+RectAngle[pos])%360)


        if abs(angle) == 0 or abs(angle) == 180 or abs(angle)== 360:
            rect.width=walls_dimensions[pos][0]
            rect.height=walls_dimensions[pos][1]
            
        else:
            rect.width=walls_dimensions[pos][1]
            rect.height=walls_dimensions[pos][0]
            # return a list of rects not one  
        
        WallRects.append(pygame.Rect(rect.centerx-rect.width/2+rect.height/2,rect.centery-rect.height/2+rect.width/2,rect.width,rect.height))

        # print("first is chair:",WallRects[pos].center)
    return WallRects
            

def intitRoomShape(rotations,positions,dimensions,Categories,offsetX,offsetZ,scale_factor):
    WallsSurfaces=[]
    state3=positions
    state4 = []
    sumX=0
    sumZ=0
    TempWalls=[[pygame.Surface((0, 0))] for _ in range(len(dimensions))]
    for i in range(len(rotations)):
        # print(self.walls_dimensions[i][1])
        image_orig = pygame.Surface((dimensions[i][0], 1))
        image_orig.set_colorkey((0, 0, 0))
        # for making transparent background while rotating an image
        color = (55, 100, 0) if Categories[i]=="wall" else (0, 200, 0) if Categories[i]=="door" else (0, 0, 200)
        # fill the rectangle / surface with green color
        image_orig.fill(color)
        # creating a copy of orignal image for smooth rotation
        
        # define rect for placing the rectangle at the desired position
        rect = image_orig.get_rect()
        
        rect.center = ((positions[i][0]+offsetX)*scale_factor,
                    (positions[i][1]+offsetZ)*scale_factor)
        # keep rotating the rectangle until running is set to False

        # set FPS

        # clear the screen every time before drawing new objects

        # making a copy of the old center of the rectangle
        old_center = rect.center
        # defining angle of the rotation
        
        # rotating the orignal image
        
        TempWalls[i] = pygame.transform.rotate(image_orig, rotations[i])
        


        rect = TempWalls[i].get_rect()
        # set the rotated rectangle to the old center
        rect.center = old_center
        sumX+=rect.centerx
        sumZ+=rect.centery
        # drawing the rotated rectangle to the screen
        # self.screen.blit(new_image, rect)
        # TempWalls.append(TempWalls[i])

    pivot= (sumX/len(list(filter(lambda a: a =="wall", Categories))),sumZ/len(list(filter(lambda a: a =="wall", Categories))))

    # New x-coordinate = (x - a)*cos(θ) - (y - b)*sin(θ) + a

    # New y-coordinate = (x - a)*sin(θ) + (y - b)*cos(θ) + b
    for i in range(len(rotations)):
        rect = TempWalls[i].get_rect()
        rect.center = ((positions[i][0]+offsetX)*scale_factor,
                    (positions[i][1]+offsetZ)*scale_factor)
        
        old_center = rect.center
        TempWalls[i]= pygame.transform.rotate(TempWalls[i], 133.639+90)
        rect.center = old_center
        TempWalls[i].set_colorkey((0, 0, 0))
        

        x_coordinate = (rect.centerx - pivot[0])*math.cos(np.radians((133.639+90))) + (rect.centery - pivot[1])*math.sin(np.radians((133.639+90))) + pivot[0]

        
        z_coordinate = (rect.centerx - pivot[0])*math.sin(np.radians((133.639+90))) - (rect.centery - pivot[1])*math.cos(np.radians((133.639+90))) - pivot[1]

        rect.center=[(x_coordinate)-(TempWalls[i].get_width()/2-rect.width/2),((z_coordinate)*-1)-(TempWalls[i].get_height()/2-rect.height/2)]
        
        

        state3[i]=rect.center
        WallsSurfaces.append(TempWalls[i])
        state4.append(rect)

    return state3,state4,WallsSurfaces,pivot
def intitFurnitureShape(rotations,positions,dimensions,Categories,offsetX,offsetZ,scale_factor,pivot):
    WallsSurfaces=[]
    state3=positions
    state4 = []
    sumX=0
    sumZ=0
    TempWalls=[[pygame.Surface((0, 0))] for _ in range(len(dimensions))]
    for i in range(len(rotations)):
        # print(self.walls_dimensions[i][1])
        image_orig = pygame.Surface((dimensions[i][0], dimensions[i][1]))
        
        image_orig.set_colorkey((0, 0, 0))
        # for making transparent background while rotating an image
        color = (55, 100, 0) if Categories[i]=="wall" else (0, 200, 0) if Categories[i]=="door" else (0, 0, 200)
        # fill the rectangle / surface with green color
        image_orig.fill(color)
        # creating a copy of orignal image for smooth rotation
        
        # define rect for placing the rectangle at the desired position
        rect = image_orig.get_rect()
        
        rect.center = ((positions[i][0]+offsetX)*scale_factor,
                    (positions[i][1]+offsetZ)*scale_factor)
        # keep rotating the rectangle until running is set to False

        # set FPS

        # clear the screen every time before drawing new objects

        # making a copy of the old center of the rectangle
        old_center = rect.center
        # defining angle of the rotation
        
        # rotating the orignal image
        
        TempWalls[i] = pygame.transform.rotate(image_orig, rotations[i])
        


        rect = TempWalls[i].get_rect()
        # set the rotated rectangle to the old center
        rect.center = old_center
        sumX+=rect.centerx
        sumZ+=rect.centery
        # drawing the rotated rectangle to the screen
        # self.screen.blit(new_image, rect)
        # TempWalls.append(TempWalls[i])



    # New x-coordinate = (x - a)*cos(θ) - (y - b)*sin(θ) + a

    # New y-coordinate = (x - a)*sin(θ) + (y - b)*cos(θ) + b
    for i in range(len(rotations)):
        rect = TempWalls[i].get_rect()
        rect.center = ((positions[i][0]+offsetX)*scale_factor,
                    (positions[i][1]+offsetZ)*scale_factor)
        
        old_center = rect.center
        TempWalls[i]= pygame.transform.rotate(TempWalls[i], 133.639+90)
        rect.center = old_center
        TempWalls[i].set_colorkey((0, 0, 0))
        

        x_coordinate = (rect.centerx - pivot[0])*math.cos(np.radians((133.639+90))) + (rect.centery - pivot[1])*math.sin(np.radians((133.639+90))) + pivot[0]

        
        z_coordinate = (rect.centerx - pivot[0])*math.sin(np.radians((133.639+90))) - (rect.centery - pivot[1])*math.cos(np.radians((133.639+90))) - pivot[1]
        
        rect.center=[(x_coordinate)-(TempWalls[i].get_width()/2-rect.width/2),((z_coordinate)*-1)-(TempWalls[i].get_height()/2-rect.height/2)]

        

        state3[i]=rect.center
        WallsSurfaces.append(TempWalls[i])
        state4.append(rect)

    return state3,state4,WallsSurfaces

def ExtractFurniturePosition(rects,angle,pivot):

    transform12=[]
    transform14=[]
    for pos,rect in enumerate(rects):
        print(pos,rect.center)
        
        x_coordinate = (rect.centerx - pivot[0])*math.cos(np.radians(-(133.639+90))) + (rect.centery - pivot[1])*math.sin(np.radians(-(133.639+90))) + pivot[0]

        
        z_coordinate = (rect.centerx - pivot[0])*math.sin(np.radians(-(133.639+90))) - (rect.centery - pivot[1])*math.cos(np.radians(-(133.639+90))) - pivot[1]
        print(pos,"x coord: ",x_coordinate,"z coord:",z_coordinate)
        transform12.append(x_coordinate)
        transform14.append(z_coordinate*-1)
    return transform12,transform14




def filter_list(lst, value):
    result = []
    for item in lst:
        if item.category == value:
            result.append(item)
    return result
def writeBack(Roomm):
    json_File =Room.to_dict(Roomm)
    # Closing file
    json_str=json.dumps(json_File)
    f2 = open('Output.json','w+')
    f2.write(str(json_str))
    f2.close()


def pre_processing(json_request=None):
    # Opening JSON file
    if(json_request==None):
        f = open('Output.json')

        # returns JSON object as 
        # a dictionary
        data = json.load(f)
        
        # Iterating through the json
        # list
        Room1 =Room.from_dict(data)

        # Closing file
        f.close()
    else:
        Room1 =Room.from_dict(json_request)
    wallsArray = Room1.surfaces
    FurnitureArray = Room1.objects
    FurnitureArray2=[[0 for elem in FurnitureArray],[0 for elem in FurnitureArray],[0 for elem in FurnitureArray]]

    wallsArray2=[[0 for elem in wallsArray],[0 for elem in wallsArray],[0 for elem in wallsArray]]
    MaxNegativeZ= 0
    MaxNegativeX= 0
    Keywords=[[0 for elem in wallsArray],[0 for elem in FurnitureArray]]
    MinAngle=float('inf')


    for pos,Wall in enumerate(wallsArray):
        transform = np.array(Wall.transform).reshape((4,4))

        # Extract the rotation matrix
        rotation = transform[:3, :3]
        # Compute the rotation angles (in degrees)
        
        y_angle = np.degrees(np.arctan2(rotation[2, 0], rotation[2, 2]))
    
        

        if MinAngle>=abs(y_angle):
            MinAngle=abs(y_angle)
        Keywords[0][pos]=Wall.category
        wallsArray2[0][pos]= [Wall.transform[12]*100,Wall.transform[14]*100]
        wallsArray2[1][pos]= [Wall.scale.x*100,2]
        wallsArray2[2][pos]=y_angle
        
        if MaxNegativeZ>Wall.transform[14]:
            MaxNegativeZ=Wall.transform[14]
        if MaxNegativeX>Wall.transform[12]:
            MaxNegativeX=Wall.transform[12]
        
    # rotations=[-43.6396,-133.639,46.3604,136.36,136.36,46.36]
    for i,furniture in enumerate(FurnitureArray):
        transform = np.array(furniture.transform).reshape((4,4))

        # Extract the rotation matrix
        rotation = transform[:3, :3]
        # Compute the rotation angles (in degrees)
        
        y_angle = np.degrees(np.arctan2(rotation[2, 0], rotation[2, 2]))


        

        if MinAngle>=abs(y_angle):
            MinAngle=abs(y_angle)

        Keywords[1][i]=furniture.category
        FurnitureArray2[0][i]= [furniture.transform[12]*100,furniture.transform[14]*100]
        FurnitureArray2[1][i]= [furniture.scale.x*100,furniture.scale.z*100]
        FurnitureArray2[2][i]=y_angle

    offsetZ= 0
    offsetX= 0


    state3,state4,Surfaces,pivot=intitRoomShape(wallsArray2[2],wallsArray2[0],wallsArray2[1],Keywords[0],offsetX,offsetZ,1)

    WallRects=drawRects((133.639+90), wallsArray2[2],state4,wallsArray2[1])

    state3,state4,Surfaces2=intitFurnitureShape(FurnitureArray2[2],FurnitureArray2[0],FurnitureArray2[1],Keywords[1],offsetX,offsetZ,1,pivot)
    FurnitureRects=drawRects2((133.639+90), FurnitureArray2[2],state4,FurnitureArray2[1])

    # from rect to number in array
    # adjusting rects


        
    # divid by 100 again 
    return FurnitureRects,WallRects,Keywords,FurnitureArray,Room1,pivot

