
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import math
def node_th(node, th):
    return (int(th*node[0]), int(th*node[1]), node[2])

def threshold(Node, thresh_coord, thresh_angle):
    x,y,t = Node[0],Node[1],Node[2]
    x = round(x/thresh_coord)* thresh_coord
    y = round(y/thresh_coord)* thresh_coord
    t = round(t/thresh_angle) * thresh_angle
    x=round(x,4)
    y=round(y,4)
    n=t//360
    t=t-(360*n)
    t=(t/thresh_angle)
    return (x, y, int(t))

def cost_to_go(curr, goal):
    c2g = ((curr[0]-goal[0])**2 + (curr[1]-goal[1])**2)**0.5
    return  c2g

def checkGoalReached(current_node, goal_state, thresh_radius):
    return np.square(current_node[0] - goal_state[0]) + np.square(current_node[1] - goal_state[1])<= thresh_radius**2

def user_input():
    print("Enter choice : ")
    print("(1) Enter points manually ")
    print("(2) Default parameters")
    choice = input()

    if choice == '1':
        print("Enter Clearence, eg = 0.5:")
        clearence = input()
        print("Enter RPM1, eg = 2:")
        rpm1 = input()
        print("Enter RPM2, eg = 3:")
        rpm2 = input()
        print("Enter source points as X,Y,theta eg = 4, 0.5, 0 :")
        start_input = input()
        start_input_x = float(start_input.split(",")[0])
        start_input_y = float(start_input.split(",")[1])
        start_input_theta = int(start_input.split(",")[2])
        print("Enter destination points as X,Y eg = 4, 8:")
        goal_input = input()
        goal_x = float(goal_input.split(",")[0])
        goal_y = float(goal_input.split(",")[1])
        start_in = (float(start_input_x), float(start_input_y), int(start_input_theta))
        goal_in = (float(goal_x), float(goal_y), int(0))
    else:
        start_in = (float(1), float(1), int(0))
        goal_in = (float(9), float(9), int(15))
        clearence = 0.3
        rpm1 = 2
        rpm2 = 3

    return start_in, goal_in, rpm1, rpm2, clearence

def plot_map(start_in, goal_node, path, radius, wheel_distance, explored):
        # node = start_in
        fig, ax = plt.subplots()
        ax.set(xlim=(0, 10), ylim=(0, 10))

        plt.plot(start_in[0], start_in[1], color='green', marker='o', linestyle='dashed', linewidth=1,markersize=4)
        plt.plot(goal_node[0], goal_node[1], color='red', marker='o', linestyle='dashed', linewidth=1,markersize=4)
        c1 = plt.Circle((2, 8), 1, fill=True)
        c2 = plt.Circle((2, 2), 1, fill=True)
        currentAxis = plt.gca()
        currentAxis.add_patch(Rectangle((0.25, 4.25), 1.5, 1.5, fill=True, alpha=1))
        currentAxis.add_patch(Rectangle((3.75, 4.25), 2.5, 1.5, fill=True, alpha=1))
        currentAxis.add_patch(Rectangle((7.25, 2), 1.5, 2, fill=True, alpha=1))
        currentAxis.add_patch(Rectangle((0, 0), 10, 10, fill=None, alpha=1))
        
        ax.add_artist(c1)
        ax.add_artist(c2)
        ax.set_aspect('equal')

        plt.grid()
        # current_node, action, child_node
        for current_node, action, child_node in explored:
            # print(action)
            Xn, Yn, Thetai = current_node
            Thetan = math.radians(Thetai*15)
            # print(Thetan)
            UL = action[0]
            UR = action[1]
            t = 0
            while t<10:
                t += 1
                Xs = Xn
                Ys = Yn
                Xn += (0.5*radius) * (UL + UR) * math.cos(Thetan)
                Yn += (0.5*radius) * (UL + UR) * math.sin(Thetan)
                Thetan += (radius / wheel_distance) * (UR - UL)
                plt.plot([Xs, Xn], [Ys, Yn], color="green")
            plt.pause(0.001)
                # plt.show()

        for node, action in path:
            # print(action)
            Xn, Yn, Thetai = node
            Thetan = math.radians(Thetai*15)
            # print(Thetan)
            UL = action[0]
            UR = action[1]
            t = 0
            while t<10:
                t += 1
                Xs = Xn
                Ys = Yn
                Xn += (0.5*radius) * (UL + UR) * math.cos(Thetan)
                Yn += (0.5*radius) * (UL + UR) * math.sin(Thetan)
                Thetan += (radius / wheel_distance) * (UR - UL)
                plt.plot([Xs, Xn], [Ys, Yn], color="red")
            plt.pause(0.001)

        # Xn, Yn, Thetai  = start_in
        # Thetan = math.radians(Thetai)
        # for node, action in path:
        #     UL= action[0]
        #     UR = action[1]
        #     t = 0
        #     while t<10:
        #         t += 1
        #         Xs = Xn
        #         Ys = Yn
        #         Xn += (0.5*radius) * (UL + UR) * math.cos(Thetan)
        #         Yn += (0.5*radius) * (UL + UR) * math.sin(Thetan)
        #         Thetan += (radius / wheel_distance) * (UR - UL)
        #         plt.plot([Xs, Xn], [Ys, Yn], color="red")

        plt.show()
        plt.pause(1)
        plt.close()
