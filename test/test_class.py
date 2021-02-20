import os, sys
import pytest
import main

x,y = 1,2
result = 3

class TestClass:

    def test_one(self):
        assert 1 == 1

    def test_x(self): 
        assert x == 1

    def test_y(self): 
        assert y == 2

    def test_result(self):
        assert (x + y) == result
