import json


def create_person():
    new_person = {"First Name": "Anna",
                  "Last Name": "Ables",
                  "Age":35,
                  "Visit": ["1/1/2020","2/3/2020","3/15/2020"]
                  }
    return new_person
   

def output_json(my_dict):
    filename = "my_booleans.json" #chose a file name .json know encode in json string
    out_file = open(filename,"w") #open it as a write? file
    json.dump(my_dict, out_file) #dump "my_dict" into "out_file"
    out_file.close() #close out_file make sure nothing bad happens
    
    
    #force to close the files that dont need. just two different approaches,both work
def output_json_with(output_data):
    filename = "my_output.txt"
    with open(filename,"w") as out_file:
        json.dump(output_data, out_file)
    print("The output is finished")
    


def creat_list():
    return [True,False,True] #in json is true false true not capitalize



if __name__ == "__main__":
    data_to_output = creat_list()
    output_json(data_to_output)