from homework import *

import pytest
import os


li = [1, 2, 3, 4, 5, 6, 7, 8, 9]

@pytest.mark.parametrize("list,indeces,result",
                        [([],[],[]),
                        ([1,2,3],[0,1,2],[1,2,3]),
                        ([1,2,'text'],[0,2],[1,'text'])]
                         )
def test_if_correct(list, indeces, result):
    assert take_from_list(list,indeces) == result

@pytest.mark.parametrize("types", ['random text', 4.2, [4.2, 5, 2.1], {}])
def test_type_values(types):
    with pytest.raises(ValueError):
        take_from_list(li, types)

@pytest.mark.parametrize("indeces", list(range(20,30)))
def test_length(indeces):
    with pytest.raises(IndexError):
        take_from_list(li, indeces)

def test_calculate():
    test_input = "{\"list\": [1,2,3,4,5,6,7,8,9], \"indices\": [0,2,4,6,8]}"
    with open('test_input.json', 'w') as f:
        f.write(test_input)
    calculate("test_input.json", "test_output.json")

    with open("test_output.json", 'r') as f_p:
        data = json.load(f_p)

    assert data == [1, 3, 5, 7, 9]

    os.remove("test_input.json")
    os.remove("test_output.json")







