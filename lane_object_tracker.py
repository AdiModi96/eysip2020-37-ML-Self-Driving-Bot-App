import cv2
import numpy as np
import matplotlib.pyplot as plt
import math


def drawBox(img,bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    X, Y = int(x+w/2) , int(y+ h/2) 
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 3 )
    cv2.circle(img, (X,Y), 2, (255,0,0),-1)
    cv2.line(img, (X,Y), (int(img.shape[1]/2),img.shape[0]), (0,255,0))
    if (X - (img.shape[1]/2)) != 0: 
        theta = math.atan((Y-img.shape[0])/(X - (img.shape[1]/2)))
    else:
        theta = 0
    theta = theta*180/math.pi
    if theta>0:
        theta = -(90 - theta)
    else:
        theta = (90 + theta)
    steer = theta/90
    cv2.putText(img, str(steer), (320, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
def drawBox1(img,bbox,bbox1):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    X, Y = int(x+w/2) , int(y+ h/2)
    x1, y1, w1, h1 = int(bbox1[0]), int(bbox1[1]), int(bbox1[2]), int(bbox1[3])
    X1, Y1 = int(x1+w1/2) , int(y1+ h1/2)
    a = w1*h1
    
    if (X - (img.shape[1]/2)) != 0: 
        theta = math.atan((Y-img.shape[0])/(X - (img.shape[1]/2)))
    else:
        theta = 0
    theta = theta*180/math.pi
    if theta>0:
        theta = -(90 - theta)
    else:
        theta = (90 + theta)
    steer = theta/90
    cv2.putText(img, str(steer), (320, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    if a>600:
        if (X1 - (img.shape[1]/2)) != 0: 
            theta = math.atan((Y1-img.shape[0])/(X1 - (img.shape[1]/2)))
        else:
            theta = 0
        theta = theta*180/math.pi
        if theta>0:
            theta = -(90 - theta)
        else:
            theta = (90 + theta)
        steer1 = theta/90
        if abs(steer)<0.30:
            steer = -steer1
        cv2.putText(img, str(steer), (320, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 3 )
    cv2.circle(img, (X,Y), 2, (255,0,0),-1)
    cv2.line(img, (X,Y), (int(img.shape[1]/2),img.shape[0]), (0,255,0))
    cv2.rectangle(img, (x1, y1), ((x1 + w1), (y1 + h1)), (255, 0, 255), 3, 3 )
    cv2.circle(img, (X1,Y1), 2, (255,0,0),-1)
    cv2.line(img, (X1,Y1), (int(img.shape[1]/2),img.shape[0]), (0,0,255))


    

image=cv2.imread('test.jpg')
lane=np.copy(image)

def canny_image(image):                                         #function to get canny output
    grey=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    blur=cv2.GaussianBlur(grey,(5,5),0)
    canny=cv2.Canny(grey,0,30)
    return canny

def roi(image):                                                 #Defination of region of interest
    height=image.shape[0]
    triangles=np.array([[(0,height),(1100,height),(520,0)]])
    mask=np.zeros_like(image)
    cv2.fillPoly(mask,triangles,255)
    masked_image=cv2.bitwise_and(image,mask)
    return masked_image

def display_lines(images,lines):                               #function to display detected line
    line_image=np.zeros_like(images)
    if lines is not None:

        for line in lines:
            x1,y1,x2,y2=line.reshape(4)
            cv2.line(line_image,(x1,y1),(x2,y2),(0,255,0),10)
    return line_image

def make_cordinate(image,line_parameters):                   #get coordinates of line
    slope,intercept=line_parameters
    y1=image.shape[0]
    y2=int(y1*(3/5))
    x1=int((y1-intercept)/slope)
    x2=int((y2-intercept)/slope)
    return np.array([x1,y1,x2,y2])


def average_slope_intercept(image,lines):                      #Make a average line from many lines
    left_fit=[]
    right_fit=[]
    for line in lines:
        x1,y1,x2,y2=line.reshape(4)
        parameters=np.polyfit((x1,x2),(y1,y2),1)
        slope=parameters[0]
        intercept=parameters[1]
        if slope<0:
            left_fit.append((slope,intercept))
        else:
            right_fit.append((slope,intercept))
    average_left=np.average(left_fit,axis=0)
    average_right=np.average(right_fit,axis=0)
    left_line=make_cordinate(image,average_left)
    right_line=make_cordinate(image,average_right)
    return np.array([left_line,right_line])



cap=cv2.VideoCapture('video10.mp4')   #enter source of video
tracker = cv2.TrackerTLD_create()
print(type(tracker))
tracker1 = cv2.TrackerTLD_create()
frame = cv2.imread("G:\\CarlaSimulator\\resize1\\img0.jpg")
frame1 = cv2.imread("G:\\CarlaSimulator\\resize1\\img304.jpg")
bbox = cv2.selectROI("Tracking",frame, False)
bbox1 = cv2.selectROI("Tracking",frame1, False)

#bbox = (258, 430, 301, 74)
tracker.init(frame, bbox)
tracker1.init(frame1, bbox1)
print(tracker.init(frame, bbox))
count = 1
while count <=539:
    img = cv2.imread("G:\\CarlaSimulator\\resize1\\img" + str(count)+ ".jpg")
    # canny=canny_image(frame)

    # ceopped_image=roi(canny)

    # line=cv2.HoughLinesP(ceopped_image,2,np.pi/180,50,np.array([]),minLineLength=100,maxLineGap=5) #the second and third argument of this function helps to contribute the size of 2D grid that is used
    #                                                                                                #second argument is rho(or number of rows) and the third argument is thetha(or number of coloumns)
    #                                                                                                #here, we have 2,1 matrix, 2rows and 1 coloumn(1 radian)
    # averaged_lines=average_slope_intercept(frame,line)
    # line_image=display_lines(frame,averaged_lines)
    # final=cv2.addWeighted(frame, 0.8, line_image, 1, 1)
    timer = cv2.getTickCount()
    success, bbox = tracker.update(img) 
    success1,bbox1 = tracker1.update(img)
    if success:
        if not success1:
            drawBox(img,bbox)
            cv2.putText(img, "Lost", (100, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
 
        else:
            drawBox1(img,bbox, bbox1)
    cv2.rectangle(img,(15,15),(200,90),(255,0,255),2)
    cv2.putText(img, "Fps:", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,255), 2);
    cv2.putText(img, "Status:", (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2);
 
 
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
    if fps>60: myColor = (20,230,20)
    elif fps>20: myColor = (230,20,20)
    else: myColor = (20,20,230)
    cv2.putText(img,str(int(fps)), (75, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, myColor, 2);
    cv2.imshow("result",img)
    count = count + 1
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()