# eysip2020-37-ML-Self-Driving-Bot-App
THE FIRST SCRIPT:
The first script handles the job of lane detection on a image to get left and right lane and it also calculates the average of those lines to find the center of the lane. 
considering the vehicle is currently moving in the direction shown by the line which divides the image into two equal parts vertically we would be able to calculate the angle between the desirable and actual direction.
After calculating that we have to convert it into steering scale.We would a output between -90 to 90 which we would map to -1 to 1 in ackerman steering scale.
THE SECOND SCRIPT:
