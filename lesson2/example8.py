def count_log_levels(log_file):
    log_levels = {}
    try:
        with open(log_file, "r") as file:
            for line in file:
                if line.strip():
                    log_level = line.split()[0]
                    log_levels[log_level] = log_levels.get(log_level, 0) + 1
    except FileNotFoundError:
        print(f"Log file '{log_file}' not found.")
    except IOError:
        print("Error reading log file.")

    return log_levels


# Test the count_log_levels function
log_file = "app.log"
log_level_counts = count_log_levels(log_file)
print("Log level counts:")
for log_level, count in log_level_counts.items():
    print(f"{log_level}: {count}")
