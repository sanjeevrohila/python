import threading
import time

def do_something():
    while True:
        with open("/tmp/current_time.txt", "a") as f:
            f.write("The time is now " + time.ctime()+"\n")
        time.sleep(2)


if __name__ == "__main__":
    t = threading.Thread(target=do_something)
    t.deamon = True
    t.start()
    print "Exiting main Thread at %s" %time.ctime()