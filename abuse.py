import subprocess
import time
from datetime import datetime, timedelta

# start_date = datetime(2000, 1, 1)
# end_date = datetime(2024, 12, 31)
# delta = timedelta(days=1)

# current_date = start_date

# Перебор дат и отправка запросов
while current_date <= end_date:
    submission = current_date.strftime('%m/%d/%Y')
    curl_command = ""
    result = subprocess.run(curl_command, shell=True, capture_output=True, text=True)
    print(f"Sent request for date: {submission}, Response: {result.stdout}")

    with open('response_log.txt', 'a') as f:
        f.write(f"Sent request for date: {submission}, Response: {result.stdout}\n")

    time.sleep(1)

    current_date += delta
