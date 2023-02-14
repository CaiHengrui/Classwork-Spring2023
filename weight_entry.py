def input_weight_entry():
    print("Enter patient weight in form of ## units (e.g., 105 lb)")
    weight_input = input("Enter weight: ")
    weight_in_kg = parse_weight_input(weight_input)
    print("The patient weight of {} kg will be stored "
          "in database.".format(weight_in_kg))


def parse_weight_input(weight_input):
    if weight_input == "": # empty string but "  " fail！！#很多个空格
        return None
    if weight_input.find(" ") < 0: #22lb but 22  lb fail！！#很多个空格
        return None
    weight, units = weight_input.split(' ')
    weight = float(weight) #22.0
    units = units.lower() # remove capitalize situation:LB Lb
    if units[-1] == "s":
        units = units[0:-1] #lbs remove s
    if units in ["lb", "pound"]:
        weight_kg = convert_lb_to_kg(weight)
    elif units == "kg":
        weight_kg = weight
    else:
        return None
    weight_kg = round(weight_kg)
    return weight_kg


def convert_lb_to_kg(weight_lb):
    weight_kg = weight_lb / 2.20462
    return weight_kg


if __name__ == "__main__":
    input_weight_entry()