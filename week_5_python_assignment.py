def create_file():
    try:
        # Create a new text file named "my_file.txt" in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Write at least three lines of text to the file
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line with some text\n")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("File created successfully.")

def read_file():
    try:
        # Read the contents of "my_file.txt"
        with open("my_file.txt", "r") as file:
            # Display the contents on the console
            print("Contents of my_file.txt:")
            print(file.read())
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def append_file():
    try:
        # Open "my_file.txt" in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text to the existing content
            file.write("Line 4 - Appended\n")
            file.write("67890\n")
            file.write("Another appended line\n")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("Content appended successfully.")

def main():
    create_file()
    read_file()
    append_file()

if __name__ == "__main__":
    main()
