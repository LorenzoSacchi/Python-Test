#! /usr/local/bin/python3

import subprocess
import threading
import time

class Mythread(threading.Thread):
    def run(self):
        print (f'from thread {self.name}')
        time.sleep(5)

def main():
    print(f'starting')
    #proc = subprocess.run(['/bin/ls','-l'])
    #print(f'return code {proc.returncode}')
    th1 = Mythread()
    th2 = Mythread()

    th1.start()
    th2.start()

    print(f'from main')
    th1.join()
    th2.join()

if __name__ == "__main__":
    main()