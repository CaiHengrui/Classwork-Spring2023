# def my_function(n):
    #create an error
    
    #IndexError: list index out of range
    # x = [1, 2, 3, 4]
    # x[len(x)]
    
    #UnboundLocalError: local variable 'c' referenced before assignment
    # a =2 
    # b =3
    # c = a + b + c
    
    #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
    # "a"**2
    
    #ZeroDivisionError: division by zero
    # 2 / 0
    
    #ModuleNotFoundError: No module named 'my_cal'
    # from my_cal import sqrt
    # answer = aqrt(n)
    # return answer
    
    # try:
        # from my_cal import sqrt
    # except ModuleNotFoundError:
        # from math import sqrt
    
    # answer = sqrt(n)
    # return answer
    
    
def calc_square_root(n):

    try:
        from my_math_calculator import sqrt #
    except ModuleNotFoundError:
        from math import sqrt

    answer = sqrt(n)
    return answer


# # def main():
    # # print(calc_square_root(4))
    
 # # $ python errors.py
 # # 2.0000000929222947
   
   
def main():
    # x = "4"
    # x = -4
    x = 9
    # There was no error
# 3.000000001396984

    try: #try block can do any amount of code in it but better be specific
        answer = calc_square_root(x)
        x = answer + 5
        if x > 10: # if any of this lines causes a error, it will jump down into other blocks
            go here
    except TypeError:  # x = "4"
        new_x = int(x)
        answer = calc_square_root(new_x)
    except ValueError: # x = -4
        print("You must send a number")
        answer = ""
    except:
        print("All errors")#it is not good but sometimes u need to make codes ruuning
    print(answer)
        
    # $ python errors.py
    # -4 
    # we need to tell the user sth about hey u didnt do it correctly


#To capture all error 

    
if __name__ == "__main__":
    main()