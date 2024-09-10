import check50
import re


@check50.check()
def exists():
    """multiplication.py exists"""
    check50.exists("multiplication.py")


@check50.check(exists)
def test_5x5():
    """Correctly prints a 5x5 multiplication table"""
    check_multiplication_table(5)


@check50.check(exists)
def test_3x3():
    """Correctly prints a 3x3 multiplication table"""
    check_multiplication_table(3)


@check50.check(exists)
def test_1x1():
    """Correctly prints a 1x1 multiplication table"""
    check_multiplication_table(1)


def check_multiplication_table(n):
    # Prepare the expected output for a given n
    expected_output = generate_expected_output(n)

    # Normalize both expected and actual output
    def normalize_output(output):
        # Strip leading/trailing spaces from each line and normalize spaces between numbers
        lines = output.strip().splitlines()
        normalized_lines = [re.sub(r'[ \t]+', ' ', line.strip()) for line in
                            lines]  # Normalize internal spaces and strip each line
        return "\n".join(normalized_lines) + "\n"  # Ensure newline at the end of the output

    # Run the student's code, normalize its output, and compare it with the normalized expected output
    actual_output = check50.run("python3 multiplication.py").stdin(str(n)).stdout()
    actual_output_normalized = normalize_output(actual_output)
    expected_output_normalized = normalize_output(expected_output)

    if actual_output_normalized != expected_output_normalized:
        raise check50.Failure(
            f"Output did not match expected output.\nExpected:\n{expected_output_normalized}\nGot:\n{actual_output_normalized}")


def generate_expected_output(n):
    output = ""
    for i in range(1, n + 1):
        row = " ".join(f"{i * j:3}" for j in range(1, n + 1))
        output += row.strip() + "\n"
    return output
