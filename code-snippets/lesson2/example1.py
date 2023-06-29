import os

# Check if a file exists
file_exists = os.path.exists("data.txt")
if file_exists:
    print("File exists!")
else:
    print("File does not exist!")

# Get the current working directory
current_dir = os.getcwd()
print("Current directory:", current_dir)

# Create a new directory
new_dir = os.path.join(current_dir, "new_directory")
os.mkdir(new_dir)
print("New directory created:", new_dir)
