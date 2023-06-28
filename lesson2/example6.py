try:
    file = open("data.txt", "r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File not found!")
except IOError:
    print("Error reading file!")
else:
    print("File read successfully!")
finally:
    file.close()
    print("File closed.")
