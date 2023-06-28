import os

# Check if a file exists
file_path = "data.txt"
if os.path.exists(file_path):
    print(f"The file '{file_path}' exists!")
else:
    print(f"The file '{file_path}' does not exist.")


import os

# Rename a file
old_name = "old_file.txt"
new_name = "new_file.txt"
os.rename(old_name, new_name)
print(f"The file '{old_name}' has been renamed to '{new_name}'.")



import os

# Delete a file
file_path = "file_to_delete.txt"
os.remove(file_path)
print(f"The file '{file_path}' has been deleted.")
