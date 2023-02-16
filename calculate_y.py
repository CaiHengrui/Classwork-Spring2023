def calculate_y_on_line(coor1, coor2, x):
    x1, y1 = coor1
    x2, y2 = coor2
    if x1 == x2:
        return None
    slope = (y2 - y1) / (x2 - x1)
    y_intercept = y1 - slope * x1
    y = slope * x + y_intercept
    return y
    
    
    
if __name__ == '__main__':
    calculate_y_on_line()