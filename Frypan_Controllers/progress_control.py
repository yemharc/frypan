import tkinter as tk
import tkinter.ttk as ttk

import threading

class Progress:
    def __init__(self, parent, side, fill):
        self.maximum = 100
        self.interval = 10
        self.Progressbar = ttk.Progressbar(parent, orient=tk.HORIZONTAL,
                                           mode="indeterminate",
                                           maximum=self.maximum)
        self.Progressbar.pack(side=side, fill=fill)

        self.thread = threading.Thread()
        self.thread.__init__(target=self.Progressbar.start(self.interval), args=())
        
        self.thread.start()
    
    def __del__(self):
        print("delete instance : ", __name__)
        
    def stop(self):
        if not self.thread.isAlive():
            VALUE = self.Progressbar["value"]
            self.Progressbar.stop()
            self.Progressbar["value"] = VALUE
            
    def start(self):
        if not self.thread.isAlive():
            VALUE = self.Progressbar["value"]
            self.Progressbar.configure(mode="indeterminate",
                                       maximum=self.maximum,
                                       value=VALUE)
            self.Progressbar.start(self.interval)
            
    def clear(self):
        if not self.thread.isAlive():
            self.Progressbar.stop()
            self.Progressbar.configure(mode="determinate", value=0)
            
    def complete(self):
        if not self.thread.isAlive():
            self.Progressbar.stop()
            self.Progressbar.configure(mode="determinate",
                                       maximum=self.maximum,
                                       value=self.maximum)