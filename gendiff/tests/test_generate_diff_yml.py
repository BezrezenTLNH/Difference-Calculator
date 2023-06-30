from gendiff.generate_diff import generate_diff


def test_generate_diff():
    file_path1 = 'gendiff/tests/fixtures/file1.yml'
    file_path2 = 'gendiff/tests/fixtures/file2.yml'

    expected_resullt_yml = \
        open('gendiff/tests/fixtures/test_result_yml.txt').read()
    assert generate_diff(file_path1, file_path2) == expected_resullt_yml
