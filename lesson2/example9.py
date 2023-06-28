def analyze_server_log(log_file):
    try:
        with open(log_file, "r") as file:
            total_requests = 0
            success_count = 0
            url_counts = {}

            for line in file:
                total_requests += 1
                elements = line.split()

                # Check if the request was successful (status code 200)
                if elements[8] == "200":
                    success_count += 1

                # Extract the requested URL and update its count
                url = elements[6]
                url_counts[url] = url_counts.get(url, 0) + 1

            # Find the top requested URLs
            top_urls = sorted(url_counts.items(), key=lambda x: x[1], reverse=True)[:5]

            # Print the analysis results
            print("Total Requests:", total_requests)
            print("Successful Requests:", success_count)
            print("Top Requested URLs:")
            for url, count in top_urls:
                print(f"{url}: {count}")
    except FileNotFoundError:
        print(f"Log file '{log_file}' not found.")
    except IOError:
        print("Error reading log file.")

# Test the analyze_server_log function
log_file = "access.log"
analyze_server_log(log_file)
