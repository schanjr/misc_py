import sys

def myexcepthook(exctype, value, traceback):
    if exctype == KeyboardInterrupt:
        print "Handler code goes here"
    else:
        sys.__excepthook__(exctype, value, traceback)
sys.excepthook = myexcepthook



#or something like

def main():
  print "This is a function"
  
if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print "exception caught on Keyboard Interrupt. 
