import passcrypt as pc
import pytest
from utils import test_file, file_cleanup

passw = "my real password"
writers = [pc.BlowfishFile, pc.DES3File, pc.AESFile]
final = []
for writer in writers:
    final.append((writer, test_file, passw))

@pytest.mark.parametrize(("writer", "filename", "password"), 
                         final) 
def test_shelf_create(writer, filename, password):
    with file_cleanup(test_file):
        shelf = pc.EncryptedShelf(writer, filename, password)
        shelf.close()

@pytest.mark.parametrize(("writer", "filename", "password"),
                          final)
def test_shelf_get(writer, filename, password):
    with file_cleanup(test_file):
        shelf = pc.EncryptedShelf(writer, filename, password)
        shelf["key"] = "value"
        assert shelf["key"] == "value"
        assert shelf.get("key") == "value"
        assert shelf.get("notkey") is None
        assert shelf.get("notkey", "notvalue") == "notvalue"
        shelf.close()

@pytest.mark.parametrize(("writer", "filename", "password"),
                          final)
def test_shelf_in(writer, filename, password):
    with file_cleanup(test_file):
        shelf = pc.EncryptedShelf(writer, filename, password)
        shelf["key"] = "value"
        assert "key" in shelf
        assert "notkey" not in shelf
        shelf.close()

@pytest.mark.parametrize(("writer", "filename", "password"), 
                         final) 
def test_shelf_set(writer, filename, password):
    with file_cleanup(test_file):
        shelf = pc.EncryptedShelf(writer, filename, password)
        shelf["key"] = "value"
        assert shelf["key"] == "value"
        shelf.close()

@pytest.mark.parametrize(("writer", "filename", "password"), 
                         final) 
def test_shelf_save(writer, filename, password):
    with file_cleanup(test_file):
        shelf = pc.EncryptedShelf(writer, filename, password)
        shelf["somekey"] = "somevalue"
        shelf.close()

        shelf = None

        # load up the old shelf
        shelf = pc.EncryptedShelf(writer, filename, password)
        assert shelf["somekey"] == "somevalue"
        shelf.close()
