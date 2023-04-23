import tkinter as tk
from tkinter import ttk
# from tkinter import *  (common but not recommended)


def set_up_window():
    def ok_btn_cmd():
        print("Ok clicked")
        patient_name = name_value.get()
        id_number = id_value.get()
        blood_letter = blood_letter_value.get()
        rh = rh_factor_value.get()
        print("Patient name is {}".format(patient_name))
        print("Patient id is {}".format(id_number))
        print("Patient blood type is {}{}".format(blood_letter, rh))

    def cancel_btn_cmd():
        root.destroy()  #

    root = tk.Tk()  # make a root(can be anything) window
    root.title("Donor Database GUI")
    root.geometry("800x600")

    # put this lable inside the root window
    top_label = ttk.Label(root, text="Blood Donor Database")
    # where to put
    top_label.grid(column=0, row=0)

    name_label = ttk.Label(root, text="Name:")
    name_label.grid(column=0, row=1)

    # store string variable
    name_value = tk.StringVar()
    # name_value.set("Enter your name here")  # 在输入框显示默认
    # entry 输入框
    name_entry = ttk.Entry(root, textvariable=name_value)
    name_entry.grid(column=1, row=1)

    id_label = ttk.Label(root, text="Id:")
    id_label.grid(column=0, row=2)
    id_value = tk.StringVar()
    # id_value = tk.intVar() 会在输入框默认显示0
    id_entry = ttk.Entry(root, textvariable=id_value)
    id_entry.grid(column=1, row=2)

    # when button was pressed, command will be run ---def ok_btn_cmd():
    ok_button = ttk.Button(root, text="Ok", command=ok_btn_cmd)
    ok_button.grid(column=1, row=6)
    cancel_button = ttk.Button(root, text="Cancel", command=cancel_btn_cmd)
    cancel_button.grid(column=2, row=6)

    blood_letter_value = tk.StringVar()
    # text="A"---display in GUI; value="A"---what put in variable if select button
    A_check = ttk.Radiobutton(root, text="A", variable=blood_letter_value,
                              value="A")
    A_check.grid(column=0, row=3)

    B_check = ttk.Radiobutton(root, text="B", variable=blood_letter_value,
                              value="B")
    B_check.grid(column=0, row=4)

    AB_check = ttk.Radiobutton(root, text="AB", variable=blood_letter_value,
                              value="AB")
    AB_check.grid(column=0, row=5)

    O_check = ttk.Radiobutton(root, text="O", variable=blood_letter_value,
                              value="O")
    O_check.grid(column=0, row=6)

    #checkbox
    rh_factor_value = tk.StringVar()
    # rh_factor_value.set("+")
    check_box_widget = ttk.Checkbutton(root, text="Rh Positive",
                                       variable=rh_factor_value,
                                       onvalue='+', offvalue='-')
    check_box_widget.grid(column=1, row=4)

    # print("Before main loop")
    root.mainloop()  # tell tk to display the window # make sure it is the last line
    # print("After main loop")


if __name__ == '__main__':
    set_up_window()
    print("End")
