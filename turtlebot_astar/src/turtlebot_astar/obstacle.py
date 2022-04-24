x_c1 = 2
y_c1 = 8
############################################
x_c2 = 2
y_c2 = 2
rad = 1
############################################
x1_l = 0.25
y1_u = 5.75
y1_d = 4.25
x1_r = 1.75
############################################
y2_d = 4.25
y2_u = 5.75
x2_r = 6.25
x2_l = 3.75
############################################
y3_d = 2
y3_u = 4
x3_r = 8.75
x3_l = 7.25

def obstacle(x,y,tot):
    circle1 = ((x - x_c1) ** 2 + (y - y_c1) ** 2 - (rad + tot) ** 2) <= 0
    circle2 = ((x - x_c2) ** 2 + (y - y_c2) ** 2 - (rad + tot) ** 2) <= 0
    square1 = (((x1_l-tot - x) <= 0) and ((y1_u+tot - y) >= 0) and ((x1_r+tot - x) >= 0) and ((y1_d-tot - y) <= 0))
    square2 = (((x2_l-tot - x) <= 0) and ((y2_u+tot - y) >= 0) and ((x2_r+tot - x) >= 0) and ((y2_d-tot - y) <= 0))
    square3 = (((x3_l-tot - x) <= 0) and ((y3_u+tot - y) >= 0) and ((x3_r+tot - x) >= 0) and ((y3_d-tot - y) <= 0))
    boundry = (x<tot or y>=10-tot or y<tot or x>=10-tot)
    if circle1 or circle2 or square1 or square2 or square3 or boundry:
        return False
    else:
        return True
def check_inputs(start, goal, clearence):
    if( obstacle(start[0], start[1], clearence)):
        return obstacle(goal[0], goal[1], clearence)
    else:
        print("Start point in obstacle space")
        return False