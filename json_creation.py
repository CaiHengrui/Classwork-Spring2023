import json


def create_person():
    new_person = {"First Name": "Anna",
                  "Last Name": "Ables",
                  "Age":35,
                  "Visit": ["1/1/2020","2/3/2020","3/15/2020"]
                  }
    return new_person
   

def output_json(my_dict):
    filename = "patient.json" #chose a file name .json know encode in json string
    out_file = open(filename,"w") #open it as a write? file
    json.dump(my_dict, out_file) #dump "my_dict" into "out_file"
    out_file.close() #close out_file make sure nothing bad happens
    





if __name__ == "__main__":
    person = create_person()
    print (person)
    output_json(person)