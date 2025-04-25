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
    return dt - timedelta(minutes=dt.minute % 5,
                          seconds=dt.second,
                          microseconds=dt.microsecond)

# Initialize counters
bins = defaultdict(lambda: {"requests": 0, "bytes": 0})

# Read and parse the log file
with open("access_log", "r") as f:
    for line in f:
        match = LOG_PATTERN.search(line)
        if match:
            dt_str, byte_str = match.groups()
            try:
                dt = parse_datetime(dt_str)
                bin_time = round_down_to_5min(dt)
                bins[bin_time]["requests"] += 1
                bins[bin_time]["bytes"] += int(byte_str) if byte_str != '-' else 0
            except Exception as e:
                print(f"Error parsing line: {line.strip()} ({e})")

# Sort bins
sorted_bins = sorted(bins.items())

# Extract data
times = [time for time, _ in sorted_bins]
requests = [data["requests"] for _, data in sorted_bins]
bytes_transferred = [data["bytes"] for _, data in sorted_bins]

# Plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Plot requests
ax1.plot(times, requests, marker='o', linestyle='-', color='blue')
ax1.set_ylabel("Number of Requests")
ax1.set_title("Requests per 5-Minute Bin")
ax1.grid(True)

# Plot bytes
ax2.plot(times, bytes_transferred, marker='o', linestyle='-', color='green')
ax2.set_ylabel("Bytes Transferred")
ax2.set_title("Bytes Transferred per 5-Minute Bin")
ax2.set_xlabel("Time")
ax2.grid(True)

# Improve x-axis formatting
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
fig.autofmt_xdate()

plt.tight_layout()
plt.show()
