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

methods = [
    (pc.BlowfishFile,),
    (pc.AESFile,),
    (pc.DES3File,)
]
