import psutil
import time

pid = int(input("PID:"))
count = 0
stats = []
process = psutil.Process(pid)
while psutil.pid_exists(pid):
    stats.append((count, str(process.cpu_percent() / psutil.cpu_count()), str(process.memory_percent())))
    count += 1
    time.sleep(1)

with open("stats.csv", 'w') as f:
    f.write("ID;CPU;MEM\n")
    for stat in stats:
        f.write(f"{stat[0]};{stat[1]};{stat[2]}\n")



