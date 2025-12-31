import time
import threading
import context
import os
import logging

log = logging.getLogger('aws2tf')

class Counter():
    
    def __init__(self, increment):
        self.next_t = time.time()
        self.i=0
        self.done=False
        self.increment = increment
        self.t = None
        self._run()
        

    def _run(self):
        # Only show STATUS messages if enabled
        if context.show_status or context.debug:
            log.info("STATUS: " + str(self.i*self.increment) + "s elapsed "+ context.tracking_message)
        
        self.next_t+=self.increment
        self.i+=1
        if not self.done:
            self.t=threading.Timer( self.next_t - time.time(), self._run)
            self.t.start()
    
    def stop(self):
        self.done=True
        if self.t is not None:
            self.t.cancel()


# Lazy initialization to prevent semaphore leaks
logical_cores = None
timed_int = None

def initialize_cores():
    """Initialize core count. Call this after validation."""
    global logical_cores
    if logical_cores is None:
        logical_cores = os.cpu_count()
        log.info("Logical cores: " + str(logical_cores))
        context.cores = logical_cores * 2
        if context.cores > 16: context.cores = 16
    return logical_cores

def initialize_timer(increment=20):
    """Initialize the timed interrupt counter. Call this after validation."""
    global timed_int
    # Ensure cores are initialized first
    initialize_cores()
    if timed_int is None:
        timed_int = Counter(increment=increment)
    return timed_int

def stop_timer():
    """Stop the timer if it's running."""
    global timed_int
    if timed_int is not None:
        timed_int.stop()




