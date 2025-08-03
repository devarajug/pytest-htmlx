import pytest

# 3 passing tests
def test_pass_one():
    assert 1 == 1

def test_pass_two():
    assert "pytest" == "pytest"

def test_pass_three():
    assert [1, 2, 3] == [1, 2, 3]

# 4 failing tests
def test_fail_one():
    assert 1 == 0

def test_fail_two():
    assert "a" == "b"

def test_fail_three():
    assert [1, 2] == [2, 1]

def test_fail_four():
    assert False

# 3 skipped tests

def test_skip_one():
    pytest.skip("demonstration skip 1")
    assert True


def test_skip_two():
    pytest.skip("demonstration skip 2")
    assert True

@pytest.mark.skip(reason="demonstration skip 3")
def test_skip_three():
    assert True