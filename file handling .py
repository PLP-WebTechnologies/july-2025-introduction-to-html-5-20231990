# Read from input.txt and write modified content to output.txt
try:
    with open("input.txt", "r") as infile:
        content = infile.read()

    # Example modification: convert text to uppercase
    modified_content = content.upper()

    with open("output.txt", "w") as outfile:
        outfile.write(modified_content)

    print("✅ File has been read and modified successfully!")

except FileNotFoundError:
    print("❌ The file 'input.txt' does not exist.")
except Exception as e:
    print(f"⚠️ An error occurred: {e}")




# Error Handling Lab

filename = input("Enter the filename you want to open: ")

try:
    with open(filename, "r") as f:
        print("✅ File content:")
        print(f.read())
except FileNotFoundError:
    print(f"❌ The file '{filename}' was not found.")
except PermissionError:
    print(f"⚠️ You don't have permission to read '{filename}'.")
except Exception as e:
    print(f"⚠️ Unexpected error: {e}")
