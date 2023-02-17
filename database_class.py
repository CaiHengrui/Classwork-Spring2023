class Patient:

    def __init__(self):
        self.first_name = ""
        self.lsat_name = ""    #like a container
        self.mrn = 0
        self.age = 0
        self.tests = []
        
        
def main():
    new_patient = Patient() # run the class called Patient
    second_patient = Patient()
    print(new_patient)
    print(second_patient)
    new_patient.first_name = "David"
    new_patient.last_name = "Ward"
    new_patient.tests.append(("HDL", 100))
    print(new_patient.first_name)
    print(new_patient.last_name)
    print(new_patient.tests)
    print(second_patient.first_name)#这个打不出来因为本来self里面就是空的，别的不会改变self里的设置
    
    
if __name__ == "__main__":
    main()
    
    
# $ python database_class.py
# <__main__.Patient object at 0x0000024BDBE5FFD0>
# <__main__.Patient object at 0x0000024BDBE5FEE0>
# David
# Ward

#Grouping all of the variables as part of the Class

