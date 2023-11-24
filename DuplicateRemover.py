import sys

def remove_duplicates(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        lines = list(set(lines))

        with open(file_path, 'w') as file:
            file.writelines(lines)

        print("Duplicate entries removed successfully.")

    except FileNotFoundError:
        print("File not found.")

if len(sys.argv) < 2:
    print("Please provide the path to the text file as a command-line argument.")

else:
    file_path = sys.argv[1]
    remove_duplicates(file_path)