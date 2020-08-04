import json

file_name = "Hellcase-1.json"

with open(file_name) as f_obj:
    data = f_obj.read()
    retrieve = json.loads(data)

counter = {}
for k, v in retrieve.items():
    if v not in counter:
        counter[v] = 1
    else:
        counter[v] += 1

file_name = "Counter.json"
with open(file_name, "w") as f_obj:
    json.dump(counter, f_obj)  # Converts to string



schedule.every().day.at("09:00").do(Task)
schedule.every().day.at("22:12").do(Task)

while True:
    schedule.run_pending()
    time.sleep(1)


