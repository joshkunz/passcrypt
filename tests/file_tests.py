import pytest
from utils import methods, file_cleanup, test_file, test_pass

@pytest.mark.parametrize(("method",), methods)
def test_constructors(method):
    "Test the various file's constructors"
    with file_cleanup(test_file):
        file = method(open(test_file, 'w'), test_pass)
        file.close()

@pytest.mark.parametrize(("method",), methods)
def test_write(method):
    with file_cleanup(test_file):
        file = method(open(test_file, 'w'), test_pass)
        file.write("some test data")
        file.close()

@pytest.mark.parametrize(("method",), methods)
def test_read(method):
    test_data = "Some more test data"
    with file_cleanup(test_file):
        file = method(open(test_file, 'w'), test_pass)
        file.write(test_data)
        file.close()

        file = method(test_file, test_pass) 
        assert test_data == file.read()
        file.close()

@pytest.mark.parametrize(("method",), methods)
def test_tell(method):
    test_data = "some even more different test data"
    with file_cleanup(test_file):
        file = method(open(test_file, 'w'), test_pass)
        assert file.tell() == 0
        file.write(test_data)
        assert file.tell() == len(test_data)
        file.close()

@pytest.mark.parametrize(("method",), methods)
def test_seek(method):
    test_data = "1234567890"
    with file_cleanup(test_file):
        file = method(open(test_file, 'w'), test_pass)
        file.write(test_data)
        file.close()

        file = method(test_file, test_pass)
        file.seek(-2, 2)
        assert file.read() == test_data[-2:]
        file.close()
