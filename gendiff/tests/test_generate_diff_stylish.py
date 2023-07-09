from gendiff.generate_diff import generate_diff


def test_generate_diff():
    file_path1 = 'gendiff/tests/fixtures/file1_stylish.yml'
    file_path2 = 'gendiff/tests/fixtures/file2_stylish.yml'

    expected_result_stylish = \
        open('gendiff/tests/fixtures/test_result_stylish.txt').read()
    assert generate_diff(file_path1, file_path2) == expected_result_stylish
