# cat pyPerf.py
#!/bin/python
 
# $ cat sos_commands/python/python-version
# Python 2.7.5
# Customer runs python 2.7.5, and so I tested it on 2.7.5
# needs to be run as root for perf access.
 
import os
from datetime import datetime
import time
 
LOAD_THRESHOLD = 2           # At this load average level the script will collect perf data every 30 seconds until load drops below.
TICKS_THRESHOLD = 10         # The number of 30 second intervals to collect perf data.
 
def dateToStr():
        present = datetime.now()
        #      YYYY-MM-DD-HH:MM:SS
        return "%s-%s-%s-%s" % (present.strftime("%Y"), present.strftime("%m"), present.strftime("%d"), present.strftime("%H:%M:%S"))
 
def main():
        exit = False
        ticks = 0
        print " ==============================================================="
        print "| "
        print "| Starting load measurement of threshold %s at %s " % (LOAD_THRESHOLD, dateToStr())
        print "| "
        print " ==============================================================="
 
        while True:
                load = os.getloadavg() # get the 1min,5min,15min load avgs. Entry 0 is 1min
                if load[0] > LOAD_THRESHOLD:
                        print " ==============================================================="
                        print "| "
                        print "| Current Load of %s exceeds the threshold of %s at %s " % (os.getloadavg(), LOAD_THRESHOLD, dateToStr())
                        print "| Creating perf data set perf-%s.data" % (dateToStr())
                        print "| Tick interval %s of %s" % (ticks, TICKS_THRESHOLD)
                        print "| "
                        print " ==============================================================="
                        os.system("perf record -agT -- sleep 30")
                        os.system("perf archive")
                        # make sure that the time label does not change between renames
                        dateTimeString = dateToStr()
                        os.rename("perf.data", "perf-"+dateTimeString+".data")
                        os.rename("perf.data.tar.bz2", "perf-"+dateTimeString+".data.tar.bz2")
                        ticks += 1
                else:
                        time.sleep(0.5)
                if ticks >= TICKS_THRESHOLD:
                        break
        if ticks >= TICKS_THRESHOLD:
                print "TICKS_THRESHOLD met %s" % (TICKS_THRESHOLD)
               
main()



"""
SAMPLE OUTPUT EXAMPLE

# ./pyPerf.py
 ===============================================================
|
| Starting load measurement of threshold 2 at 2021-02-09-18:09:03
|
 ===============================================================
 ===============================================================
|
| Current Load of (2.15, 0.96, 1.25) exceeds the threshold of 2 at 2021-02-09-18:09:46
| Creating perf data set perf-2021-02-09-18:09:46.data
| Tick interval 0 of 10
|
 ===============================================================
[ perf record: Woken up 103 times to write data ]
[ perf record: Captured and wrote 30.862 MB perf.data (239811 samples) ]
Now please run:
 
$ tar xvf perf.data.tar.bz2 -C ~/.debug
 
wherever you need to run 'perf report' on.
 ===============================================================
|
| Current Load of (3.83, 1.53, 1.43) exceeds the threshold of 2 at 2021-02-09-18:10:29
| Creating perf data set perf-2021-02-09-18:10:29.data
| Tick interval 1 of 10
|
 ===============================================================
[ perf record: Woken up 117 times to write data ]
[ perf record: Captured and wrote 30.772 MB perf.data (239246 samples) ]
Now please run:
 
$ tar xvf perf.data.tar.bz2 -C ~/.debug
 
wherever you need to run 'perf report' on.
 ===============================================================
|
| Current Load of (4.43, 1.93, 1.56) exceeds the threshold of 2 at 2021-02-09-18:11:06
| Creating perf data set perf-2021-02-09-18:11:06.data
| Tick interval 2 of 10
|
 ===============================================================
[ perf record: Woken up 43 times to write data ]
[ perf record: Captured and wrote 11.216 MB perf.data (86521 samples) ]
Now please run:
 
$ tar xvf perf.data.tar.bz2 -C ~/.debug
 
wherever you need to run 'perf report' on.
 ===============================================================
|
| Current Load of (2.66, 1.78, 1.53) exceeds the threshold of 2 at 2021-02-09-18:11:38
| Creating perf data set perf-2021-02-09-18:11:38.data
| Tick interval 3 of 10
|
 ===============================================================
[ perf record: Woken up 39 times to write data ]
[ perf record: Captured and wrote 10.249 MB perf.data (83332 samples) ]
Now please run:
 
$ tar xvf perf.data.tar.bz2 -C ~/.debug
 
wherever you need to run 'perf report' on.
^CTraceback (most recent call last):
  File "./pyPerf.py", line 53, in <module>
    main()       
  File "./pyPerf.py", line 47, in main
    time.sleep(0.5)
KeyboardInterrupt
 
 
 
 
 
# ls
perf-2021-02-09-18:10:29.data          perf-2021-02-09-18:11:38.data.tar.bz2
perf-2021-02-09-18:10:29.data.tar.bz2  perf-2021-02-09-18:12:10.data
perf-2021-02-09-18:11:06.data          perf-2021-02-09-18:12:10.data.tar.bz2
perf-2021-02-09-18:11:06.data.tar.bz2  pyPerf.py
perf-2021-02-09-18:11:38.data
"""















