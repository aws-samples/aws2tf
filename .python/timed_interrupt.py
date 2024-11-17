import time
import threading
import globals

class Counter():
    def __init__(self, increment):
        self.next_t = time.time()
        self.i=0
        self.done=False
        self.increment = increment
        self._run()

    def _run(self):
        print("\naws2tf: " + str(self.i*self.increment) + " seconds, "+ globals.tracking_message+"\n")
        self.next_t+=self.increment
        self.i+=1
        if not self.done:
            threading.Timer( self.next_t - time.time(), self._run).start()
    
    def stop(self):
        self.done=True

timed_int=Counter(increment = 15)

