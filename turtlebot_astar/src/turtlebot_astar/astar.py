
from queue import PriorityQueue
from turtlebot_astar.obstacle import obstacle
from turtlebot_astar.utils import *
from turtlebot_astar.neighbours import cost

def a_star(start, goal_node, actions, thresholdDistance, thresholdAngle, radius, wheel_distance, clearence):

    scale = int(1/thresholdDistance)  #100
    scale_dir = 10*scale  #1000
    scale_ang = int(360/thresholdAngle)  #36
    goal_threshold = 0.25

    visited = np.array(np.zeros((scale_dir, scale_dir, scale_ang)))
    cost_to_come = np.array(np.ones((scale_dir, scale_dir, scale_ang)) * np.inf)
    cost_matrix = np.array(np.ones((scale_dir, scale_dir, scale_ang)) * np.inf)

    explored=[]
    parent={}
    que = PriorityQueue()
    que.put((cost_to_go(start, goal_node), start))

    cost_matrix[int(start[0]),int(start[1]),start[2]] = cost_to_go(start, goal_node)
    cost_to_come[int(start[0]),int(start[1]),start[2]] = 0
    ###################### A-STAR ##################################
    while (not que.empty()):
        _, current_node = que.get()
        if checkGoalReached(current_node,goal_node, goal_threshold):
            print("Path Found!")
            print(current_node)
            return True, parent, [current_node, 0], explored
        cur_th = (int(scale*current_node[0]),int(scale*current_node[1]),current_node[2])
        for action in actions:
            child = cost(current_node[0], current_node[1], current_node[2], action[0], action[1], thresholdAngle, radius, wheel_distance)
            
            if(child==None):
                continue
            cur_child_node, child_cost = child
            child_node = threshold(cur_child_node, thresholdDistance, thresholdAngle)

            child_th = (int(scale*child_node[0]),int(scale*child_node[1]),child_node[2])
            if checkGoalReached(child_node, goal_node, goal_threshold):
                print("Path Found!")
                parent[child_node] = [current_node, action]
                print(child_node)
                return True, parent, [child_node, action], explored
            flag = obstacle(child_node[0],child_node[1], clearence)

            child_th = (int(child_node[0]),int(child_node[1]),child_node[2])
            cur_th = (int(current_node[0]),int(current_node[1]),current_node[2])
            if (flag == 1):
                if visited[child_th] == 0:
                    visited[child_th] = 1
                    explored.append([current_node, action, child_node])
                    parent[child_node]=[current_node, action]
                    cost_to_come[child_th]=child_cost + cost_to_come[cur_th]
                    cost_matrix[child_th]=cost_to_come[child_th] + cost_to_go(child_node, goal_node)
                    que.put((cost_matrix[child_th] ,child_node))
                else:
                    if cost_matrix[child_th] > child_cost + cost_to_come[cur_th] + cost_to_go(child_node, goal_node):#cost_matrix[cur_th] + sum(action):
                        cost_to_come[child_th] = child_cost + cost_to_come[cur_th]
                        cost_matrix[child_th] = cost_to_come[child_th] + cost_to_go(child_node, goal_node)
                        # cost_matrix[child_th] = cost_matrix[cur_th] + sum(action)
                        parent[child_node] = [current_node, action]
    print("No path found")
    return False, parent, [current_node, 0], explored

def backtrack(parent_list, goal, start):
    path=[]
    node = goal
    while (node[0] != start):
        node = parent_list[node[0]]
        path.append(node)
    return path
