import pytest
import unittest


import Inputs



# Test valid Inputs #
class InputTest(unittest.TestCase):
    def test_input(self):
        filename = "input.txt"
        f = open(filename, "r")
        inParams = Inputs.getfile(f)
        f.close()
        assert inParams[0] == (3.0), "Something wrong in the Inputs.py"
        assert inParams[1] == (3.0), "Something wrong in the Inputs.py"
        assert inParams[5] == (1), "Something wrong in the Inputs.py"
        assert inParams[6] == (3), "Something wrong in the Inputs.py"
    
    def test_invalid_Joint_count(self):
        filename = "TestCases/Invalid_Joints.txt"
        f = open(filename, "r")
        inParams = Inputs.getfile(f)
        flag=Inputs.verify(inParams[0],inParams[1],inParams[2],inParams[3],inParams[4],inParams[5],inParams[6])
        f.close()
        assert flag is False, "Something wrong in the verify module Inputs.py"

    def test_invalid_Member_count(self):
        filename = "TestCases/Invalid_Members.txt"
        f = open(filename, "r")
        inParams = Inputs.getfile(f)
        flag=Inputs.verify(inParams[0],inParams[1],inParams[2],inParams[3],inParams[4],inParams[5],inParams[6])
        f.close()
        assert flag is False, "Something wrong in the verify module Inputs.py"


    def test_invalid_forces(self):
        filename = "TestCases/Invalid_forces.txt"
        f = open(filename, "r")
        inParams = Inputs.getfile(f)
        flag=Inputs.verify(inParams[0],inParams[1],inParams[2],inParams[3],inParams[4],inParams[5],inParams[6])
        f.close()
        assert flag is False, "Something wrong in the verify module Inputs.py"
            
    def test_invalid_distance(self):
        filename = "TestCases/Invalid_location.txt"
        f = open(filename, "r")
        inParams = Inputs.getfile(f)
        flag=Inputs.verify(inParams[0],inParams[1],inParams[2],inParams[3],inParams[4],inParams[5],inParams[6])
        f.close()
        assert flag is False, "Something wrong in the verify module Inputs.py"

    def test_There_is_no_support(self):
        filename = "TestCases/Invalid_supports.txt"
        f = open(filename, "r")
        inParams = Inputs.getfile(f)
        flag=Inputs.verify(inParams[0],inParams[1],inParams[2],inParams[3],inParams[4],inParams[5],inParams[6])
        f.close()
        assert flag is False, "Something wrong in the verify module Inputs.py"

    def test_invalid_support_index(self):
        filename = "TestCases/Invalid_support_index.txt"
        f = open(filename, "r")
        inParams = Inputs.getfile(f)
        flag=Inputs.verify(inParams[0],inParams[1],inParams[2],inParams[3],inParams[4],inParams[5],inParams[6])
        f.close()
        assert flag is False, "Something wrong in the verify module Inputs.py"

    def test_invalid_member_connection(self):
        filename = "TestCases/Invalid_member_connection.txt"
        f = open(filename, "r")
        inParams = Inputs.getfile(f)
        flag=Inputs.verify(inParams[0],inParams[1],inParams[2],inParams[3],inParams[4],inParams[5],inParams[6])
        f.close()
        assert flag is False, "Something wrong in the verify module Inputs.py"
                              





