#!/usr/bin/env python3
"""
Migrated timed_interrupt module for aws2tf that uses ConfigurationManager.

This module contains progress tracking and interrupt handling functions updated to use
ConfigurationManager instead of global variables while maintaining all
timing and progress reporting functionality.
"""

import time
import threading
import multiprocessing
from typing import Optional, Callable
from .config import ConfigurationManager


class Counter:
    """
    Progress counter with timed interrupts for status reporting.
    
    This class provides periodic status updates during long-running operations
    using ConfigurationManager for tracking messages and timing information.
    """
    
    def __init__(self, config: ConfigurationManager, increment: int = 20):
        """
        Initialize the counter with configuration.
        
        Args:
            config: Configuration manager for tracking messages and timing.
            increment: Time interval in seconds between status updates.
        """
        self.config = config
        self.next_t = time.time()
        self.i = 0
        self.done = False
        self.increment = increment
        self.t = None
        self.start_time = time.time()
        
        # Start the timer
        self._run()
    
    def _run(self):
        """Internal method to handle timed status updates."""
        try:
            elapsed_seconds = self.i * self.increment
            tracking_message = self.config.get_tracking_message()
            
            # Get estimated time if available
            try:
                estimated_time = self.config.processing.get_estimated_time()
                if estimated_time > 0:
                    print(f"STATUS: {elapsed_seconds}s elapsed (est. {estimated_time:.1f}s) {tracking_message}")
                else:
                    print(f"STATUS: {elapsed_seconds}s elapsed {tracking_message}")
            except AttributeError:
                # Fallback if estimated time not available
                print(f"STATUS: {elapsed_seconds}s elapsed {tracking_message}")
            
            self.next_t += self.increment
            self.i += 1
            
            if not self.done:
                delay = max(0, self.next_t - time.time())
                self.t = threading.Timer(delay, self._run)
                self.t.start()
                
        except Exception as e:
            if self.config.is_debug_enabled():
                print(f"Error in timed interrupt: {str(e)}")
            # Continue running even if there's an error
            if not self.done:
                self.t = threading.Timer(self.increment, self._run)
                self.t.start()
    
    def stop(self):
        """Stop the timed interrupt counter."""
        self.done = True
        if self.t:
            self.t.cancel()
        
        # Report final elapsed time
        total_elapsed = time.time() - self.start_time
        if self.config.is_debug_enabled():
            print(f"Timer stopped after {total_elapsed:.2f} seconds")
    
    def update_message(self, message: str):
        """
        Update the tracking message.
        
        Args:
            message: New tracking message to display.
        """
        self.config.set_tracking_message(message)
    
    def get_elapsed_time(self) -> float:
        """
        Get the total elapsed time since counter started.
        
        Returns:
            Elapsed time in seconds.
        """
        return time.time() - self.start_time
    
    def reset(self):
        """Reset the counter to start from zero."""
        self.i = 0
        self.next_t = time.time()
        self.start_time = time.time()


class TimedInterruptManager:
    """
    Manager for timed interrupts with configuration support.
    
    This class manages the lifecycle of timed interrupt counters and provides
    a clean interface for progress tracking throughout the application.
    """
    
    def __init__(self, config: ConfigurationManager):
        """
        Initialize the timed interrupt manager.
        
        Args:
            config: Configuration manager for tracking and settings.
        """
        self.config = config
        self.active_counter = None
        self.default_increment = 20
    
    def start_counter(self, increment: Optional[int] = None, message: Optional[str] = None) -> Counter:
        """
        Start a new timed interrupt counter.
        
        Args:
            increment: Time interval between updates (default: 20 seconds).
            message: Initial tracking message.
            
        Returns:
            The created Counter instance.
        """
        # Stop any existing counter
        self.stop_counter()
        
        if increment is None:
            increment = self.default_increment
        
        if message:
            self.config.set_tracking_message(message)
        
        self.active_counter = Counter(self.config, increment)
        return self.active_counter
    
    def stop_counter(self):
        """Stop the active counter if one exists."""
        if self.active_counter:
            self.active_counter.stop()
            self.active_counter = None
    
    def update_message(self, message: str):
        """
        Update the tracking message for the active counter.
        
        Args:
            message: New tracking message.
        """
        self.config.set_tracking_message(message)
    
    def is_active(self) -> bool:
        """
        Check if a counter is currently active.
        
        Returns:
            True if a counter is running.
        """
        return self.active_counter is not None and not self.active_counter.done
    
    def get_elapsed_time(self) -> float:
        """
        Get elapsed time from the active counter.
        
        Returns:
            Elapsed time in seconds, or 0 if no active counter.
        """
        if self.active_counter:
            return self.active_counter.get_elapsed_time()
        return 0.0


def setup_multiprocessing_cores(config: ConfigurationManager) -> int:
    """
    Set up multiprocessing core count in configuration.
    
    Args:
        config: Configuration manager to update with core count.
        
    Returns:
        Number of cores configured for use.
    """
    logical_cores = multiprocessing.cpu_count()
    print(f"Logical cores: {logical_cores}")
    
    # Calculate cores to use (logical cores * 2, max 16)
    cores = logical_cores * 2
    if cores > 16:
        cores = 16
    
    config.set_cores(cores)
    print(f"Configured to use {cores} cores for processing")
    
    return cores


