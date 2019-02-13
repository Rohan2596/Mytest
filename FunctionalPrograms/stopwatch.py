import datetime
def start():
    start=datetime.datetime.now().microsecond
    return start
def stop(start):
    stop=datetime.datetime.now().microsecond
    return (stop - start)
start=start()
print(stop(start))