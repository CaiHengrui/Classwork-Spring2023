
def calculate_driver():
    x1,x2 = coordinate1_input()
    y1,y2 = coordinate2_input()
    print(x1,y1)  
    print(x2,y2)
    if x1 == x2:
        return None
    else:
        s = calculate_slope(x1,x2,y1,y2)
        y_i = calculate_y_intercept(s,x1,y1)
        new_x = input_new_x()
        y_final =  calculate_y_on_line(s, new_x,y_i)
        ouput(y_final)
        
    print("program ending")
    
def coordinate1_input():
    x1 = float(input("Enter the x of the first coordinate:"))
    x2 = float(input("Enter the x of the second coordinate:"))
    
   
    return x1,x2
    
def coordinate2_input():
    y1 = float(input("Enter the y of the first coordinate:"))
    y2 = float(input("Enter the y of the second coordinate:"))
    
    return y1,y2


def calculate_slope(x1,x2,y1,y2):
    
    slope = (y2 - y1) / (x2 - x1)
    return slope
    

def calculate_y_intercept(slope,x1,y1):
    y_intercept = y1 - slope * x1
    return y_intercept
    
def input_new_x():
    x_new= float(input("Enter the x of the new coordinate:"))
    return x_new
    
def calculate_y_on_line(slope, x, y_inter):
    y = slope * x + y_inter
    return y

def ouput(y):
    print("the return value of y is:{}".format(y))
    
if __name__ == '__main__':
    calculate_driver()
    
    # calculate_y_on_line()
