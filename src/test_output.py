import pytest
import unittest
import React
import Inputs
import internal
import numpy as np

def abserr(actual, expected):
    return abs(actual - expected)

def meanerr(actual_vector, expected_vector,size):
    sum=0
    for i in range(0,size):
        sum+=abs(actual_vector[i]-expected_vector[i])
    return sum/size    

   
class OutputCorrectnessTest(unittest.TestCase):
    def test_output(self):
        filename = "input.txt"
        f = open(filename, "r")
        (n,m,J,M,F,p,r)=Inputs.getfile(f)
        (px,py,ry,I)=internal.internals(n,m,J,M,F,p,r)
        assert abserr(px, 0.0) < 0.1
        assert abserr(py, 25.0) < 0.1
        assert abserr(ry, 25.0) < 0.1
        assert abserr(I[0], -35.36) < 0.1
        assert abserr(I[1], 25.0) < 0.1
        assert abserr(I[2], -35.36) < 0.1
    
    def test_valid_n4m5(self):
        filename = "Testcases/valid_n4m5.txt"
        f = open(filename, "r")
        (n,m,J,M,F,p,r)=Inputs.getfile(f)
        (px,py,ry,I)=internal.internals(n,m,J,M,F,p,r)
        ans=np.zeros(m)
        ans=[0,0,-10,0,0]
        assert abserr(px, 0.0) < 0.01
        assert abserr(py, 0.0) < 0.01
        assert abserr(ry, -10.0) < 0.1
        assert meanerr(I,ans,m) < 0.1

    def test_valid_n5m7(self):
        filename = "Testcases/valid_n5m7.txt"
        f = open(filename, "r")
        (n,m,J,M,F,p,r)=Inputs.getfile(f)
        (px,py,ry,I)=internal.internals(n,m,J,M,F,p,r)
        ans=np.zeros(m)
        ans=[-53.03,37.5,-17.6,-25,17.6,12.5,-17.6]
        assert abserr(px, 0.0) < 0.1
        assert abserr(py, 37.5) < 0.1
        assert abserr(ry, 12.5) < 0.1
        assert meanerr(I,ans,m) < 0.1

    def test_valid_crane(self):
        filename = "Testcases/valid_crane.txt"
        f = open(filename, "r")
        (n,m,J,M,F,p,r)=Inputs.getfile(f)
        (px,py,ry,I)=internal.internals(n,m,J,M,F,p,r)
        ans=np.zeros(m)
        ans=[0,200,0,-300,0,200,0,-300,0,200,0,-300,-200,-200,282.8,-300,223.6]
        assert abserr(px, 0.0) < 0.1
        assert abserr(py, 300.0) < 0.1
        assert abserr(ry, -200.0) < 0.1
        assert meanerr(I,ans,m) < 0.1    
        

       
           