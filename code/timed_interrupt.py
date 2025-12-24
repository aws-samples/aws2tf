import time
import threading
import context
import multiprocessing
import logging

log = logging.getLogger('aws2tf')

class Counter():
    
    def __init__(self, increment):
        self.next_t = time.time()
        self.i=0
        self.done=False
        self.increment = increment
        self._run()
        

    def _run(self):
        #print("STATUS: " + str(self.i*self.increment) + "s elapsed (est. "+str(context.esttime) +"s) "+ context.tracking_message)
        log.info("STATUS: " + str(self.i*self.increment) + "s elapsed "+ context.tracking_message)
        self.next_t+=self.increment
        self.i+=1
        if not self.done:
            self.t=threading.Timer( self.next_t - time.time(), self._run)
            self.t.start()
    
    def stop(self):
        self.done=True
        self.t.cancel()


logical_cores = multiprocessing.cpu_count()
log.info("Logical cores: " + str(logical_cores))
context.cores = logical_cores * 2
if context.cores > 16: context.cores = 16
timed_int=Counter(increment = 20)



