import hashlib, os, multiprocessing


def worker():
    data = os.urandom(1024)
    while True:
        hashlib.sha512(data).hexdigest()

if __name__ == "__main__":
    while True:
        multiprocessing.Process(target=worker).start()