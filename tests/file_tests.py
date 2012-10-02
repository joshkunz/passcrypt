import pytest
from utils import encryption_methods, file_cleanup, test_file

@pytest.mark.parametrize(("constructor",), encryption_methods)
def test_constructors(constructor):
    "Test the various file's constructors"
    with file_cleanup(test_file):
        constructor()

@pytest.mark.parametrize(("con",), encryption_methods)
def test_write(con):
    with file_cleanup(test_file):
        file = con()
        file.write("some test data")
        file.close()

@pytest.mark.parametrize(("con",), encryption_methods)
def test_read(con):
    test_data = "Some more test data"
    with file_cleanup(test_file):
        file = con()
        file.write(test_data)
        file.close()
        file = con()
        assert test_data == file.read()
        file.close()

@pytest.mark.parametrize(("con",), encryption_methods)
def test_tell(con):
    test_data = "some even more different test data"
    with file_cleanup(test_file):
        file = con()
        assert file.tell() == 0
        file.write(test_data)
        assert file.tell() == len(test_data)