def create_timed_interrupt(config: ConfigurationManager, increment: int = 20) -> Counter:
    """
    Create a timed interrupt counter with configuration.
    
    Args:
        config: Configuration manager for tracking.
        increment: Time interval between status updates.
        
    Returns:
        Counter instance for progress tracking.
    """
    return Counter(config, increment)


# Compatibility functions for existing code

def create_legacy_counter(increment: int = 20) -> 'LegacyCounter':
    """
    Create a legacy counter for backward compatibility.
    
    This function creates a counter that mimics the old global behavior
    but uses a minimal configuration setup.
    
    Args:
        increment: Time interval between updates.
        
    Returns:
        Legacy counter instance.
    """
    # Create a minimal config for legacy support
    from .config import ConfigurationManager
    config = ConfigurationManager()
    config.set_tracking_message("Processing...")
    
    return LegacyCounter(config, increment)


class LegacyCounter(Counter):
    """
    Legacy counter for backward compatibility.
    
    This class provides the same interface as the original Counter
    but uses ConfigurationManager internally.
    """
    
    def __init__(self, config: ConfigurationManager, increment: int = 20):
        """
        Initialize legacy counter.
        
        Args:
            config: Configuration manager.
            increment: Time interval between updates.
        """
        super().__init__(config, increment)
    
    def set_message(self, message: str):
        """
        Set tracking message (legacy interface).
        
        Args:
            message: Tracking message to set.
        """
        self.update_message(message)


# Module-level functions for easy integration

def initialize_timed_interrupt(config: ConfigurationManager) -> TimedInterruptManager:
    """
    Initialize the timed interrupt system with configuration.
    
    Args:
        config: Configuration manager for the application.
        
    Returns:
        TimedInterruptManager instance for managing progress tracking.
    """
    # Set up multiprocessing cores
    setup_multiprocessing_cores(config)
    
    # Create and return the manager
    return TimedInterruptManager(config)


def get_system_info(config: ConfigurationManager) -> dict:
    """
    Get system information for performance tuning.
    
    Args:
        config: Configuration manager.
        
    Returns:
        Dictionary with system information.
    """
    logical_cores = multiprocessing.cpu_count()
    configured_cores = config.get_cores()
    
    return {
        'logical_cores': logical_cores,
        'configured_cores': configured_cores,
        'core_utilization': configured_cores / logical_cores,
        'max_recommended_cores': min(16, logical_cores * 2)
    }


# Progress tracking utilities

class ProgressTracker:
    """
    Enhanced progress tracking with percentage completion.
    """
    
    def __init__(self, config: ConfigurationManager, total_items: int, 
                 description: str = "Processing"):
        """
        Initialize progress tracker.
        
        Args:
            config: Configuration manager.
            total_items: Total number of items to process.
            description: Description of the operation.
        """
        self.config = config
        self.total_items = total_items
        self.processed_items = 0
        self.description = description
        self.start_time = time.time()
        
        # Set initial message
        self.update_progress()
    
    def increment(self, count: int = 1):
        """
        Increment the progress counter.
        
        Args:
            count: Number of items processed.
        """
        self.processed_items += count
        self.update_progress()
    
    def update_progress(self):
        """Update the progress message."""
        if self.total_items > 0:
            percentage = (self.processed_items / self.total_items) * 100
            elapsed = time.time() - self.start_time
            
            if self.processed_items > 0:
                estimated_total = elapsed * (self.total_items / self.processed_items)
                remaining = estimated_total - elapsed
                message = (f"{self.description}: {self.processed_items}/{self.total_items} "
                          f"({percentage:.1f}%) - {remaining:.1f}s remaining")
            else:
                message = f"{self.description}: {self.processed_items}/{self.total_items} (0.0%)"
        else:
            message = f"{self.description}: {self.processed_items} items processed"
        
        self.config.set_tracking_message(message)
    
    def complete(self):
        """Mark progress as complete."""
        elapsed = time.time() - self.start_time
        message = f"{self.description}: Completed {self.processed_items} items in {elapsed:.2f}s"
        self.config.set_tracking_message(message)
        
        if self.config.is_debug_enabled():
            rate = self.processed_items / elapsed if elapsed > 0 else 0
            print(f"Processing rate: {rate:.2f} items/second")


# Context manager for timed operations

class TimedOperation:
    """
    Context manager for timed operations with automatic progress tracking.
    """
    
    def __init__(self, config: ConfigurationManager, operation_name: str, 
                 increment: int = 20):
        """
        Initialize timed operation.
        
        Args:
            config: Configuration manager.
            operation_name: Name of the operation for tracking.
            increment: Time interval for progress updates.
        """
        self.config = config
        self.operation_name = operation_name
        self.increment = increment
        self.counter = None
        self.start_time = None
    
    def __enter__(self):
        """Start the timed operation."""
        self.start_time = time.time()
        self.config.set_tracking_message(f"Starting {self.operation_name}...")
        self.counter = Counter(self.config, self.increment)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """End the timed operation."""
        if self.counter:
            self.counter.stop()
        
        elapsed = time.time() - self.start_time
        if exc_type is None:
            self.config.set_tracking_message(f"Completed {self.operation_name} in {elapsed:.2f}s")
        else:
            self.config.set_tracking_message(f"Failed {self.operation_name} after {elapsed:.2f}s")
        
        return False  # Don't suppress exceptions
    
    def update_message(self, message: str):
        """
        Update the operation message.
        
        Args:
            message: New message to display.
        """
        full_message = f"{self.operation_name}: {message}"
        self.config.set_tracking_message(full_message)