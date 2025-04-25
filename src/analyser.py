import re
from collections import Counter

LOG_FILE = "/logs/access_log"

def parse_log(file_path):
    ip_pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+)')
    with open(file_path, "r") as f:
        ips = [ip_pattern.match(line).group(1) for line in f if ip_pattern.match(line)]
    return Counter(ips)

if __name__ == "__main__":
    counts = parse_log(LOG_FILE)
    for ip, count in counts.most_common():
        print(f"{ip}: {count} requests")