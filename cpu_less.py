import os, multiprocessing, time

def worker():
    data = os.urandom(1024)
    start_time = time.time()
    x=0
    while time.time() - start_time < 60:  # Run for 2 minutes
        for i in data:
            x+=i


if __name__ == "__main__":
    max_workers = 100
    processes = []
    multiprocessing.freeze_support()

    for _ in range(max_workers):
        p = multiprocessing.Process(target=worker)
        p.start()
        processes.append(p)

    try:
        for p in processes:
            p.join()  # Wait for each worker to finish
    except KeyboardInterrupt:
        for p in processes:
            p.terminate()  # Terminate any remaining workers if interrupted