# ChangeCase.py - This program converts a string to lowercase and uppercase.
# Input:  Interactive
# Output:  Uppercase and lowercase versions of the user-entered string.

def main():
    sample = input("Enter a string or 'done' when you want to quit: ")

    while sample.lower() != "done":
        # Call lower() function here and print the result.
        lower_result = sample.lower()
        print("Lowercase: " + lower_result)

        # Call upper() function here and print the result.
        upper_result = sample.upper()
        print("Uppercase: " + upper_result)

        # Prompt user again
        sample = input("Enter a string or 'done' when you want to quit: ")

# End of main() function.

if __name__ == '__main__':
    # Call the main function to run program
    main()