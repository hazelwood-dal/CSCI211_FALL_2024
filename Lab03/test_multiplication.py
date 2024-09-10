import check50
import check50.c

@check50.check()
def exists():
    """multiplication.py exists"""
    check50.exists("multiplication.py")

@check50.check()
def test_5x5():
    """Correctly prints a 5x5 multiplication table"""
    check50.run("python3 multiplication.py").stdin("5").stdout("  1  2  3  4  5\n  2  4  6  8 10\n  3  6  9 12 15\n  4  8 12 16 20\n  5 10 15 20 25\n", regex=False).exit(0)

@check50.check()
def test_3x3():
    """Correctly prints a 3x3 multiplication table"""
    check50.run("python3 multiplication.py").stdin("3").stdout("  1  2  3\n  2  4  6\n  3  6  9\n", regex=False).exit(0)

@check50.check()
def test_1x1():
    """Correctly prints a 1x1 multiplication table"""
    check50.run("python3 multiplication.py").stdin("1").stdout("  1\n", regex=False).exit(0)
