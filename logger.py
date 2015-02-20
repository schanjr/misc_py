# -*- coding: utf-8 -*-
import sys



class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open(__file__.split('\\')[-1] + "_logger.txt", "a+")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  


#Sample Usage
#sys.stdout = Logger()
