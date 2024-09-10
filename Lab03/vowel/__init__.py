import check50
import check50.c
import check50.py

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


@check50.check(exists)
def function_exists():
    """count_letter function is defined in vowel.py"""
    # Import the module and check if the count_letter function is defined
    module = check50.py.import_("vowel.py")

    if not hasattr(module, "count_letter"):
        raise check50.Failure("count_letter function not defined in vowel.py")


@check50.check(function_exists)
def test_vowel_not_present():
    """count_letter returns 0 if the vowel is not present in the word"""
    module = check50.py.import_("vowel.py")

    result = module.count_letter("banana", "e")

    if result != 0:
        raise check50.Failure(f"Expected 0 but got {result} for count_letter('banana', 'e')")


@check50.check(function_exists)
def test_multiple_vowels():
    """count_letter returns correct count for multiple vowels in a word"""
    module = check50.py.import_("vowel.py")

    result = module.count_letter("banana", "a")

    if result != 3:
        raise check50.Failure(f"Expected 3 but got {result} for count_letter('banana', 'a')")
