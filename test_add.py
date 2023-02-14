# def test_add():
    # from add import add
	# answer = add(0.1,0.2)
	# assert answer == 0.3
    
# test will fail because base10 and base2 will cause residue like 0.30000000004

#so how to write a test that will approximately get the value 
import pytest

def test_add():
    from add import add
	answer = add(0.1,0.2)
	assert answer == pytest.approx(0.3) #pass
    
    
'''
$ python
>>>import pytest
>>>pytest.approx(0.3)显示range
0.3 ± 3.0e-07
>>>pytest.approx(0.3,abs=0.1) #修改range
0.3 ± 1.0e-01
>>>quit()
'''

#how to merge into main with test in advance  
#Test before merging from a branch into the main story
   
   
