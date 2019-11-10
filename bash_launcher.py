"""
Bash Launcher
=============
Main executable file. Multi thread processes are running.
One writes the buffer and another reads and clear it.
Some Mutex strategy must be implemented in order to avoid data loose.

@Luis Arribas
"""

import subprocess
import threading

data_generator_path = '/Users/luisarribas/Data_pipeline_project/stream_data_generator.py'
data_reader_path = '/Users/luisarribas/Data_pipeline_project/stream_data_reader.py'


class MyThread(threading.Thread):
    def __init__(self, threadID, name, process):
        threading.Thread.__init__(self)
        self.process = process
        self.threadID = threadID
        self.name = name

    def run(self):
        print("Starting " + self.name)
        subprocess.run(["python", self.process])


# Create new threads
thread1 = MyThread(1, "data_generator", data_generator_path)
thread2 = MyThread(2, "data_reader", data_reader_path)

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Exiting Main Thread")
