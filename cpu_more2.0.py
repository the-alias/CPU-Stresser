import hashlib, os, multiprocessing, time

def worker():
    data = os.urandom(1024)
    start_time = time.time()
    while time.time() - start_time < 120:  # Run for 2 minutes
        hashlib.sha512(data).hexdigest()

if __name__ == "__main__":
    max_workers = 100
    processes = []

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
