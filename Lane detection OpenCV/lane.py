import cv2
import numpy as np
import matplotlib.pyplot as plt

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



cap=cv2.VideoCapture(0)   #enter source of video
while (cap.isOpened()):
    _,frame=cap.read()
    canny=canny_image(frame)

    ceopped_image=roi(canny)

    line=cv2.HoughLinesP(ceopped_image,2,np.pi/180,50,np.array([]),minLineLength=100,maxLineGap=5) #the second and third argument of this function helps to contribute the size of 2D grid that is used
                                                                                                   #second argument is rho(or number of rows) and the third argument is thetha(or number of coloumns)
                                                                                                   #here, we have 2,1 matrix, 2rows and 1 coloumn(1 radian)
    averaged_lines=average_slope_intercept(frame,line)
    line_image=display_lines(frame,averaged_lines)
    final=cv2.addWeighted(frame, 0.8, line_image, 1, 1)
    cv2.imshow("result",final)
    out.write(final)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
