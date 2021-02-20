import os, sys
import pytest
import main

x,y = 1,2
result = 3


class TestInit:

    def test_one(self):
        assert 1 == 1

    def test_addition(self):
        assert main.addition(x,y) == result

    def adding_words(self):
        x = "1"
        main.addition(x, y)

    def test_addition_exception(self):
        with pytest.raises(TypeError):
            self.adding_words(self)

