from gendiff.scripts.gendiff import generate_diff

def test_generate_diff():
    file1 = 'file1.json'
    file2 = 'file2.json'
    test_file = generate_diff(file1, file2)
    assert isinstance(str, generate_diff(file1, file2))
    assert test_file.startswith('{')
    assert test_file.endswith('}')
