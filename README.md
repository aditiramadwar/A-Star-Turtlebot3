


# A Star  Path Planning on Turtlebot
Authors:

 - Arunava Basu
 - Aditi Ramadwar

This project utilizes the A Star algorithm to find the shortest optimal path between two points in a given map of obstacles.
The map is defined as follows : 
  
<p align="center">

<img  alt="map1"  src="turtlebot_astar/results/map1.png"  width="75%" />

</p>
<p align="center">

<img  alt="map"  src="turtlebot_astar/results/map.png"  width="75%" />

</p>

## Steps to run the program

To run the program enter this command in a terminal :
 

    roslaunch turtlebot_astar gazebo_.launch  x_pos:=-4 y_pos:=-4
   

## [Gazebo Output](https://drive.google.com/file/d/1fTHATY70mAmW86jeslcLVCxxvLCsoOOm/view?usp=sharing)



The output image shows the path found. 

 - The explored vectors are shown in green during the search
 - The optimal path is shown in red 
 - Yellow is the goal
 - Blue is the start point


<p align="center">

<img  alt="result"  src="turtlebot_astar/results/path.gif"  width="75%" />

</p>

