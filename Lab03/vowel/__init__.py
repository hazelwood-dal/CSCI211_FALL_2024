import check50
import check50.c

@check50.check()
def exists():
    """vowel.py exists"""
    check50.exists("vowel.py")

@check50.check()
def test_hello():
    """Correctly counts vowels in 'Hello World'"""
    check50.run("python3 vowel.py").stdin("Hello World").stdout("The number of 'a's is: 0\nThe number of 'e's is: 1\nThe number of 'i's is: 0\nThe number of 'o's is: 2\nThe number of 'u's is: 0\nThe total number of vowels is: 3\n", regex=False).exit(0)

@check50.check()
def test_no_vowels():
    """Correctly handles a string with no vowels"""
    check50.run("python3 vowel.py").stdin("bcdfgh").stdout("The number of 'a's is: 0\nThe number of 'e's is: 0\nThe number of 'i's is: 0\nThe number of 'o's is: 0\nThe number of 'u's is: 0\nThe total number of vowels is: 0\n", regex=False).exit(0)

@check50.check()
def test_mixed_case():
    """Correctly handles a string with uppercase vowels"""
    check50.run("python3 vowel.py").stdin("AEIOUaeiou").stdout("The number of 'a's is: 2\nThe number of 'e's is: 2\nThe number of 'i's is: 2\nThe number of 'o's is: 2\nThe number of 'u's is: 2\nThe total number of vowels is: 10\n", regex=False).exit(0)
