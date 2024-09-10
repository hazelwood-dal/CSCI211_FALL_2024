import check50
import re

@check50.check()
def exists():
    """multiplication.py exists"""
    check50.exists("multiplication.py")

@check50.check(exists)
def test_5x5():
    """Correctly prints a 5x5 multiplication table"""
    expected_output = "1 2 3 4 5 \n2 4 6 8 10 \n3 6 9 12 15 \n4 8 12 16 20 \n5 10 15 20 25 \n"
    # Normalize spaces between numbers and keep newlines intact
    normalized_expected = re.sub(r'[ \t]+', ' ', expected_output.strip())
    # Replace multiple spaces with a single space, but keep newlines as they are
    #normalized_expected = re.sub(r'\s{2,}', ' ', normalized_expected)
    check50.run("python3 multiplication.py").stdin("5").stdout(normalized_expected, regex=True).exit(0)

@check50.check(exists)
def test_3x3():
    """Correctly prints a 3x3 multiplication table"""
    expected_output = "1 2 3 \n2 4 6 \n3 6 9 \n"
    # Normalize spaces between numbers and keep newlines intact
    normalized_expected = re.sub(r'[ \t]+', ' ', expected_output.strip())
    # Replace multiple spaces with a single space, but keep newlines as they are
    #normalized_expected = re.sub(r'\s{2,}', ' ', normalized_expected)
    check50.run("python3 multiplication.py").stdin("3").stdout(normalized_expected, regex=True).exit(0)

@check50.check(exists)
def test_1x1():
    """Correctly prints a 1x1 multiplication table"""
    expected_output = "1 \n"
    # Normalize spaces between numbers and keep newlines intact
    normalized_expected = re.sub(r'[ \t]+', ' ', expected_output.strip())
    # Replace multiple spaces with a single space, but keep newlines as they are
    #normalized_expected = re.sub(r'\s{2,}', ' ', normalized_expected)
    check50.run("python3 multiplication.py").stdin("1").stdout(normalized_expected, regex=True).exit(0)
