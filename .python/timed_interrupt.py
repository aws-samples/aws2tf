import time
import threading
import globals
import multiprocessing
import os
from ctypes import cdll, byref, create_string_buffer
import platform

class Counter():
    
    def __init__(self, increment):
        self.next_t = time.time()
        self.i=0
        self.done=False
        self.increment = increment
        self._run()
        

    def _run(self):
        print("STATUS: " + str(self.i*self.increment) + "s elapsed (est. "+str(globals.esttime) +"s) "+ globals.tracking_message)
        self.next_t+=self.increment
        self.i+=1
        if not self.done:
            self.t=threading.Timer( self.next_t - time.time(), self._run)
            self.t.start()
    
    def stop(self):
        self.done=True
        self.t.cancel()


logical_cores = multiprocessing.cpu_count()
print("Logical cores: " + str(logical_cores))
globals.cores = logical_cores * 2
if globals.cores > 16: globals.cores = 16
timed_int=Counter(increment = 20)



