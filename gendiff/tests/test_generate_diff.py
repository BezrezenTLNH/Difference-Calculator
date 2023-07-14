from gendiff.generate_diff import generate_diff


def test_generate_diff():
    data_1 = 'gendiff/tests/fixtures/file1_stylish.json'
    data_2 = 'gendiff/tests/fixtures/file2_stylish.json'

    # expected_result_stylish = \
    #     open('gendiff/tests/fixtures/test_result_stylish.txt').read()
    expected_result_plain = \
        open('gendiff/tests/fixtures/test_result_plain.txt').read()
    expected_result_json = \
        open('gendiff/tests/fixtures/test_result_json.txt').read()

    # assert generate_diff(data_1, data_2, 'stylish') == expected_result_stylish
    # assert generate_diff(data_1, data_2) == expected_result_stylish
    assert generate_diff(data_1, data_2, 'plain') == expected_result_plain
    assert generate_diff(data_1, data_2, 'json') == expected_result_json
