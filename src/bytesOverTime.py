import re
from datetime import datetime, timedelta
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Regex to parse typical access log lines
LOG_PATTERN = re.compile(
    r'\[([^\]]+)\] "[A-Z]+ [^"]+" \d+ (\d+|-)'
)

# Function to parse datetime from log
def parse_datetime(dt_str):
    return datetime.strptime(dt_str, "%d/%b/%Y:%H:%M:%S %z")

# Function to round down to nearest 5 minutes
def round_down_to_5min(dt):
    return dt - timedelta(minutes=dt.minute % 5, seconds=dt.second, microseconds=dt.microsecond)

# Initialize counters
bins = defaultdict(lambda: {"requests": 0, "bytes": 0})

# Read and parse the log file
with open("/Users/ewen/MyProg/PEI2/projetS2/python_script/src/sample_access_log", "r") as f:
    for line in f:
        match = LOG_PATTERN.search(line)
        if match:
            dt_str, byte_str = match.groups()
            try:
                dt = parse_datetime(dt_str)
                bin_time = round_down_to_5min(dt)
                bins[bin_time]["requests"] += 1
                bins[bin_time]["bytes"] += int(byte_str)
            except Exception as e:
                print(f"Error parsing line: {line.strip()} ({e})")

# Sort bins
sorted_bins = sorted(bins.items())

# Extract data
times = [time for time, _ in sorted_bins]
requests = [data["requests"]//60*5 for _, data in sorted_bins]
bytes_transferred = [data["bytes"] for _, data in sorted_bins]

# Plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 10), sharex=True)

# Plot requests
ax1.bar(times, requests, color='blue', width=0.005)
ax1.set_ylabel("Number of Requests")
ax1.set_title("Requests per 5-Minute Bin")
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.legend(["Requests"], loc="upper left")

# Plot bytes
ax2.bar(times, bytes_transferred, color='green', width=0.005)
ax2.set_ylabel("Bytes Transferred")
ax2.set_title("Bytes Transferred per 5-Minute Bin")
ax2.set_xlabel("Time")
ax2.grid(axis='y', linestyle='--', alpha=0.7)
ax2.legend(["Bytes Transferred"], loc="upper left")

# Improve x-axis formatting
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax2.xaxis.set_major_locator(mdates.HourLocator(interval=1))  # Set tick interval to 1 hour
fig.autofmt_xdate(rotation=45)  # Rotate x-axis labels for better readability

# Save and show the plot
fig.tight_layout()
fig.savefig("bytes_count_improved.png")
plt.show()
