import pytest

# @pytest.mark.parametrize("coor1,coor2,new_x,expected",
# [((0,0),(1,1),2,2),
# ((0,0),(1,2),2,4),
# ((0,0),(1,0),3,0),
# ((0,0),(0,1),1,None),
# ((1,1),(1,1),2,None)

# ])



# def test_calculate_y_on_line(coor1,coor2,new_x,expected):
    # from calculate_y import calculate_y_on_line
    # answer = calculate_y_on_line(coor1,coor2,new_x)
    # assert answer == expected
    





@pytest.mark.parametrize("x1,x2,y1,y2,expected",
[(0,1,0,1,1 ),
(0,1,0,0,0),
(0,0,1,0,None),
(1,1,1,1,None)
])


def test_calculate_slope(x1,x2,y1,y2,expected     ):
    from calculate_y import calculate_slope
    answer = calculate_slope(x1,x2,y1,y2)
    assert answer == expected