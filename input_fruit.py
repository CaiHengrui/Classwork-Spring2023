# in_file = open("input_data.txt", "r") #the string is the file name you want to open( the file is in the main). If it is in another  floder,u have to give the name in that folder: "data/input_data.txt" or put in an absolute path "C:\users\daw\calss_repos\input_data.txt"
# #"/" and "\"
# #But if u want to share it ,it won't work.
# #Relative reference to u current path
# #make sure your input foler is in the same folder of u python code

# #'r' for read  'w' for write  'a' for pin to?
# fruits = in_file.readlines() #数据大时，全read 再操作比较好
# print(fruits)
# in_file.close()


# in_file = open("input_data.txt", "r") #look for the data I want
# for line in in_file:
    # print(line) #read in line by line?

# # or
# first_fruit = in_file.readline() # can't go back to read it again without closing the file and reopen it
# second_fruit = in_line.readline() #read single line in the file



    in_file = open("input_file.txt", "r")
    first_line = in_file.readline()
    patient_data = first_line.strip("\n").split("=") # 去掉后面的换行，从=分开
    patient_id = int(patient_data[1])
