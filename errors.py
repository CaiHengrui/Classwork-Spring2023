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
    print(calc_square_root(-4))
    
    # $ python errors.py
    # -4 
    # we need to tell the user sth about hey u didnt do it correctly




    
if __name__ == "__main__":
    main()