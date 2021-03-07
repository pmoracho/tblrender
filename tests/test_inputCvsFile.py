import os, tempfile, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tblrender.InputCvsFile import InputCvsFile

SIMPLE_CVS = """Col1, Col2, Col3
 1, 2, 3
 4, 5, 6"""

def test_inputCvsFile():

    config = {"file": mock_cvsfile(SIMPLE_CVS)}
    proc = InputCvsFile(config)
    proc.process()

    assert [['Col1', ' Col2', ' Col3'], [' 1', ' 2', ' 3'], [' 4', ' 5', ' 6']] == proc.data[0]

def mock_cvsfile(content):

    tmp = tempfile.NamedTemporaryFile(delete=False)
    try:
        tmp.write(content.encode("utf-8"))
    finally:
        tmp.close()

    return tmp.name