class Patient:

    def __init__(self):
        self.first_name = ""
        self.lsat_name = ""
        self.mrn = 0
        self.age = 0
        self.tests = []
        
        
def main():
    new_patient = Patient() # run the class called Patient
    second_patient = Patient()
    print(new_patient)
    print(second_patient)
    
    
if __name__ == "__main__":
    main()
    
    
# $ python database_class.py
# <__main__.Patient object at 0x00000286D8CAFFD0> 
# print out the fact and give the memory location

# $ python database_class.py
# <__main__.Patient object at 0x000001C1C11CFFD0>
# <__main__.Patient object at 0x000001C1C11CFEB0>

 