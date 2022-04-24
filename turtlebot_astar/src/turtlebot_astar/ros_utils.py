import math
import rospy
from geometry_msgs.msg import Twist
def velocity_inputs(UL, UR, radius, wheel_distance):
    r = radius
    L = wheel_distance
    rpm_UL = UL*2*math.pi/60
    rpm_UR = UR*2*math.pi/60
    theta_dot = (r / L) * (rpm_UR - rpm_UL) 
    vel_mag = (r / 2) * (rpm_UL + rpm_UR)
    return vel_mag, theta_dot

def move_turtlebot(path, radius, wheel_distance):
    msg = Twist()
    rospy.init_node('robot_talker', anonymous=True)
    velPub = rospy.Publisher('cmd_vel', Twist, queue_size=100)
    msg.linear.x = 0.0
    msg.angular.z = 0.0
    velPub.publish(msg)
    ros=[]
    for i in range (len(path)):
        ros.append(path[i][1])
    c = 0
    r = rospy.Rate(10)
    for action in ros:
        print("action:", action)
        while not rospy.is_shutdown():
            if c == 101:
                msg.linear.x = 0
                msg.angular.z = 0
                velPub.publish(msg)
                break
            else:
                vel, th = velocity_inputs(action[0],action[1], radius, wheel_distance)
                msg.linear.x = vel*10
                msg.angular.z =  th*10
                velPub.publish(msg)
                c += 1
                r.sleep()
        c = 0
