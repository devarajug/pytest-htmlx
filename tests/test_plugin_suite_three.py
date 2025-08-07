import pytest
import time

# 3 passing tests
def test_pass_one():
    time.sleep(0.1)
    assert 1 == 1


# 4 failing tests
def test_fail_one():
    time.sleep(0.1)
    assert 1 == 0

def test_fail_two():
    time.sleep(0.2)
    assert 2 == "2"

def test_fail_three():
    time.sleep(0.5)
    assert None



# 3 skipped tests

def test_skip_one():
    time.sleep(0.8)
    pytest.skip("demonstration skip 1")
    assert True
