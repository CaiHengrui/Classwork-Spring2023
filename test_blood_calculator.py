# 3As
# 1. Arrange
# 2. Act
# 3. Assert


#decorator---one function but check multiple times
import pytest

@pytest.mark.parametrize("HDL_input,expected",
[(65,"Normal"),
 (45,"Borderline low"),
 (20,"low")
 ])

def test_HDL_analysis(HDL_input,expected):
    from blood_calculator import HDL_analysis
    # 1. Arrange
    # 2. Act
    answer = HDL_analysis(HDL_input)
    # 3. Assert
    assert answer == expected


@pytest.mark.parametrize("LDL_input,expected",
[(200,"very high"),
 (170,"high"),
 (145,"Boarderline high"),
 (14,"normal")
 ])

def test_LDL_analysis(LDL_input,expected):
    from blood_calculator import LDL_analysis
    # 1. Arrange
    # 2. Act
    answer = LDL_analysis(LDL_input)
    # 3. Assert
    assert answer == expected









# def test_HDL_analysis():
    # from blood_calculator import HDL_analysis
    # # 1. Arrange
    # HDL_input = 65
    # expected = "Normal"
    # # 2. Act
    # answer = HDL_analysis(HDL_input)
    # # 3. Assert
    # assert answer == "Normal"
    
    # HDL_input = 45
    # answer = HDL_analysis(HDL_input)
    # assert answer == "Borderline low"
    # # not recommended
    
    
    
# def test_HDL_analysis_Borderline_Low():
    # from blood_calculator import HDL_analysis
    # # 1. Arrange
    # HDL_input = 45
    # # 2. Act
    # answer = HDL_analysis(HDL_input)
    # # 3. Assert
    # assert answer == "Borderline low"
    
# def test_HDL_analysis_Low():
    # from blood_calculator import HDL_analysis
    # # 1. Arrange
    # HDL_input = 5
    # # 2. Act
    # answer = HDL_analysis(HDL_input)
    # # 3. Assert
    # assert answer == "low"