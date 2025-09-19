import csv
from collections import Counter, defaultdict

# Read CSV file
with open("AWS_S3_HoneyBucketLogs.csv", "r") as f:
    reader = csv.DictReader(f)

    ip_counter = Counter()
    ip_user_map = defaultdict(list)  # to map IP → [User IDs]

    for row in reader:
        ip = row.get("Source IP")
        user = row.get("User ID")
        
        if ip:
            ip_counter[ip] += 1
            if user:
                ip_user_map[ip].append(user)

# 🔹 Top 10 Source IPs
print("🔹 Top 10 Source IPs:")
for ip, count in ip_counter.most_common(10):
    print(f"{ip} => {count} requests, Users: {set(ip_user_map[ip])}")
