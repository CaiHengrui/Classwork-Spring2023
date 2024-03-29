import tkinter as tk
from tkinter import ttk
# from tkinter import *  (common but not recommended)
import requests
from PIL import Image, ImageTk
from tkinter import filedialog


def create_blood_string(blood_letter, rh):
    blood_string = "{}{}".format(blood_letter, rh)
    return blood_string


def id_number_verification(id_number):
    if 1 <= id_number <= 1000000:
        return True
    else:
        return False


def send_data_to_server(patient_name, id_number, blood_string,
                        donation_center):
    patient = {"id": id_number, "name": patient_name,
               "blood_type": blood_string}
    r = requests.post("http://127.0.0.1:5000/new_patient", json=patient)
    return r.text


def check_and_upload_data(patient_name, id_number, blood_letter, rh,
                          donation_center):
    blood_string = create_blood_string(blood_letter, rh)
    id_number = int(id_number)
    if id_number_verification(id_number) is False:
        return "ID number is incorrect"
    msg = send_data_to_server(patient_name, id_number, blood_string,
                              donation_center)
    return msg


def set_up_window():
    def ok_btn_cmd():
        print("Ok clicked")
        # 1.get infor from the GUI
        patient_name = name_value.get()
        id_number = id_value.get()
        blood_letter = blood_letter_value.get()
        rh = rh_factor_value.get()
        donation_center = donation_value.get()
        # 2.send data to other functions and do the work and are testable
        # msg = check_and_upload_data(patient_name, id_number, blood_letter, rh,
        #                             donation_center)
        # # 3.update the GUI
        # status_label.configure(text=msg)  # status_label = ttk.Label(root, text="")  # start with nothing
        # id_entry.configure(state=tk.DISABLED)  # 当ok被按时，禁用id_entry
        # print("Patient name is {}".format(patient_name))
        # print("Patient id is {}".format(id_number))
        # print("Patient blood type is {}{}".format(blood_letter, rh))
        # donation_combobox["values"] = ("A", "B", "C")  # click ok button will change list

    def cancel_btn_cmd():
        root.destroy()  #
        # id_entry.configure(state=tk.NORMAL)  # 恢复禁用

    def change_label_color():
        current_color = top_label.cget("foreground")  # 获取top_label的当前颜色状态
        if current_color == "":
            color = "black"
        else:
            color = current_color.string  # 获取当前颜色的字符串值
        if color == "black":
            new_color = "red"
        else:
            new_color = "black"
        top_label.configure(foreground=new_color)
        root.after(1000, change_label_color)  # 重新call这个function

    def shuffle_choices():
        current_choices = list(donation_combobox.cget("values"))
        import random
        random.shuffle(current_choices)
        donation_combobox.configure(values=current_choices)

    def change_image_cmd():
        # term: garbage collection
        print("Run change image")
        # new_image = Image.open("Images/blood_pic.jpeg")
        # tk_image = ImageTk.PhotoImage(new_image)
        # image_label.configure(image=tk_image)
        # image_label.image = tk_image

        filename = filedialog.askopenfilename(initialdir="Images")
        if filename == "":  # cancel
            return
        new_image = Image.open(filename)
        # keep the x y ratio
        current_size = new_image.size  # test 在其他地方写？
        max_size = 150  # test
        alpha = max_size/max(current_size)  # test
        new_image = new_image.resize((round(alpha*current_size[0]),  # test
                                      round(alpha*current_size[1])))  # test
        tk_image = ImageTk.PhotoImage(new_image)
        image_label.configure(image=tk_image)
        print(type(tk_image))
        image_label.image = tk_image  # solve garbage collection

    root = tk.Tk()  # make a root(can be anything) window
    root.title("Donor Database GUI")
    # root.geometry("800x600")

    # put this lable inside the root window
    top_label = ttk.Label(root, text="Blood Donor Database", foreground="red")  # 改字体颜色
    top_label.configure(foreground="red")  # 这样改颜色也行
    # ttk.Label(root, text="Blood Donor Database").pack()
    # where to put #占用两列（默认centered） #顶格sticky=“W” （west side：靠左）or ”E“ast or "N"orth (top) or "S"outh or SE
    top_label.grid(column=0, row=0, columnspan=2, sticky=tk.W)    # top_label.pack()  -different layout
    name_label = ttk.Label(root, text="Name:")
    name_label.grid(column=0, row=1, sticky=tk.E)

    # store string variable
    name_value = tk.StringVar()
    # name_value.set("Enter your name here")  # 在输入框显示默认
    # entry 输入框
    name_entry = ttk.Entry(root, textvariable=name_value)
    name_entry.grid(column=1, row=1, padx=5)  # "padding x"的缩写，其中"padding"指填充，"x"表示水平方向

    id_label = ttk.Label(root, text="Id:")
    id_label.grid(column=0, row=2, sticky=tk.E)
    id_value = tk.StringVar()
    # id_value = tk.intVar() 会在输入框默认显示0
    id_entry = ttk.Entry(root, textvariable=id_value)
    id_entry.grid(column=1, row=2, padx=5)  # Add 5 pixels of horizontal padding

    # when button was pressed, command will be run ---def ok_btn_cmd():
    ok_button = ttk.Button(root, text="Ok", command=ok_btn_cmd)
    ok_button.grid(column=1, row=6)
    cancel_button = ttk.Button(root, text="Cancel", command=cancel_btn_cmd)
    cancel_button.grid(column=2, row=6)

    blood_letter_value = tk.StringVar()
    # text="A"---display in GUI; value="A"---what put in variable if select button
    A_check = ttk.Radiobutton(root, text="A", variable=blood_letter_value,
                              value="A")
    A_check.grid(column=0, row=3, sticky=tk.W)

    B_check = ttk.Radiobutton(root, text="B", variable=blood_letter_value,
                              value="B")
    B_check.grid(column=0, row=4, sticky=tk.W)

    AB_check = ttk.Radiobutton(root, text="AB", variable=blood_letter_value,
                              value="AB")
    AB_check.grid(column=0, row=5, sticky=tk.W)

    O_check = ttk.Radiobutton(root, text="O", variable=blood_letter_value,
                              value="O")
    O_check.grid(column=0, row=6, sticky=tk.W)

    #checkbox
    rh_factor_value = tk.StringVar()
    # rh_factor_value.set("+")
    check_box_widget = ttk.Checkbutton(root, text="Rh Positive",
                                       variable=rh_factor_value,
                                       onvalue='+', offvalue='-')
    check_box_widget.grid(column=1, row=4)

    donation_label = ttk.Label(root, text="Closest Donation Center")
    donation_label.grid(column=2, row=0)
    donation_value = tk.StringVar()
    donation_combobox = ttk.Combobox(root, textvariable=donation_value)  # 下拉列表框
    donation_combobox.grid(column=2, row=1)
    donation_combobox["values"] = ("Durham", "Apex", "Raleigh")
    donation_combobox.state(["readonly"])  # 防止能输入别的（只读）

    donation_combobox.configure(postcommand=shuffle_choices)

    status_label = ttk.Label(root, text="")  # start with nothing
    status_label.grid(row=7, column=0, columnspan=10)

    # add image
    pil_image = Image.open("Images/blank_pic.jpeg")
    pil_image = pil_image.resize((150, 100))
    tk_image = ImageTk.PhotoImage(pil_image)
    # put it into label
    image_label = ttk.Label(root, image=tk_image)
    image_label.grid(column=1, row=7)
    image_label.image = tk_image  # solve garbage collection

    image_change_button = ttk.Button(root, text="Change Image",
                                     command=change_image_cmd)
    image_change_button.grid(column=2, row=7)

    root.after(3000, change_label_color)  # 注意这里的function不要（）

    # print("Before main loop")
    root.mainloop()  # tell tk to display the window # make sure it is the last line
    # print("After main loop")


if __name__ == '__main__':
    set_up_window()
    print("End")
