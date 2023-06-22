from gendiff.generate_diff import generate_diff
import pytest


@pytest.fixture
def test_generate_diff():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    test_file = generate_diff(file1, file2)
    assert isinstance(str, test_file)
    assert test_file.startswith('{')
    assert test_file.endswith('}')
