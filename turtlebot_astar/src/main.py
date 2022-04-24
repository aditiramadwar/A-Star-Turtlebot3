from turtlebot_astar.astar import *
from turtlebot_astar.obstacle import check_inputs
from turtlebot_astar.utils import threshold, user_input
from turtlebot_astar.ros_utils import move_turtlebot
import time
radius = 0.033
wheel_distance = 0.89
thresholdDistance = 0.1
thresholdAngle = 15

######### Implement user input start and goal ##########
time.sleep(3)
start_in, goal_in, rpm1, rpm2, clearence = user_input()

actions = [[rpm1, 0],
            [0, rpm1],
            [rpm1, rpm1],
            [0, rpm2],
            [rpm2, 0],
            [rpm2, rpm2],
            [rpm1, rpm2],
            [rpm2, rpm1]]
start = threshold(start_in, thresholdDistance, thresholdAngle)
goal_node = threshold(goal_in, thresholdDistance, thresholdAngle)

if(check_inputs(start_in, goal_in, clearence)):
        print("Searching for optimal path.....")
        found_flag, parent_list, final_node, explored = a_star(start, goal_node, actions, thresholdDistance, thresholdAngle, radius, wheel_distance, clearence)

        if (found_flag):
            path = backtrack(parent_list, final_node, start)
            path.reverse()
            plot_map(start_in, goal_in, path, radius, wheel_distance, explored)
            move_turtlebot(path, radius, wheel_distance)
else:
    print("Invalid inputs, Enter new points!")


