import sys
import thread
from ryu.cmd import manager

def start_controller(port):
    sys.argv.append("/home/hpdn/ryu-controller/mycontroller.py")
    sys.argv.append("--ofp-tcp-listen-port=%d"%port)
    sys.argv.append("--observe-links")
    sys.argv.append("--verbose")
    #sys.argv.append("--enable-debugger")
    manager.main()

if __name__ == '__main__':
    thread.start_new_thread(start_controller,(6662,))
    thread.start_new_thread(start_controller,(6663,))