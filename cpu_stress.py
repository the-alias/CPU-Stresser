import hashlib
import os
import multiprocessing
import psutil
import keyboard
import sys
import time

def worker():
    data = os.urandom(1024)
    while True:
        hashlib.sha512(data).hexdigest()

def monitor_and_adjust(intensity):
    sys.stdout.write("\033[K")
    print(f"Workers started: {len(intensity)}",end='\r')
    while True:
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
            if percentage < 85:
                intensity[i] +=1
        print(f"CPU Core {i}: {percentage}% usage  ",end='\r')
        sys.stdout.flush()
        time.sleep(1)
            
def hotkey_listener():
    keyboard.wait('s+o+t')
    os._exit(0)

if __name__ == "__main__":
    psutil.Process(os.getpid()).nice(psutil.IDLE_PRIORITY_CLASS)
    cpu_count = multiprocessing.cpu_count()
    intensity = multiprocessing.Manager().list([1 for _ in range(cpu_count)])

    for _ in range(cpu_count):
        multiprocessing.Process(target=worker).start()

    monitor_process = multiprocessing.Process(target=monitor_and_adjust,args=(intensity,))
    monitor_process.start()

    hotkey_process = multiprocessing.Process(target=hotkey_listener)
    hotkey_process.start()
    hotkey_process.join()

    monitor_process.terminate()