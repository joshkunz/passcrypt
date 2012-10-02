import passcrypt as pc
import pytest
from utils import test_file, file_cleanup, encryption_methods

@pytest.mark.parametrize(("constructor",), encryption_methods)
def test_shelf_create(constructor):
    with file_cleanup(test_file):
        shelf = pc.FileShelf(constructor())
        shelf.close()

@pytest.mark.parametrize(("constructor",), encryption_methods)
def test_shelf_set(constructor):
    with file_cleanup(test_file):
        shelf = pc.FileShelf(constructor())
        shelf["key"] = "value"
        assert shelf["key"] == "value"
        shelf.close()

@pytest.mark.parametrize(("constructor",), encryption_methods)
def test_shelf_save(constructor):
    with file_cleanup(test_file):
        shelf = pc.FileShelf(constructor())
        shelf["somekey"] = "somevalue"
        shelf.close()

        shelf = pc.FileShelf(constructor())
        assert ["somekey"] == "somevalue"
        shelf.close()
