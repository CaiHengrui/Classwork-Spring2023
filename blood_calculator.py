def interface():
    print("blood calculator")
    keep_running = True
    while keep_running:

        print("options:")
        print("1-HDL")
        print("2-LDL")
        print("3-Total Cholesterol")
        print("9-quit")
        choice = input("select an option：")
        if choice =="9":
            keep_running = False

            #new feature new branch
        elif choice =="1":
            HDL_driver()
        elif choice =="2":
            LDL_driver()
        elif choice =="3":
            TC_driver() 
    print("program ending")


def generic_input(test_name):
    value = input("Enter the {} value:".format(test_name))
    value = int(value)
    return value
    
def generic_output(test_name,test_value,test_analy):
    print ("the {} result of {} is considered {}"
        .format(test_name,test_value,test_analy))
    return




def HDL_driver(): 
    #HDL_input= HDL_input() same name problem
    HDL_in= generic_input("HDL")
    HDL_analy = HDL_analysis(HDL_in)
    generic_output("HDL",HDL_in,HDL_analy)


def LDL_driver():
    LDL_in=generic_input("LDL")
    LDL_analy=LDL_analysis(LDL_in)
    generic_output("LDL",LDL_in,LDL_analy)

def TC_driver():
    TC_in=generic_input("Total Cholesterol")
    TC_analy=TC_analysis(TC_in)
    generic_output("Total Cholesterol",TC_in,TC_analy)




# def HDL_input():
    # HDL_value = input("Enter the HDL result:")
    # HDL_value = int(HDL_value)
    # return HDL_value

# def LDL_input():
    # LDL_value= input("Enter the LDL result:")
    # LDL_value= int(LDL_value)    
    # return LDL_value

# def TC_input():
    # TC_value= input("Enter the Total Cholesterol result:")
    # TC_value= int(TC_value)    
    # return TC_value



def HDL_analysis(HDL_int):
    if HDL_int >= 60:
        answer = "Normal"
    elif 40 <= HDL_int < 60:
        answer = "Borderline low"
    else:
        answer = "low"
    return answer


def LDL_analysis(LDL_int):
    if LDL_int >=190:
        answer="very high"
    elif 160<= LDL_int<190:
        answer="high"
    elif 130<=LDL_int<160:
        answer="Boarderline high"
    else:
        answer="normal"    
    return answer

def TC_analysis(TC_int):
    if TC_int < 200:
        answer = "Normal"
    elif 200 <= TC_int < 240:
        answer = "Borderline high"
    else:
        answer = "high"
    return answer




def HDL_output(HDL_value,HDL_analy):
    print("The HDL result of {} is considered {}".format(HDL_value,HDL_analy))
    return


def LDL_output(LDL_value,LDL_analy):
    print("The LDL result of {} is considered {}".format(LDL_value,LDL_analy))
    return

def TC_output(TC_value,TC_analy):
    print("The Total Cholesterol result of {} is considered {}".format(TC_value,TC_analy))
    return

if __name__ == "__main__":
    interface()

# merge zhihou  checkout main  and pull