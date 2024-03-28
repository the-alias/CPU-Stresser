import multiprocessing
import time
import random

def worker_process():
    time.sleep(random.randint(1, 5))

def create_processes(target, num_processes, max_concurrent_processes):
    active_processes = []
    for _ in range(num_processes):
        active_processes = [p for p in active_processes if p.is_alive()]
        
        while len(active_processes) >= max_concurrent_processes:
            time.sleep(0.5)
            active_processes = [p for p in active_processes if p.is_alive()]
        
        p = multiprocessing.Process(target=target)
        p.start()
        active_processes.append(p)
    
    for p in active_processes:
        p.join()

if __name__ == "__main__":
    multiprocessing.freeze_support()  # Add freeze support for PyInstaller on Windows
    TOTAL_PROCESSES = 1000
    MAX_CONCURRENT_PROCESSES = 100
    
    create_processes(worker_process, TOTAL_PROCESSES, MAX_CONCURRENT_PROCESSES)
