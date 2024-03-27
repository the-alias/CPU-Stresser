import hashlib, os, multiprocessing, time, psutil

def worker():
    data = os.urandom(1024)
    start_time = time.time()
    while time.time() - start_time < 5:  # Run for 2 minutes
        hashlib.sha512(data).hexdigest()


if __name__ == "__main__":
    multiprocessing.freeze_support()
    try:
        max_workers = 600
        processes = []
        count = 0
        wait = 1
        for i in range(max_workers):
            #print("Worker:",i)
            count += 1
            if count == 10:
                wait = 0
                count = 0
            while wait == 0:
                cpu_usage = psutil.cpu_percent(percpu=True)
                avg_cpu_usage= sum(cpu_usage)/len(cpu_usage)
                #print(avg_cpu_usage,i)
                if avg_cpu_usage > 85:
                    time.sleep(1/60)
                else:
                     wait = 1

            p = multiprocessing.Process(target=worker)
            p.start()
            processes.append(p)

        for p in processes:
            p.join()  # Wait for each worker to finish
    except KeyboardInterrupt:
        for p in processes:
            p.terminate()  # Terminate any remaining workers if interrupted
