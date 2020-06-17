# eysip2020-37-ML-Self-Driving-Bot-App
THE FIRST SCRIPT:

The first script handles the job of lane detection on a image to get left and right lane and it also calculates the average of those lines to find the center of the lane. 
considering the vehicle is currently moving in the direction shown by the line which divides the image into two equal parts vertically we would be able to calculate the angle between the desirable and actual direction.
After calculating that we have to convert it into steering scale.We would a output between -90 to 90 which we would map to -1 to 1 in ackerman steering scale.

THE SECOND SCRIPT:

It invovles converting the things done on a particular image to work on a contious camera feed. The latest version had a function camera.listen inside to which we can call a function to process a image as soon as the camera listens to recieve a image.Inside this processing function all the things which were done inside the first script is done again to process the image to return the steering angle.

THE THIRD SCRIPT:

It is mostly the script for gaining data made by Gaurav only but small tweaks are made on it make it automatic and the functions used in the first script is used here.

THE FOURTH SCRIPT:

This script uses select ROI for choosing bounding boxes for lane. Then TrackerTLD is created and initialised with this bounding box and its corresponding image.Then we get centre of the bounding box everytime the image changes and the tracker gets updated.Then with center and the midpoint of the bottom line of the image(width/2,height) is used to create a line then the angle between this line and Y axis found.It is in the range of -90 to 90 then angle is mapped to -1 to 1 to give the steering value.

THE FIFTH SCRIPT:

The fifth script invovles addition of another Tracker for object detection so that the vehicle can move away from it.
The above method used in Fourth script is used for getting steering values from the object detector(Note: it is important to note that the steering value we get from the object detector is not the value we should cause if the object is in say left then it would give only negative  steering value which would make the bot to move in left direction but that is not needed).if the object detector cant detect anything or the area of the bounding box of object detector is less than the AREA THRESHOLD then steering value given by lane dtector will be used if the area is above threshold then if value by object detector is less than the POSITION THRESHOLD then negative of the value given by object dtector will be fed to the bot/ vehicle if it is above the POSITION THRESHOLD then value from lane detector will be used.

AREA THRESHOLD:
The area threshold is dtermined by keeping the object at a save distance from the bot then its area is caluculated.If the area is above this threshold which means the object is neare to the bot than save distance so it is a danger and the bot should move away from it.

POSITION THREHOLD:
this threshold determines whether the object is within the lane or not . If a object is not within the lane then we need not worry about it.

