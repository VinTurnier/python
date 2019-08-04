import pytest

def sum(num1, num2):
	return num1+num2

def test_sum():
	assert sum(1,2)==3

def test_sum_output_type():
	assert type(sum(1,2)) is int

def test_sum_fails():
	assert sum(1,4) != 4


@pytest.mark.parametrize('num1,num2,expected',[(3,5,8),
			(5,6,11),(1,7,8),(20,30,50),(100,200,300)])
def test_multiple_sum(num1,num2,expected):
	assert sum(num1,num2) == expected

