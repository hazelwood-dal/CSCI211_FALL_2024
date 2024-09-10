
def main():
    # Get the value of 'n' from the user
    n = int(input("Enter the size of the multiplication table: "))

    # Outer loop for rows
    for i in range(1, n + 1):
        # Inner loop for columns
        for j in range(1, n + 1):
            # Print the product of i and j, formatted with a width of 3 for neatness
            print(f"{i * j:3}", end=" ")
        # Move to the next line after each row is printed
        print()

if __name__ == "__main__":
    main()