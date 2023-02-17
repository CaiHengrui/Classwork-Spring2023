class Patient:
## Grouping all of the variables as part of the Class
## and grouping all the function that act on this variables
    def __init__(self, patient_first_name,
                 patient_last_name,
                 patient_mrn,
                 patient_age):
        self.first_name = patient_first_name
        self.last_name = patient_last_name
        self.mrn = patient_mrn
        self.age = patient_age
        self.tests = []
        
        
        
    def get_full_name(self):
        full_name = "{} {}".format(self.first_name,
                                   self.last_name)
        return full_name

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False        
        
def main():
    new_patient = Patient("Ann", "Ables", 1, 34) # another way to run the class called Patient
    second_patient = Patient("Bob", "Boyles", 2, 45)
    
    print(new_patient)
    print(second_patient)
    # new_patient.first_name = "David"
    # new_patient.last_name = "Ward"
    new_patient.tests.append(("HDL", 100))
    print(new_patient.first_name)
    print(new_patient.last_name)
    print(new_patient.tests)
    print(second_patient.first_name)#这个打不出来因为本来self里面就是空的，别的不会改变self里的设置
    
    print(new_patient.get_full_name())#
    
    
    print(new_patient.is_adult())
    
    
if __name__ == "__main__":
    main()
    
    
# $ python database_class.py
# <__main__.Patient object at 0x0000024BDBE5FFD0>
# <__main__.Patient object at 0x0000024BDBE5FEE0>
# David
# Ward

