# eysip2020-37-ML-Self-Driving-Bot-App
THE FIRST SCRIPT:

The first script handles the job of lane detection on a image to get left and right lane and it also calculates the average of those lines to find the center of the lane. 
considering the vehicle is currently moving in the direction shown by the line which divides the image into two equal parts vertically we would be able to calculate the angle between the desirable and actual direction.
After calculating that we have to convert it into steering scale.We would a output between -90 to 90 which we would map to -1 to 1 in ackerman steering scale.
THE SECOND SCRIPT:

It invovles converting the things done on a particular image to work on a contious camera feed. The latest version had a function camera.listen inside to which we can call a function to process a image as soon as the camera listens to recieve a image.Inside this processing function all the things which were done inside the first script is done again to process the image to return the steering angle.
THE THIRD SCRIPT:

It is mostly the script for gaining data made by Gaurav only but small tweaks are made on it make it automatic and the functions used in the first script is used here.
