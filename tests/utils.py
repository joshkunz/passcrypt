import passcrypt as pc
import contextlib as cl
import os
from functools import partial

@cl.contextmanager
def file_cleanup(filename):
    yield None
    os.remove(filename)

test_pass = "some pass"
test_file = "somefile.test"

# get partially applied constructors
blowfish_file = partial(pc.BlowfishFile, test_file, test_pass)
aes_file = partial(pc.AESFile, test_file, test_pass)
des3_file = partial(pc.DES3File, test_file, test_pass)

encryption_methods = [(blowfish_file,), (aes_file,), (des3_file,)]
