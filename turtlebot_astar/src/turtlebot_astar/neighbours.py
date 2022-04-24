import math
from turtlebot_astar.obstacle import obstacle
from turtlebot_astar.utils import cost_to_go
def cost(Xi, Yi, Thetai, UL, UR, thresholdAngle, radius, wheel_distance):
    t = 0
    Delta_Xn = Xi
    Delta_Yn = Yi
    Thetan = math.radians(Thetai*thresholdAngle)
# Xi, Yi,Thetai: Input point's coordinates
# Xs, Ys: Start point coordinates for plot function
# Xn, Yn, Thetan: End point coordintes
    D = 0
    while t < 10:
        t += 1
        Xs = Delta_Xn
        Ys = Delta_Yn
        Delta_Xn += 0.5*radius * (UL + UR) * math.cos(Thetan)
        Delta_Yn += 0.5*radius * (UL + UR) * math.sin(Thetan)
        Thetan += (radius / wheel_distance) * (UR - UL)
        D += cost_to_go([Xs, Ys], [Delta_Xn, Delta_Yn])
        flag = obstacle(Delta_Xn,Delta_Yn, 0.1)

        if (flag != 1):
            return None
    Thetan = math.degrees(Thetan)
    return (Delta_Xn, Delta_Yn, Thetan), D
    