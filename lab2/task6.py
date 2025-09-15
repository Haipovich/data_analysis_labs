import requests

url = 'https://www.py4e.com/code3/mbox.txt'
response = requests.get(url)
mbox = response.text

all_lines = mbox.split('\n')

email_count = {}

for line in all_lines:
    if line.startswith("From "):
        parts = line.split()
        if len(parts) > 1:
            email = parts[1]
            email_count[email] = email_count.get(email, 0) + 1

if email_count:
    max_email = max(email_count, key=email_count.get)
    max_count = email_count[max_email]
    print(f"The most active sender: {max_email} — {max_count} писем")
else:
    print("No sender found.")
