#utilizes file handling and exception handling to read and write a configuration file

def read_configuration_file(file_path):
    try:
        with open(file_path, "r") as file:
            config_data = file.read()
            print("Configuration file content:")
            print(config_data)
    except FileNotFoundError:
        print(f"Configuration file '{file_path}' not found.")
    except IOError:
        print("Error reading configuration file.")

def write_configuration_file(file_path, config_data):
    try:
        with open(file_path, "w") as file:
            file.write(config_data)
            print("Configuration file updated successfully.")
    except IOError:
        print("Error writing to configuration file.")

# Example usage
config_file_path = "config.ini"
config_content = """
[Server]
Host = example.com
Port = 8080
"""

write_configuration_file(config_file_path, config_content)
read_configuration_file(config_file_path)
