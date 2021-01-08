# Customized-Training-Data-for-Eye-Tracking-on-screen

- Need python >= 3.7

run 
```
sh setup.sh
```

# Data

For each camera with different capture image dimensions there will be different data files.
Each file is saved with the dimensions of the camera that is recording in csv format.
Each row of each data file in csv format will contain the arrays of the captured image (according to the dimensions of the captured image) and each
value of these arrays are separated by the ";" symbol. After each array value, there will be 2 more values always separated by the ";" symbol indicating
the x axis and y axis on the screen of where your eyes where looking.

So, for example if your camera is recording with this image dimension 2 rows, 3 cols, 3 channels, each line of the data file
2_3_3.csv will be:

value1;value2;value3;value4;value5;value6;value7;value8;value9;value10;value11;value12;value13;value14;value15;value16;value17;value18;x_axis;y_axis;\n

# How it should work

You have to click the circles on the screen until they disappear, in this way your are focusing your eyes on a memorized region of the screen
and while you click on the circle the camera will capture the image, so be sure your camera can see your face.


So for e
