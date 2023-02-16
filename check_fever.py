def test_check_fever():
    from blood_calculator import check_fever
    ut_temps = [97, 98.6, 100.1,103, 98.4]
    wer = check_fever(input_temps)
    ected = True
    ert answer == expected



def check_fever(input_list):
    for temperature in input_list:
        if temperature > 100.5:
            return True
    return False