import subprocess
import time
from datetime import datetime, timedelta

# Формирование дат для перебора
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

    # Логирование ответа в файл (добавьте нужный путь к файлу)
    with open('response_log.txt', 'a') as f:
        f.write(f"Sent request for date: {submission}, Response: {result.stdout}\n")

    # Время сна между запросами (в секундах)
    time.sleep(1)

    current_date += delta
