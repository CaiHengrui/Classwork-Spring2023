# 3As
# 1. Arrange
# 2. Act
# 3. Assert

def test_HDL_analysis( ):
    from blood_calculator import HDL_analysis
    # 1. Arrange
    HDL_input = 65
    # 2. Act
    answer = HDL_analysis(HDL_input)
    # 3. Assert
    assert answer == "Normal"
    
    HDL_input = 45
    answer = HDL_analysis(HDL_input)
    assert answer == "Borderline low"
    # not recommended
    
    
    
def test_HDL_analysis_Borderline_Low():
    from blood_calculator import HDL_analysis
    # 1. Arrange
    HDL_input = 45
    # 2. Act
    answer = HDL_analysis(HDL_input)
    # 3. Assert
    assert answer == "Borderline low"
    
def test_HDL_analysis_Low():
    from blood_calculator import HDL_analysis
    # 1. Arrange
    HDL_input = 5
    # 2. Act
    answer = HDL_analysis(HDL_input)
    # 3. Assert
    assert answer == "low"