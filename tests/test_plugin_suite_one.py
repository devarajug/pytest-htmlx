import pytest
import time

# 3 passing tests
def test_pass_one():
    time.sleep(0.1)
    assert 1 == 1

def test_pass_two():
    time.sleep(0.2)
    assert "pytest" == "pytest"

def test_pass_three():
    time.sleep(0.3)
    assert [1, 2, 3] == [1, 2, 3]

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

def test_fail_four():
    time.sleep(0.1)
    assert False

# 3 skipped tests

def test_skip_one():
    time.sleep(0.8)
    pytest.skip("demonstration skip 1")
    assert True


def test_skip_two():
    time.sleep(0.3)
    pytest.skip("demonstration skip 2")
    assert True

def test_skip_three():
    time.sleep(0.4)
    pytest.skip("demonstration skip 3")
    assert True