def increment_by_five(x):
    answer=x+5
    if answer == 15:
        print("bad input")
        return False
    return answer,True
        
        
y=increment_by_five(12)
print('The answer is {}'.format(y))
print(y[0])
print(y[1])

