import pytest

# calling a fixture creates an argument in the scope of the test with that name.
@pytest.mark.model1 #custom marks should get registered in pytest.ini (=configuration file) / req. using custom pytest_configure hook.
def test_firstItem(list_true_false):  #"test_*": methode of a class / a function (meaning it's defined outside of any class) 
    assert list_true_false[0]==True, "content not True"

@pytest.mark.xfail
@pytest.mark.model2
def test_secondItem(list_true_false):
    assert list_true_false[1]==True, "content not True"