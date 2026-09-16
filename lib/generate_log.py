from datetime import datetime
import os
import requests


def generate_log(data):
    """
    Write a list of log entries to a timestamped text file.

    STEP 1: Validate input
        - `data` must be a list. If it isn't, raise a ValueError.

    STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")

    STEP 3: Write each entry in `data` to the file, one per line.

    STEP 4: Print a confirmation message and return the filename.
    """
    # STEP 1: Validate input
    if not isinstance(data, list):
        raise ValueError("data must be a list of log entries")

    # STEP 2: Generate a filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # STEP 3: Write the log entries to a file using File I/O
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename
    print(f"Log written to {filename}")

    return filename


def fetch_data():
    """Fetch a sample post from a public API using the `requests` package."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}


if __name__ == "__main__":
    # Use an installed package (requests) to pull in external data.
    post = fetch_data()
    title = post.get("title", "No title found")
    print("Fetched Post Title:", title)

    # Build the log entries, including data pulled from the API call above,
    # then write them out to a timestamped log file.
    log_entries = [
        "User logged in",
        "User updated profile",
        "Report exported",
        f"Fetched Post Title: {title}",
    ]
    generate_log(log_entries)
