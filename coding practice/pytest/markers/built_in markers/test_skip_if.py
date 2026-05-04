import pytest
import sys

@pytest.mark.skipif(sys.version_info<(3,11) ,reason="needs higher version")
def test_new_syntax():
    assert True

